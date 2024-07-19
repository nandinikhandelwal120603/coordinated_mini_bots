import cv2
import numpy as np
import time 


def findArucoMarkers(img, markersize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)# Create detector parameters
    # Detect ArUco markers
    # dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    # marker_corners, marker_ids, _ = cv2.aruco.detectMarkers(frame, dictionary, parameters=parameters)

    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(imgGray)
    
    if draw:
        cv2.aruco.drawDetectedMarkers(img, markerCorners, markerIds)
        
    return markerCorners, markerIds

def getMarkerCoordinates(markers, ids, point=0): 
    marker_array = []
    for marker in markers:
        marker_array.append([int(marker[0][point][0]), int(marker[0][point][1])])
    return marker_array, ids

def getMarkerCenter_foam(marker, ids):
    left_top, _ = getMarkerCoordinates(marker, ids, point=0)  # first corner
    right_top, _ = getMarkerCoordinates(marker, ids, point=1)  # 2nd corner    
    left_bot, _ = getMarkerCoordinates(marker, ids, point=2)  # 3rd corner
    right_bot, _ = getMarkerCoordinates(marker, ids, point=3)  # 4th corner
    
    if bool(left_top):
        center_X = (left_top[0][0] + right_top[0][0] + left_bot[0][0] + right_bot[0][0]) * 0.25
        center_Y = (left_top[0][1] + right_top[0][1] + left_bot[0][1] + right_bot[0][1]) * 0.25
        markerCenter = [[int(center_X), int(center_Y)]]
    else:
        markerCenter = [[0, 0]]
    print(markerCenter)
    return markerCenter

def draw_corners(img, corners):
    for corner in corners:
        cv2.circle(img, (corner[0], corner[1]), 10, (0, 255, 0), thickness=-1)



def draw_numbers(img, corners, ids):
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 4
    for corner, id in zip(corners, ids):
        cv2.putText(img, str(id), (corner[0] + 10, corner[1] + 10), font, 2, (0, 0, 0), thickness)

def show_spec(img, corners):
    font = cv2.FONT_HERSHEY_SIMPLEX
    thickness = 2
    amount_of_corners = len(corners)
    spec_string = str(amount_of_corners) + " markers found."
    cv2.putText(img, spec_string, (15, 15), font, 2, (0, 0, 250), thickness)



def draw_field(img, corners, ids):  
    # Only when 4 IDs are available
    if len(corners) == 4:
        # Sort corners based on the IDs
        markers_sorted = [corners[np.where(ids == i)[0][0]] for i in range(1, 5)]
        
        # Create contours
        contours = np.array(markers_sorted, dtype=np.int32)
        
        # Create overlay
        overlay = img.copy()
        
        # Fill polygon with color
        cv2.fillPoly(overlay, pts=[contours], color=(255, 215, 0))
        
        alpha = 0.4  # Transparency factor
        
        # Overlay transparent rectangle over the image
        img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
        square_found = True
    else:
        img_new = img
        square_found = False
    return img_new, square_found



def order_points(pts):
    # Initialize a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    # The top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # Compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # Return the ordered coordinates
    return rect

def four_point_transform(image, pts):
    # Obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    # Compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordinates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # Compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # Now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "bird's eye view",
    # (i.e., top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    # Compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    # Return the warped image
    return warped

def main():
    # Initialize USB camera
    cap = cv2.VideoCapture(0)
    
    # Initialize square points
    square_points = [
        [10, 10],
        [10, int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) - 10],
        [int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) - 10, 10],
        [int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) - 10, int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) - 10]
    ]

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame")
            break

        # Detect ArUco markers
        #marker_corners, marker_ids = cv2.aruco.detectMarkers(frame, dictionary=cv2.aruco.DICT_6X6_250)
        
        dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
        parameters = cv2.aruco.DetectorParameters()
        detector = cv2.aruco.ArucoDetector(dictionary, parameters)#
        markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)

        # Get marker coordinates
        if markerIds is not None:
            marker_coords, _ = getMarkerCoordinates(markerCorners, markerIds)
        else:
            marker_coords = []

        # Draw detected markers and their IDs
        frame_with_markers = frame.copy()
        if len(marker_coords) > 0:
            draw_corners(frame_with_markers, marker_coords)
            draw_numbers(frame_with_markers, marker_coords, markerIds)

        # Display number of markers found
        show_spec(frame_with_markers, marker_coords)

        # Draw filled field if 4 IDs are available
        frame_with_field, square_found = draw_field(frame_with_markers, marker_coords, markerIds)

        # Display frames
        cv2.imshow('Frame with Markers', frame_with_markers)
        cv2.imshow('Frame with Field', frame_with_field)

        # If 4 markers found, display the wrapped image in a new window
        if square_found:
            # Extract square and show in an extra window
            img_wrapped = four_point_transform(frame, np.array(square_points))
            cv2.imshow('Wrapped Image', img_wrapped)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()


# Entry point of the program
if __name__ == "__main__":
    main()
