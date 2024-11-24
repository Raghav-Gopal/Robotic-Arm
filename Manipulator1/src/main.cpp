#include <WiFi.h>
#include <ESP32Servo.h>

// const char* ssid = "Raghav's ESP32";   /* Set Your SSID */
// const char* password = "ghuterthigh";  /* Set Your Password */

// WiFiServer server(80); /* Instance of WiFiServer with port number 80 */
// WiFiClient client;

// IPAddress Ip(192, 168, 1, 1);
// IPAddress NMask(255, 255, 255, 0);

// String request;
// #define SERVO_PIN 23
// Servo myservo;  // Create a servo object
// int servoAngle = 0;  // Variable to store the current angle of the servo (initially 0)

// void setup() {
//   Serial.begin(115200);
//   myservo.attach(SERVO_PIN);  // Attach the servo to GPIO pin 15
//   myservo.write(servoAngle);  // Set initial angle to 0 degrees

//   Serial.println("ESP32 Access Point Mode");
//   WiFi.mode(WIFI_AP);
//   WiFi.softAP(ssid, password);  // Set your SSID and Password
//   delay(100);
//   WiFi.softAPConfig(Ip, Ip, NMask);  // Set the IP and subnet mask
//   Serial.print("Connect to IP address: ");
//   Serial.println(WiFi.softAPIP());  // Print the ESP32's IP address (192.168.1.1)
  
//   server.begin();  // Start the web server
// }

// void html() {
//   client.println("HTTP/1.1 200 OK");
//   client.println("Content-Type: text/html");
//   client.println("Connection: close");
//   client.println();

//   client.println("<!DOCTYPE HTML>");
//   client.println("<html>");
//   client.println("<head>");
//   client.println("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
//   client.println("<link rel=\"icon\" href=\"data:,\">");
//   client.println("<style>");
//   client.println("html { font-family: Arial; text-align: center;}");
//   client.println(".button {background-color: #4CAF50; border: none; color: white; padding: 15px 32px; text-align: center; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;}");
//   client.println("</style>");
//   client.println("</head>");
//   client.println("<body>");
  
//   client.println("<h2>ESP32 Servo Control</h2>");
//   client.println("<p>Control the Servo between 0 and 180 degrees</p>");
  
//   // Buttons to control the servo position
//   client.print("<p><a href=\"/SERVO_0\"><button class=\"button\">Move to 0°</button></a></p>");
//   client.print("<p><a href=\"/SERVO_90\"><button class=\"button\">Move to 90°</button></a></p>");
//   client.print("<p><a href=\"/SERVO_180\"><button class=\"button\">Move to 180°</button></a></p>");
  
//   client.println("</body>");
//   client.println("</html>");
// }

// void loop() {
//   client = server.available();  // Listen for incoming clients
  
//   if (!client) {
//     return;  // If no client is connected, just return
//   }
  
//   while (client.connected()) {
//     if (client.available()) {
//       char c = client.read();  // Read the incoming client request
//       request += c;  // Append the request character to the request string
      
//       if (c == '\n') {
//         // Process request to move servo to specific angles
//         if (request.indexOf("GET /SERVO_0") != -1) {
//           Serial.println("Moving Servo to 0°");
//           servoAngle = 0;
//           myservo.write(servoAngle);  // Move servo to 0°
//         }
//         if (request.indexOf("GET /SERVO_90") != -1) {
//           Serial.println("Moving Servo to 90°");
//           servoAngle = 90;
//           myservo.write(servoAngle);  // Move servo to 90°
//         }
//         if (request.indexOf("GET /SERVO_180") != -1) {
//           Serial.println("Moving Servo to 180°");
//           servoAngle = 180;
//           myservo.write(servoAngle);  // Move servo to 180°
//         }

//         // Send the HTML page with buttons
//         html();
//         break;
//       }
//     }
//   }

//   delay(1);
//   request = "";  // Clear the request string
//   client.stop();  // Disconnect the client
// }
// Define the pin for the potentiometer
const int potPin = 36;  // Potentiometer output connected to GPIO 23

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  
  // Setup pin mode
  pinMode(potPin, INPUT);
}

void loop() {
  // Read the analog value from the potentiometer
  int potValue = analogRead(potPin);  // Read the value from the potentiometer (0 to 4095 on ESP32)

  // Map the potentiometer value to an angle (0 to 180 degrees)
  // float angle = map(potValue, 0, 4095, 0, 180);

  // Print the angle to the Serial Monitor
  // Serial.print("Angle: ");
  Serial.println(potValue);
  
  // Small delay to avoid flooding the serial monitor
  delay(100);
}
