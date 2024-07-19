import requests
import time

#SHIMPI'S PHONE
ESP8266_IP = "192.168.0.101"

def move_forward():
    url = f"http://{ESP8266_IP}/control?command=forward"
    response = requests.get(url)
    print(response.text)

def move_backward():
    url = f"http://{ESP8266_IP}/control?command=backward"
    response = requests.get(url)
    print(response.text)

def turn_left():
    url = f"http://{ESP8266_IP}/control?command=left"
    response = requests.get(url)
    print(response.text)

def turn_right():
    url = f"http://{ESP8266_IP}/control?command=right"
    response = requests.get(url)
    print(response.text)

def move_backward_left():
    url = f"http://{ESP8266_IP}/control?command=backleft"
    response = requests.get(url)
    print(response.text)

def move_backward_right():
    url = f"http://{ESP8266_IP}/control?command=backright"
    response = requests.get(url)
    print(response.text)

def move_forward_left():
    url = f"http://{ESP8266_IP}/control?command=forwardleft"
    response = requests.get(url)
    print(response.text)

def move_forward_right():
    url = f"http://{ESP8266_IP}/control?command=forwardright"
    response = requests.get(url)
    print(response.text)

def no_move_servo():
    url = f"http://{ESP8266_IP}/control?command=nomove"
    response = requests.get(url)
    print(response.text)

def generate_and_execute(directions):
    print("Given Directions:", directions)

    for direction in directions:
        if direction == 'FORWARD':
            print("Moving servo forward")
            move_forward()
            time.sleep(10)  # Delay for 5 seconds after moving the servo
        elif direction == 'BACKWARD':
            print("Moving servo backward")
            move_backward()
            time.sleep(10)
        elif direction == 'LEFT':
            print("Turning servo left")
            turn_left()
            time.sleep(10)
        elif direction == 'RIGHT':
            print("Turning servo right")
            turn_right()
            time.sleep(10)
        elif direction == 'BACKWARD_LEFT':
            print("Moving servo backward left")
            move_backward_left()
            time.sleep(10)
        elif direction == 'BACKWARD_RIGHT':
            print("Moving servo backward right")
            move_backward_right()
            time.sleep(10)
        elif direction == 'FORWARD_LEFT':
            print("Moving servo forward left")
            move_forward_left()
            time.sleep(10)
        elif direction == 'FORWARD_RIGHT':
            print("Moving servo forward right")
            move_forward_right()
            time.sleep(10)
        elif direction =='NO_MOVE':
            print("No movement needed")
            no_move_servo()
            

# Example list of directions
directions_list = ['BACKWARD_RIGHT', 'BACKWARD_LEFT', 'FORWARD_RIGHT', 'FORWARD_LEFT', 'BACKWARD', 'FORWARD', 'LEFT', 'RIGHT','NO_MOVE']
#directions_list = ['FORWARD_LEFT', 'FORWARD_LEFT', 'FORWARD', 'FORWARD', 'FORWARD']
# Example usage:
generate_and_execute(directions_list)

#

#--------------------------------------------------------------------------------------------

# import requests
# import time

# def move_servo(ip_address, command):
#     url = f"http://{ip_address}/control?command={command}"
#     response = requests.get(url)
#     print(response.text)

# def generate_and_execute(ip_address1, direction_list1, ip_address2, direction_list2):
#     print("Executing Direction List 1 on IP:", ip_address1)
#     for direction in direction_list1:
#         if direction == 'FORWARD':
#             move_servo(ip_address1, 'forward')
#         elif direction == 'BACKWARD':
#             move_servo(ip_address1, 'backward')
#         elif direction == 'LEFT':
#             move_servo(ip_address1, 'left')
#         elif direction == 'RIGHT':
#             move_servo(ip_address1, 'right')
#         elif direction == 'BACKWARD_LEFT':
#             move_servo(ip_address1, 'backleft')
#         elif direction == 'BACKWARD_RIGHT':
#             move_servo(ip_address1, 'backright')
#         elif direction == 'FORWARD_LEFT':
#             move_servo(ip_address1, 'forwardleft')
#         elif direction == 'FORWARD_RIGHT':
#             move_servo(ip_address1, 'forwardright')
#         else:
#             move_servo(ip_address1, 'nomove')

#     print("Executing Direction List 2 on IP:", ip_address2)
#     for direction in direction_list2:
#         if direction == 'FORWARD':
#             move_servo(ip_address2, 'forward')
#         elif direction == 'BACKWARD':
#             move_servo(ip_address2, 'backward')
#         elif direction == 'LEFT':
#             move_servo(ip_address2, 'left')
#         elif direction == 'RIGHT':
#             move_servo(ip_address2, 'right')
#         elif direction == 'BACKWARD_LEFT':
#             move_servo(ip_address2, 'backleft')
#         elif direction == 'BACKWARD_RIGHT':
#             move_servo(ip_address2, 'backright')
#         elif direction == 'FORWARD_LEFT':
#             move_servo(ip_address2, 'forwardleft')
#         elif direction == 'FORWARD_RIGHT':
#             move_servo(ip_address2, 'forwardright')
#         else:
#             move_servo(ip_address2, 'nomove')

# # Example lists of directions and IP addresses
# directions_list1 = ['FORWARD', 'BACKWARD', 'BACKWARD_LEFT', 'FORWARD_RIGHT', 'FORWARD']
# directions_list2 = ['BACKWARD', 'LEFT', 'RIGHT', 'FORWARD_LEFT']

# IP_address1 = "192.168.0.103"
# IP_address2 = "192.168.0.102"

# # Example usage:
# generate_and_execute(IP_address1, directions_list1, IP_address2, directions_list2)
