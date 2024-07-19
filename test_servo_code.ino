#include <Servo.h>

Servo myservo1;
Servo myservo2; // create servo objects to control the servos

void setup() {
  myservo1.attach(4);
  myservo2.attach(5); // attaches the servos to the servo objects
  
  // Move both servos to home position
  myservo1.write(0);
  myservo2.write(0);
  delay(1000); // Give some time for the servos to reach the home position
}

void loop() {
  // Move the robot forward
  for (int pos = 0; pos <= 90; pos += 1) {
    myservo1.write(45 - pos); // rotate servo1 forward
    myservo2.write(90 - pos); // rotate servo2 backward
    delay(15);
  }

  delay(1000); // delay for stability

  // Move the robot backward
  for (int pos = 90; pos >= 0; pos -= 1) {
    myservo1.write(pos); // rotate servo1 backward
    myservo2.write(90 - pos); // rotate servo2 forward
    delay(15);
  }

  delay(1000); // delay for stability
}
