#include <WiFi.h>
#include <ESP32Servo.h>

Servo myServo;
void setup() {
myServo.attach(23);
}

void loop() {
  myServo.write(180);
  delay(500);
  myServo.write(0);
  delay(500);
}