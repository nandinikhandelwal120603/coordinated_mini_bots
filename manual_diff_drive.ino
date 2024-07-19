//#include <Servo.h>
//
//#define LEFT_SERVO_PIN 13 // Define the pin for left servo
//#define RIGHT_SERVO_PIN 15 // Define the pin for right servo
//
//Servo leftServo; // Create servo object for left servo
//Servo rightServo; // Create servo object for right servo
//
//void setup() {
//  Serial.begin(115200); // Initialize serial communication with baud rate 115200
//  leftServo.attach(LEFT_SERVO_PIN); // Attach left servo to pin
//  rightServo.attach(RIGHT_SERVO_PIN); // Attach right servo to pin
//  Serial.println("Ready to receive commands.");
//}
//
//void loop() {
//  if (Serial.available() > 0) {
//    String command = Serial.readStringUntil('\n'); // Read the incoming command
//    command.trim(); // Remove leading/trailing whitespace
//
//    // Debugging output
//    Serial.print("Received command: ");
//    Serial.println(command);
//
//    // Move the robot based on the received command
//    if (command == "F")
//      moveForward();
//    else if (command == "B")
//      moveBackward();
//    else if (command == "L")
//      turnLeft();
//    else if (command == "R")
//      turnRight();
//    else if (command == "FL")
//      moveDiagonalForwardLeft();
//    else if (command == "FR")
//      moveDiagonalForwardRight();
//    else if (command == "BL")
//      moveDiagonalBackwardLeft();
//    else if (command == "BR")
//      moveDiagonalBackwardRight();
//    else if (command == "Q")
//      stopMotors();
//    else
//      Serial.println("Invalid command.");
//  }
//}
//
//void moveForward() {
//  leftServo.writeMicroseconds(1500);
//  rightServo.writeMicroseconds(1500);
//}
//
//void moveBackward() {
//  leftServo.writeMicroseconds(1500);
//  rightServo.writeMicroseconds(1500);
//  delay(100); // Add a delay to ensure both motors start moving backward
//  leftServo.writeMicroseconds(1300);
//  rightServo.writeMicroseconds(1700);
//}
//
//void turnLeft() {
//  leftServo.writeMicroseconds(1300);
//  rightServo.writeMicroseconds(1700);
//}
//
//void turnRight() {
//  leftServo.writeMicroseconds(1700);
//  rightServo.writeMicroseconds(1300);
//}
//
//void moveDiagonalForwardLeft() {
//  leftServo.writeMicroseconds(1300);
//  rightServo.writeMicroseconds(1500);
//}
//
//void moveDiagonalForwardRight() {
//  leftServo.writeMicroseconds(1500);
//  rightServo.writeMicroseconds(1700);
//}
//
//void moveDiagonalBackwardLeft() {
//  leftServo.writeMicroseconds(1500);
//  rightServo.writeMicroseconds(1300);
//}
//
//void moveDiagonalBackwardRight() {
//  leftServo.writeMicroseconds(1700);
//  rightServo.writeMicroseconds(1500);
//}
//
//void stopMotors() {
//  leftServo.writeMicroseconds(1500);
//  rightServo.writeMicroseconds(1500);
//}



#include <Servo.h>

#define LEFT_SERVO_PIN 13 // Define the pin for left servo
#define RIGHT_SERVO_PIN 15 // Define the pin for right servo

Servo leftServo; // Create servo object for left servo
Servo rightServo; // Create servo object for right servo

void setup() {
  Serial.begin(115200); // Initialize serial communication with baud rate 115200
  leftServo.attach(LEFT_SERVO_PIN); // Attach left servo to pin
  rightServo.attach(RIGHT_SERVO_PIN); // Attach right servo to pin
  Serial.println("Ready to receive commands.");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the incoming command
    command.trim(); // Remove leading/trailing whitespace

    // Debugging output
    Serial.print("Received command: ");
    Serial.println(command);

    // Move the robot based on the received command
    if (command == "F")
      moveForward();
    else if (command == "B")
      moveBackward();
    else if (command == "L")
      turnLeft();
    else if (command == "R")
      turnRight();
    else if (command == "Q")
      stopMotors();
    else
      Serial.println("Invalid command.");
  }
}

void moveForward() {
  leftServo.write(90); // Set speed for forward motion
  rightServo.write(90); // Set speed for forward motion
}

void moveBackward() {
  leftServo.write(90); // Set speed for backward motion
  rightServo.write(90); // Set speed for backward motion
  delay(100); // Add a delay to ensure both motors start moving backward
  leftServo.write(0); // Set speed for backward motion
  rightServo.write(180); // Set speed for backward motion
}

void turnLeft() {
  leftServo.write(0); // Set speed for left turn
  rightServo.write(180); // Set speed for left turn
}

void turnRight() {
  leftServo.write(180); // Set speed for right turn
  rightServo.write(0); // Set speed for right turn
}

void stopMotors() {
  leftServo.write(90); // Stop left motor
  rightServo.write(90); // Stop right motor
}
