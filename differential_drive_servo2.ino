#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

const char* ssid = "Airtel_anan_5586";
const char* password = "air25684";

ESP8266WebServer server(80);
Servo leftServo;  // create servo object to control left servo
Servo rightServo;  // create servo object to control right servo

void setup() {
  Serial.begin(115200);
  leftServo.attach(5);  // attaches left servo on GPIO5 to the servo object
  rightServo.attach(4);  // attaches right servo on GPIO4 to the servo object

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/control", handleControl); // Set up control endpoint
  server.begin(); // Start server
}

void loop() {
  server.handleClient(); // Handle client requests
}

// Handle control endpoint
void handleControl() {
  String command = server.arg("command");
  if (command == "forward") {
    moveForward();
    server.send(200, "text/plain", "Moving forward");
  } else if (command == "backward") {
    moveBackward();
    server.send(200, "text/plain", "Moving backward");
  } else if (command == "left") {
    turnLeft();
    server.send(200, "text/plain", "Turning left");
  } else if (command == "right") {
    turnRight();
    server.send(200, "text/plain", "Turning right");
  } else if (command == "backleft") {
    moveBackwardLeft();
    server.send(200, "text/plain", "Moving backward left");
  } else if (command == "backright") {
    moveBackwardRight();
    server.send(200, "text/plain", "Moving backward right");
  } else if (command == "forwardleft") {
    moveForwardLeft();
    server.send(200, "text/plain", "Moving forward left");
  } else if (command == "forwardright") {
    moveForwardRight();
    server.send(200, "text/plain", "Moving forward right");
  } else if (command == "nomove") {
    stopMotors();
    server.send(200, "text/plain", "Stopping");
  }
}

// Move forward
void moveForward() {
  leftServo.write(180);  // move left servo forward
  rightServo.write(0);   // move right servo forward
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after moving
}

// Move backward
void moveBackward() {
  leftServo.write(0);    // move left servo backward
  rightServo.write(180); // move right servo backward
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after moving
}

// Turn left
void turnLeft() {
  leftServo.write(0);    // move left servo backward
  rightServo.write(0);   // move right servo forward
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after turning
}

// Turn right
void turnRight() {
  leftServo.write(180);  // move left servo forward
  rightServo.write(180); // move right servo backward
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after turning
}

// Move backward left
void moveBackwardLeft() {
  leftServo.write(0);    // move left servo backward
  rightServo.write(90);  // move right servo to center for diagonal movement
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after moving
}

// Move backward right
void moveBackwardRight() {
  leftServo.write(90);   // move left servo to center for diagonal movement
  rightServo.write(180); // move right servo backward
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after moving
}

// Move forward left
void moveForwardLeft() {
  leftServo.write(90);   // move left servo to center for diagonal movement
  rightServo.write(0);   // move right servo forward
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after moving
}

// Move forward right
void moveForwardRight() {
  leftServo.write(180);  // move left servo forward
  rightServo.write(90);  // move right servo to center for diagonal movement
  delay(1000); // Adjust delay according to your needs
  stopMotors(); // Stop motors after moving
}

// Stop motors
void stopMotors() {
  leftServo.write(90);   // stop left servo
  rightServo.write(90);  // stop right servo
}
