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
#                 directions.append("DIAGONAL_RIGHT")
#             elif current_pos[1] > goal[1]:
#                 next_pos[1] -= 1  # Move one step left in the column direction
#                 directions.append("DIAGONAL_LEFT")
#             else:
#                 directions.append("FORWARD")
#         elif current_pos[0] > goal[0]:
#             next_pos[0] -= 1  # Move one step backward in the row direction
#             if current_pos[1] < goal[1]:
#                 next_pos[1] += 1  # Move one step right in the column direction
#                 directions.append("DIAGONAL_LEFT")
#             elif current_pos[1] > goal[1]:
#                 next_pos[1] -= 1  # Move one step left in the column direction
#                 directions.append("DIAGONAL_RIGHT")
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

# # Define the starting position and the goal position
# src = [2, 5]
# goal = [8, 8]

# # Get directions
# directions = give_directions(src, goal)
# print("Directions:", directions)

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

# # Draw path from src to goal
# current_pos = src
# for direction in directions:
#     if direction == "FORWARD":
#         next_pos = (current_pos[0] + 1, current_pos[1])
#     elif direction == "BACKWARD":
#         next_pos = (current_pos[0] - 1, current_pos[1])
#     elif direction == "RIGHT":
#         next_pos = (current_pos[0], current_pos[1] + 1)
#     elif direction == "LEFT":
#         next_pos = (current_pos[0], current_pos[1] - 1)
#     elif direction == "DIAGONAL_RIGHT":
#         next_pos = (current_pos[0] + 1, current_pos[1] + 1)
#     elif direction == "DIAGONAL_LEFT":
#         next_pos = (current_pos[0] + 1, current_pos[1] - 1)
#     cv2.line(image, (current_pos[1] * cell_size + cell_size // 2, current_pos[0] * cell_size + cell_size // 2),
#              (next_pos[1] * cell_size + cell_size // 2, next_pos[0] * cell_size + cell_size // 2),
#              (0, 0, 255), 2)
#     current_pos = next_pos

# # Mark starting and goal positions
# cv2.circle(image, (src[1] * cell_size + cell_size // 2, src[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)
# cv2.circle(image, (goal[1] * cell_size + cell_size // 2, goal[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)

# # Display the image
# cv2.imshow("Path", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#simple grid based path planning for 1 robot 

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

# Define the starting position and the goal position
src = [1, 5]
goal = [6, 3]

# Get directions
directions = give_directions(src, goal)
print("Directions:", directions)

# Define grid parameters
grid_size = 10
grid_height = 7
grid_width = 9
cell_size = 50

# Create blank image
image = np.zeros((grid_height * cell_size, grid_width * cell_size, 3), dtype=np.uint8)

# Draw grid lines
for i in range(1, grid_height):
    cv2.line(image, (0, i * cell_size), (grid_width * cell_size, i * cell_size), (255, 255, 255), 1)
for j in range(1, grid_width):
    cv2.line(image, (j * cell_size, 0), (j * cell_size, grid_height * cell_size), (255, 255, 255), 1)

# Draw path from src to goal
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

# Mark starting and goal positions
cv2.circle(image, (src[1] * cell_size + cell_size // 2, src[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)
cv2.circle(image, (goal[1] * cell_size + cell_size // 2, goal[0] * cell_size + cell_size // 2), 5, (0, 255, 0), -1)

# Display the image
cv2.imshow("Path", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
