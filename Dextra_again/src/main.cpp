// #include <Arduino.h>
// #include <ESP32Servo.h>
// #include <ArduinoJson.h>
// #include <WiFi.h>
// #include <string.h>

// Servo baseServo;
// Servo topServo;

// const int basePin = 15;
// const int topPin = 23;
// const char* ssid = "Ram4g";
// const char* password = "vibhu123";
// const char* host = "192.168.29.224";
// const uint16_t port = 2023;
// int topDetached = 0;
// int bottomDetached = 0;
// int msgNum = 0;
// int OTA_Mode = 0; // 0 - offline, use indices. 1- Online, read and implement
// const int MaxPathSize = 2000;
// int topAngle = 0;
// int bottomAngle = 0;
// int baseDetach = 0;
// int topDetach = 0;
// int iter_var = 0;
// int total = 0;
// int execute = 0;
// int TopServo[MaxPathSize];
// int BaseServo[MaxPathSize];
// int TopDetach[MaxPathSize];
// int BottomDetach[MaxPathSize];
// WiFiClient client;

// void Json(const String& msg) {
//   JsonDocument docket;
//   DeserializationError error = deserializeJson(docket, msg);
//   if (error) {
//     Serial.print("deserializeJson() failed: ");
//     Serial.println(error.c_str());
//     return;
//   }

//   topAngle = docket["topServoAngle"];
//   bottomAngle = docket["bottomServoAngle"];
//   baseDetach = docket["detachBase"];
//   topDetach = docket["detachTop"];
//   iter_var = docket["iter"].as<int>();
//   total = docket["total"].as<int>();

// }

// void angleProcessor(int topDetach, int &topDetached, int baseDetach, int &bottomDetached, Servo &topServo, Servo &baseServo, int topAngle, int bottomAngle){
//   if (!topDetach) {
//           if (topDetached){topServo.attach(topPin);}
//           topDetached = 0;    
//           topServo.write(topAngle);
//           }
//           else {
//             topServo.detach();
//             topDetached = 1;
//           }
//           if (!baseDetach){
//           if (bottomDetached) {baseServo.attach(basePin);}
//           bottomDetached = 0;
//           baseServo.write(bottomAngle);
//           }
//           else {
//             baseServo.detach();
//             bottomDetached = 1;
//           }
// }

// void setup() {
//   Serial.begin(115200);
//   baseServo.attach(basePin);
//   topServo.attach(topPin);
  
//   Serial.println("Connecting to WiFi...");
//   WiFi.begin(ssid, password);

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println("\nConnected to WiFi.");
//   Serial.println(WiFi.localIP());

//   Serial.print("Connecting to server at ");
//   Serial.print(host); Serial.print(":"); Serial.println(port);
  
//   if (client.connect(host, port)) {
//     Serial.println("Connected to server.");
//   } else {
//     Serial.println("Connection to server failed.");
//   }
// }

// void loop() {
//     while (client.available()) {
//       String msg = client.readStringUntil('\n');
//       Serial.println(msg.c_str());
//       if (msg.length() == 0) {
//         continue;
//       }
//       switch (msgNum)
//       {
//       case 0:
//         if(atoi(msg.c_str())) {
//           OTA_Mode =1;
//           Serial.println("Recognized OTA Mode");
//         }
//         else {
//           OTA_Mode = 0;
//         }
//         msgNum++;
//         break;
//       default:
//       msgNum++;
//         Json(msg);
//         if (OTA_Mode==1){
//           angleProcessor(topDetach, topDetached, baseDetach, bottomDetached, topServo, baseServo, topAngle, bottomAngle);
//         }
//         else {
//           if(iter_var <= total) {
//           TopServo[iter_var] = topAngle;
//           BaseServo[iter_var] = bottomAngle;
//           BottomDetach[iter_var] = baseDetach;
//           TopDetach[iter_var] = topDetach;
//           if(iter_var == total) {
//             execute = 1;
//           }
//           else {
//             execute = 0;
//           }
//           }
//           if(execute) {
//             Serial.println("Executing for loop");
//             for (int i =0; i<=total; i++){
//               angleProcessor(TopDetach[i], topDetached, BottomDetach[i], bottomDetached, topServo, baseServo, TopServo[i], BaseServo[i]);
//               delay(25);
//             }
//           }
//         }
//         break;
//       }
//   }
//   if (!client.connected()) {
//     client.connect(host,port);
//     Serial.println("Attempting to connect");
//     msgNum = 0;
//     delay(1000);
//   }
//   delay(50);

  
// }

#include <Arduino.h>

int STEP = 2;
int FAULT = 4;

void setup() {
  pinMode(STEP, OUTPUT);
  pinMode(FAULT, INPUT);
  // digitalWrite(FAULT, LOW);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(STEP, HIGH);
  Serial.println(digitalRead(FAULT));
  delayMicroseconds(100);
  digitalWrite(STEP, LOW);
  delay(100); // 10ms between steps
  Serial.println(digitalRead(FAULT));
}

