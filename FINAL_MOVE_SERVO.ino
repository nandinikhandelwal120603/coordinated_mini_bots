#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

//
//const char* ssid = "RAturtle2_5G";
//const char* password = "RNA12345";
const char* ssid = "Airtel_anan_5586";
const char* password = "air25684";

ESP8266WebServer server(80);
Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(115200);
  myservo.attach(8);  // attaches the servo on GPIO2 to the servo object

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.on("/control", HTTP_GET, []() {
    String command = server.arg("command");
    if (command == "move") {
      for (pos = 0; pos <= 180; pos += 1) {
        myservo.write(pos);
        delay(15);
      }
      for (pos = 180; pos >= 0; pos -= 1) {
        myservo.write(pos);
        delay(15);
      }
      server.send(200, "text/plain", "OK");
    } else if (command == "nomove") {
      // Do nothing, servo stays in its current position
      server.send(200, "text/plain", "Servo not moved");
    }
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
