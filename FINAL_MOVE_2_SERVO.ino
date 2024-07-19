#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

const char* ssid = "Hittleboy";
const char* password = "6tau3u4n";

ESP8266WebServer server(80);
Servo servo1;
Servo servo2;
int pos1 = 0;
int pos2 = 0;

void setup() {
  Serial.begin(115200);
  servo1.attach(15);  // attach servo 1 to GPIO5
  servo2.attach(13);  // attach servo 2 to GPIO4

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/control", HTTP_GET, []() {
    String command = server.arg("command");
    if (command == "move") {
      // Move both servos gradually
      for (pos1 = 0, pos2 = 0; pos1 <= 180 && pos2 <= 180; pos1 += 1, pos2 += 1) {
        servo1.write(pos1);
        servo2.write(pos2);
        delay(15); // Adjust delay as needed
      }
      server.send(200, "text/plain", "OK");
    } else if (command == "nomove") {
      // Do nothing, servos stay in their current positions
      server.send(200, "text/plain", "Servos not moved");
    }
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
