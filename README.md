# coordinated_mini_bots

# Coordinated Mini Bots - Success in Localization, Mapping, and Communication!

💫 I'm thrilled to announce the successful completion and presentation of our project, "Coordinated Mini Bots"! This project focused on developing a team of mini-robots capable of navigating an environment collaboratively.

## Project Highlights
💥 **Coordinated Mini Bots - Success in Localization, Mapping, and Communication!**
- **Localization and Mapping**: Tackled real-time localization and mapping using AR and OpenCV, enabling accurate environmental understanding.
- **Communication Infrastructure**: Implemented HTTP POST protocol over Wi-Fi for seamless communication and coordinated actions.
- **Hardware Challenges Addressed**: Overcame hardware hurdles through persistent troubleshooting and innovative solutions.

🚀 **Project Presentation**:
The project culminated in a successful presentation showcasing the capabilities of our coordinated mini-bots, the effectiveness of our AR/OpenCV-based approach, robust communication protocols, and solutions to hardware challenges.

## Overview
In the fluctuating world of warehouse automation, the collaboration of miniature robots coordinated by a robotic system is revolutionary for material handling operations. Drawing inspiration from social insects' teamwork, these small robots offer unique solutions and enhanced effectiveness.

## 1.1 Purpose
A coordinated robot system combines the intelligence and abilities of small independent swarm mini-bots to perform difficult, time-consuming, or dangerous work. This report examines how collective actions among several robots improve the handling process, making it more efficient, adaptable, and sustainable.

## 1.2 Industrial Focus: Palletizing and Depalletizing
Within warehousing operations, two central aspects where coordinated robotic systems focus include pallet loading and unloading.

- **Palletizing**: Arranging products on pallets for easy storage and movement.
- **Depalletizing**: Miniature robots work together to remove products from pallets, involving identification, gripping, and relocation of items within the warehouse.

## Coordinated Micro-Bots Approach Advantages
- **Efficiency**: Combined operation of several bots speeds up task performance compared to a single robot.
- **Adaptability**: Designed for flexible handling environments, adaptable to different conditions.
- **Robustness**: A swarm's resilience and adaptability ensure operational goals are met even if individual robots fail.

## 1.4 Smart Collaboration with ESP8266 and OpenCV
ESP8266 and OpenCV enhance the capabilities of swarming mini-bots. The ESP8266 facilitates seamless wireless communication, while OpenCV provides swarm vision for obstacle detection and collision avoidance, improving pallet handling tasks.

## 3. Problem Statement
Optimizing coordination and task allocation for multiple mini-bots poses significant challenges, hindering efficiency in seamless operations.

## 3.1 Objectives
- To design and develop mini-bots.
- To establish communication between mini-bots.
- To improve localization and mapping of mini-bots.

## 4. Methodology
### Bot Design and Development
The mini-bot design involves creating a PCB that connects different subsystems. Each mini-bot includes an Aruco marker for localization, an electromagnet for controlling pallets, a battery for power, and two rotary servos for movement. 

### Communication Establishment
The system uses HTTP POST instructions to send data between tiny bots and the main computer. Mini-bots use the NodeMCU 8266 Wi-Fi module for connection and OpenCV to examine visual data from cameras, enhancing spatial awareness and task coordination.

### Mini Bots Mobility
When the system starts, it performs an inventory assessment and assigns tasks to each mini-bot based on real-time data. Mini-bots independently calculate optimal routes and follow precise instructions for navigating, picking up, and dropping pallets. An emergency stop option ensures safety, and the main computer monitors the system's performance.

## 5. Tools and Techniques
### 5.1 Communication Architecture
The system relies on a central computer using OpenCV for processing and communication. Directions are communicated via HTTP POST requests facilitated by ESP8266 modules, ensuring smooth operation and data transfer.

### 5.2 Localization
Aruco marks and high-resolution network cameras (ZEBRONICS Sharp PRO) are used for accurate positioning and navigation.

### 5.3 Robot Control & Power Management
ESP8266 modules handle real-time communication and coordination. Power management involves switching converters, voltage regulators, and Samsung 30Q 18650 batteries for efficient operation.

### 5.4 Path Planning
Using OpenCV and computer vision algorithms, the system ensures accurate detection and tracking of markers, optimizing navigation and task completion.

---

**Note**: This is my 3rd-year 6th-semester project-based learning project given by our college to create innovative solutions based on what we have studied throughout the BTech program.
