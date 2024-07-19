#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_MPU6050.h>

// Motor A
int motor1Pin1 = 27; // OUT1
int motor1Pin2 = 26; // OUT2
int enable1Pin = 14;

// Motor B
int motor2Pin1 = 33; // OUT3
int motor2Pin2 = 32; // OUT4
int enable2Pin = 25;

// MPU6050
Adafruit_MPU6050 mpu;

void setup() {
  // sets the pins as outputs for motor A:
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(enable1Pin, OUTPUT);

  // sets the pins as outputs for motor B:
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  pinMode(enable2Pin, OUTPUT);

  // Start with motors stopped
  stopMotors();

  Serial.begin(115200);

  // Initialize MPU6050
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.println("MPU6050 Found!");

  // Testing
  Serial.println("Testing DC Motors...");
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.print("Acceleration X: ");
  Serial.print(a.acceleration.x);
  Serial.print(", Y: ");
  Serial.print(a.acceleration.y);
  Serial.print(", Z: ");
  Serial.print(a.acceleration.z);
  Serial.println(" m/s^2");

  Serial.print("Rotation X: ");
  Serial.print(g.gyro.x);
  Serial.print(", Y: ");
  Serial.print(g.gyro.y);
  Serial.print(", Z: ");
  Serial.print(g.gyro.z);
  Serial.println(" rad/s");

  Serial.print("Temperature: ");
  Serial.print(temp.temperature);
  Serial.println(" degC");

  delay(500); // Delay to allow time for reading

  moveForward();
  delay(2000);

  stopMotors();
  delay(1000);

  moveBackward();
  delay(2000);

  stopMotors();
  delay(1000);

  moveLeft();
  delay(2000);

  stopMotors();
  delay(1000);

  moveRight();
  delay(2000);

  stopMotors();
  delay(1000);
}

void stopMotors() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
  analogWrite(enable1Pin, 0);
  analogWrite(enable2Pin, 0);
}

void moveForward() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
  analogWrite(enable1Pin, 255);
  analogWrite(enable2Pin, 255);
  Serial.println("Moving Forward");
}

void moveBackward() {
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
  analogWrite(enable1Pin, 255);
  analogWrite(enable2Pin, 255);
  Serial.println("Moving Backward");
}

void moveLeft() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
  analogWrite(enable1Pin, 255);
  analogWrite(enable2Pin, 255);
  Serial.println("Turning Left");
}

void moveRight() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
  analogWrite(enable1Pin, 255);
  analogWrite(enable2Pin, 255);
  Serial.println("Turning Right");
}
