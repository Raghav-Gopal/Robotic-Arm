#include <WiFi.h>
#include <ESP32Servo.h>

Servo myServo;
void setup() {
myServo.attach(23);
pinMode(22,OUTPUT_OPEN_DRAIN);
}

void loop() {
  myServo.write(180);
  digitalWrite(22,HIGH);
  delay(1000);
  digitalWrite(22,LOW);
  myServo.write(0);
  delay(1000);
}