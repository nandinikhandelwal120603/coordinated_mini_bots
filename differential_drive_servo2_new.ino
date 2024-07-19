

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

const char* ssid = "RATurtle";
const char* password = "RNA12345";
//const char* ssid = "Hittleboy";
//const char* password = "6tau3u4n";



ESP8266WebServer server(80);
Servo leftServo;  // create servo object to control left servo
Servo rightServo;  // create servo object to control right servo

void setup() {
  Serial.begin(115200);
  leftServo.attach(13);  // attaches left servo on GPIO5 to the servo object
  rightServo.attach(15);  // attaches right servo on GPIO4 to the servo object

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
    moveDiagonalBackwardLeft();
    server.send(200, "text/plain", "Moving backward left");
  } else if (command == "backright") {
    moveDiagonalBackwardRight();
    server.send(200, "text/plain", "Moving backward right");
  } else if (command == "forwardleft") {
    moveDiagonalForwardLeft();
    server.send(200, "text/plain", "Moving forward left");
  } else if (command == "forwardright") {
    moveDiagonalForwardRight();
    server.send(200, "text/plain", "Moving forward right");
  } else if (command == "nomove") {
    stopMotors();
    server.send(200, "text/plain", "Stopping");
  }
}

void moveForward() {
  leftServo.writeMicroseconds(1500);
  rightServo.writeMicroseconds(1500);
  delay(50);
}

void moveBackward() {
  leftServo.writeMicroseconds(1300);
  rightServo.writeMicroseconds(1300);
  delay(50); // Delay to ensure movement is executed
//  leftServo.writeMicroseconds(1300);
//  rightServo.writeMicroseconds(1700);
//  delay(50); // Delay to ensure movement is executed
//}
}

void turnLeft() {
  leftServo.writeMicroseconds(1300);
  rightServo.writeMicroseconds(1700);
  delay(50); // Delay to ensure movement is executed
}

void turnRight() {
  leftServo.writeMicroseconds(1700);
  rightServo.writeMicroseconds(1300);
  delay(50); // Delay to ensure movement is executed
}

void moveDiagonalForwardLeft() {
  leftServo.writeMicroseconds(1700);
  rightServo.writeMicroseconds(1500);
  delay(50); // Delay to ensure movement is executed
}

void moveDiagonalForwardRight() {
  leftServo.writeMicroseconds(1500);
  rightServo.writeMicroseconds(1300);
  delay(50); // Delay to ensure movement is executed
}

void moveDiagonalBackwardLeft() {
  leftServo.writeMicroseconds(1500);
  rightServo.writeMicroseconds(1700);
  delay(50); // Delay to ensure movement is executed
}

void moveDiagonalBackwardRight() {
  leftServo.writeMicroseconds(1300);
  rightServo.writeMicroseconds(1500);
  delay(50); // Delay to ensure movement is executed
}

void stopMotors() {
  leftServo.writeMicroseconds(1500);
  rightServo.writeMicroseconds(1500);
  delay(50); // Delay to ensure movement is executed
}
