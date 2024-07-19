# import cv2
# import numpy as np

# def give_directions(src, goal):
#     directions = []
#     current_pos = src
#     while current_pos != goal:
#         next_pos = [current_pos[0], current_pos[1]]  # Create a copy of current position
#         if current_pos[0] < goal[0]:
#             next_pos[0] += 1  # Move one step forward in the row direction
#             if current_pos[1] < goal[1]:
#                 next_pos[1] += 1  # Move one step right in the column direction
#                 directions.append("FORWARD_RIGHT")
#             elif current_pos[1] > goal[1]:
#                 next_pos[1] -= 1  # Move one step left in the column direction
#                 directions.append("FORWARD_LEFT")
#             else:
#                 directions.append("FORWARD")
#         elif current_pos[0] > goal[0]:
#             next_pos[0] -= 1  # Move one step backward in the row direction
#             if current_pos[1] < goal[1]:
#                 next_pos[1] += 1  # Move one step right in the column direction
#                 directions.append("BACKWARD_RIGHT")
#             elif current_pos[1] > goal[1]:
#                 next_pos[1] -= 1  # Move one step left in the column direction
#                 directions.append("BACKWARD_LEFT")
#             else:
#                 directions.append("BACKWARD")
#         else:
#             if current_pos[1] < goal[1]:
#                 next_pos[1] += 1  # Move one step right in the column direction
#                 directions.append("RIGHT")
#             elif current_pos[1] > goal[1]:
#                 next_pos[1] -= 1  # Move one step left in the column direction
#                 directions.append("LEFT")
#         current_pos = next_pos  # Update current position
    
#     return directions

# # Define the starting positions and the goal positions for each robot
# robot1_src = [1, 5]
# robot1_goal = [6, 3]

# robot2_src = [2, 6]
# robot2_goal = [8, 5]

# robot3_src = [3, 2]
# robot3_goal = [7, 7]

# # Get directions for each robot
# directions_robot1 = give_directions(robot1_src, robot1_goal)
# directions_robot2 = give_directions(robot2_src, robot2_goal)
# directions_robot3 = give_directions(robot3_src, robot3_goal)

# print("Directions for Robot 1:", directions_robot1)
# print("Directions for Robot 2:", directions_robot2)
# print("Directions for Robot 3:", directions_robot3)

# # Define grid parameters
# grid_size = 10
# grid_height = 7
# grid_width = 9
# cell_size = 50

# # Create blank image
# image = np.zeros((grid_height * cell_size, grid_width * cell_size, 3), dtype=np.uint8)

# # Draw grid lines
# for i in range(1, grid_height):
#     cv2.line(image, (0, i * cell_size), (grid_width * cell_size, i * cell_size), (255, 255, 255), 1)
# for j in range(1, grid_width):
#     cv2.line(image, (j * cell_size, 0), (j * cell_size, grid_height * cell_size), (255, 255, 255), 1)

# # Draw path for each robot
# def draw_path(image, src, goal, directions):
#     current_pos = src
#     for direction in directions:
#         if direction == "FORWARD":
#             next_pos = (current_pos[0] + 1, current_pos[1])
#         elif direction == "FORWARD_LEFT":
#             next_pos = (current_pos[0] + 1, current_pos[1] - 1)
#         elif direction == "FORWARD_RIGHT":
#             next_pos = (current_pos[0] + 1, current_pos[1] + 1)
#         elif direction == "BACKWARD":
#             next_pos = (current_pos[0] - 1, current_pos[1])
#         elif direction == "BACKWARD_LEFT":
#             next_pos = (current_pos[0] - 1, current_pos[1] - 1)
#         elif direction == "BACKWARD_RIGHT":
#             next_pos = (current_pos[0] - 1, current_pos[1] + 1)
#         elif direction == "RIGHT":
#             next_pos = (current_pos[0], current_pos[1] + 1)
#         elif direction == "LEFT":
#             next_pos = (current_pos[0], current_pos[1] - 1)
#         cv2.line(image, (current_pos[1] * cell_size + cell_size // 2, current_pos[0] * cell_size + cell_size // 2),
#                  (next_pos[1] * cell_size + cell_size // 2, next_pos[0] * cell_size + cell_size // 2),
#                  (0, 0, 255), 2)
#         current_pos = next_pos

# draw_path(image, robot1_src, robot1_goal, directions_robot1)
# draw_path(image, robot2_src, robot2_goal, directions_robot2)
# draw_path(image, robot3_src, robot3_goal, directions_robot3)

# # Mark starting and goal positions for each robot
# cv2.circle(image, (robot1_src[1] * cell_size + cell_size // 2, robot1_src[0] * cell_size + cell_size // 2), 5, (0, 255, 255), -1)
# cv2.circle(image, (robot1_goal[1] * cell_size + cell_size // 2, robot1_goal[0] * cell_size + cell_size // 2), 5, (0, 255, 255), -1)

# cv2.circle(image, (robot2_src[1] * cell_size + cell_size // 2, robot2_src[0] * cell_size + cell_size // 2), 5, (255, 255, 0), -1)
# cv2.circle(image, (robot2_goal[1] * cell_size + cell_size // 2, robot2_goal[0] * cell_size + cell_size // 2), 5, (255, 255, 0), -1)

# cv2.circle(image, (robot3_src[1] * cell_size + cell_size // 2, robot3_src[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)
# cv2.circle(image, (robot3_goal[1] * cell_size + cell_size // 2, robot3_goal[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)

# # Display the image
# cv2.imshow("Path", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

def give_directions(src, goal):
    directions = []
    current_pos = src
    while current_pos != goal:
        next_pos = [current_pos[0], current_pos[1]]  # Create a copy of current position
        if current_pos[0] < goal[0]:
            next_pos[0] += 1  # Move one step forward in the row direction
            if current_pos[1] < goal[1]:
                next_pos[1] += 1  # Move one step right in the column direction
                directions.append("FORWARD_RIGHT")
            elif current_pos[1] > goal[1]:
                next_pos[1] -= 1  # Move one step left in the column direction
                directions.append("FORWARD_LEFT")
            else:
                directions.append("FORWARD")
        elif current_pos[0] > goal[0]:
            next_pos[0] -= 1  # Move one step backward in the row direction
            if current_pos[1] < goal[1]:
                next_pos[1] += 1  # Move one step right in the column direction
                directions.append("BACKWARD_RIGHT")
            elif current_pos[1] > goal[1]:
                next_pos[1] -= 1  # Move one step left in the column direction
                directions.append("BACKWARD_LEFT")
            else:
                directions.append("BACKWARD")
        else:
            if current_pos[1] < goal[1]:
                next_pos[1] += 1  # Move one step right in the column direction
                directions.append("RIGHT")
            elif current_pos[1] > goal[1]:
                next_pos[1] -= 1  # Move one step left in the column direction
                directions.append("LEFT")
        current_pos = next_pos  # Update current position
    
    return directions

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Define the starting positions and the goal positions for each robot
robot1_src = [1, 5]
robot1_goal = [4, 3]

robot2_src = [2, 6]
robot2_goal = [6, 5]

robot3_src = [3, 2]
robot3_goal = [7, 7]

# Get directions for each robot
directions_robot1 = give_directions(robot1_src, robot1_goal)
directions_robot2 = give_directions(robot2_src, robot2_goal)
directions_robot3 = give_directions(robot3_src, robot3_goal)

print("Directions for Robot 1:", directions_robot1)
print("Directions for Robot 2:", directions_robot2)
print("Directions for Robot 3:", directions_robot3)

# Define grid parameters
grid_size = 12000
grid_height = 100
grid_width = 120
cell_size = 63 # 7*6

# Create blank image
image = np.zeros((grid_height * cell_size, grid_width * cell_size, 3), dtype=np.uint8)

# Draw grid lines
for i in range(1, grid_height):
    cv2.line(image, (0, i * cell_size), (grid_width * cell_size, i * cell_size), (255, 255, 255), 1)
for j in range(1, grid_width):
    cv2.line(image, (j * cell_size, 0), (j * cell_size, grid_height * cell_size), (255, 255, 255), 1)

# Draw path for each robot
def draw_path(image, src, goal, directions):
    current_pos = src
    for direction in directions:
        if direction == "FORWARD":
            next_pos = (current_pos[0] + 1, current_pos[1])
        elif direction == "FORWARD_LEFT":
            next_pos = (current_pos[0] + 1, current_pos[1] - 1)
        elif direction == "FORWARD_RIGHT":
            next_pos = (current_pos[0] + 1, current_pos[1] + 1)
        elif direction == "BACKWARD":
            next_pos = (current_pos[0] - 1, current_pos[1])
        elif direction == "BACKWARD_LEFT":
            next_pos = (current_pos[0] - 1, current_pos[1] - 1)
        elif direction == "BACKWARD_RIGHT":
            next_pos = (current_pos[0] - 1, current_pos[1] + 1)
        elif direction == "RIGHT":
            next_pos = (current_pos[0], current_pos[1] + 1)
        elif direction == "LEFT":
            next_pos = (current_pos[0], current_pos[1] - 1)
        cv2.line(image, (current_pos[1] * cell_size + cell_size // 2, current_pos[0] * cell_size + cell_size // 2),
                 (next_pos[1] * cell_size + cell_size // 2, next_pos[0] * cell_size + cell_size // 2),
                 (0, 0, 255), 2)
        current_pos = next_pos

def move_robot(src, goal, directions):
    current_pos = src
    for direction in directions:
        if current_pos == goal:
            break
        if direction == "FORWARD":
            next_pos = (current_pos[0] + 1, current_pos[1])
        elif direction == "FORWARD_LEFT":
            next_pos = (current_pos[0] + 1, current_pos[1] - 1)
        elif direction == "FORWARD_RIGHT":
            next_pos = (current_pos[0] + 1, current_pos[1] + 1)
        elif direction == "BACKWARD":
            next_pos = (current_pos[0] - 1, current_pos[1])
        elif direction == "BACKWARD_LEFT":
            next_pos = (current_pos[0] - 1, current_pos[1] - 1)
        elif direction == "BACKWARD_RIGHT":
            next_pos = (current_pos[0] - 1, current_pos[1] + 1)
        elif direction == "RIGHT":
            next_pos = (current_pos[0], current_pos[1] + 1)
        elif direction == "LEFT":
            next_pos = (current_pos[0], current_pos[1] - 1)
        current_pos = next_pos
    return current_pos

# Check which robot is closest to its goal
robot1_distance = distance(robot1_src, robot1_goal)
robot2_distance = distance(robot2_src, robot2_goal)
robot3_distance = distance(robot3_src, robot3_goal)

# Keep moving the closest robot until it is one grid away from its goal
while min(robot1_distance, robot2_distance, robot3_distance) > 1:
    if robot1_distance == min(robot1_distance, robot2_distance, robot3_distance):
        robot1_src = move_robot(robot1_src, robot1_goal, directions_robot1)
        robot1_distance = distance(robot1_src, robot1_goal)
    if robot2_distance == min(robot1_distance, robot2_distance, robot3_distance):
        robot2_src = move_robot(robot2_src, robot2_goal, directions_robot2)
        robot2_distance = distance(robot2_src, robot2_goal)
    if robot3_distance == min(robot1_distance, robot2_distance, robot3_distance):
        robot3_src = move_robot(robot3_src, robot3_goal, directions_robot3)
        robot3_distance = distance(robot3_src, robot3_goal)

# Draw paths for each robot after movement
draw_path(image, robot1_src, robot1_goal, directions_robot1)
draw_path(image, robot2_src, robot2_goal, directions_robot2)
draw_path(image, robot3_src, robot3_goal, directions_robot3)

# Mark starting and goal positions for each robot
cv2.circle(image, (robot1_src[1] * cell_size + cell_size // 2, robot1_src[0] * cell_size + cell_size // 2), 5, (255, 255, 0), -1)
cv2.circle(image, (robot1_goal[1] * cell_size + cell_size // 2, robot1_goal[0] * cell_size + cell_size // 2), 5, (255, 255, 0), -1)

cv2.circle(image, (robot2_src[1] * cell_size + cell_size // 2, robot2_src[0] * cell_size + cell_size // 2), 5, (0, 255, 255), -1)
cv2.circle(image, (robot2_goal[1] * cell_size + cell_size // 2, robot2_goal[0] * cell_size + cell_size // 2), 5, (0, 255, 255), -1)

cv2.circle(image, (robot3_src[1] * cell_size + cell_size // 2, robot3_src[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)
cv2.circle(image, (robot3_goal[1] * cell_size + cell_size // 2, robot3_goal[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)

# Display the image
cv2.imshow("Path", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
