// #include <WiFi.h>
#include <ESP32Servo.h>
#include <math.h>
int SW1 = 16; int SW2 = 17; int SW3 = 5; int SW4 = 18;
int pot = 36;
int M0 = 27; int M1 = 14; int M2 = 12;
int STEP =26; int SLEEP = 25;
int ledM0 = 15; int ledM1 =2; int ledM2 = 0;
bool lastSwVal1 = false, lastSwVal2 = false, lastSwVal3 = false, lastSwVal4 = false;
int ledOpt = 19;

unsigned long lastMillis = 0;
unsigned long currentMillis = 0;

//pot gives 0 to 4095
float potVal;
bool SwVal1, SwVal2, SwVal3, SwVal4, State1, State2, State3, State4;
int stepPosition =0;

void SWupdater() {
  if(SwVal1 && !lastSwVal1) {State1 = !State1;}
  if(SwVal2 && !lastSwVal2) {State2 = !State2;}
  if(SwVal3 && !lastSwVal3) {State3 = !State3;}
  if(SwVal4 && !lastSwVal4) {State4 = !State4;}
  lastSwVal1 = SwVal1; lastSwVal2 = SwVal2; lastSwVal3 = SwVal3; lastSwVal4 = SwVal4;
  digitalWrite(ledM0, State4);
  digitalWrite(ledM1, State3);
  digitalWrite(ledM2, State2);
  digitalWrite(ledOpt, State1);
  digitalWrite(M0, State4);
  digitalWrite(M1, State3);
  digitalWrite(M2, State2);
  digitalWrite(SLEEP, State1);
}

void setup() {
  Serial.begin(115200);
  pinMode(SW1, INPUT_PULLDOWN);
  pinMode(SW2, INPUT_PULLDOWN);
  pinMode(SW3, INPUT_PULLDOWN);
  pinMode(SW4, INPUT_PULLDOWN);
  pinMode(pot,INPUT);

  pinMode(STEP, OUTPUT);
  pinMode(SLEEP, OUTPUT);
  pinMode(ledM0, OUTPUT);
  pinMode(ledM1, OUTPUT);
  pinMode(ledM2, OUTPUT);
  pinMode(ledOpt, OUTPUT);
}
void loop() {
  potVal = analogRead(pot);
  Serial.println(potVal);

  
  int stepDelay = map(potVal, 0, 4095, 2000, 100); 

  digitalWrite(STEP, HIGH);
  delayMicroseconds(stepDelay); 
  digitalWrite(STEP, LOW);
  delayMicroseconds(stepDelay); 

  SwVal1 = digitalRead(SW1);
  SwVal2 = digitalRead(SW2);
  SwVal3 = digitalRead(SW3);
  SwVal4 = digitalRead(SW4);
  SWupdater();
}
