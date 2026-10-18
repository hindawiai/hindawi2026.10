// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves the AyeAM control interface's endpoint, GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, and answers OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#ಅನ್ತರ್ಭಾವ <WiFi.h>
#ಅನ್ತರ್ಭಾವ <WebServer.h>

ಸ್ಥಿರಾಂಕ ಅಕ್ಷರ *ಜಾಲ_name = "your-network";
ಸ್ಥಿರಾಂಕ ಅಕ್ಷರ *ಜಾಲ_password = "your-password";
ಸ್ಥಿರಾಂಕ ಪೂರ್ಣಾಂಕ IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

ಶೂನ್ಯ wheels(ಪೂರ್ಣಾಂಕ ಎಡಭಾಗ_forward, ಪೂರ್ಣಾಂಕ ಎಡಭಾಗ_backward, ಪೂರ್ಣಾಂಕ ಬಲಭಾಗ_forward, ಪೂರ್ಣಾಂಕ ಬಲಭಾಗ_backward, ಪೂರ್ಣಾಂಕ ವೇಗ) {
  digitalWrite(IN1, ಎಡಭಾಗ_forward); digitalWrite(IN2, ಎಡಭಾಗ_backward);
  digitalWrite(IN3, ಬಲಭಾಗ_forward); digitalWrite(IN4, ಬಲಭಾಗ_backward);
  analogWrite(ENA, ವೇಗ); analogWrite(ENB, ವೇಗ);
}

ಶೂನ್ಯ drive(ಅಕ್ಷರ direction, ಪೂರ್ಣಾಂಕ ವೇಗ) {
  ಆದರೆ (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, ವೇಗ);
  ಇಲ್ಲದಿದ್ದರೆ ಆದರೆ (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, ವೇಗ);
  ಇಲ್ಲದಿದ್ದರೆ ಆದರೆ (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, ವೇಗ);
  ಇಲ್ಲದಿದ್ದರೆ ಆದರೆ (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, ವೇಗ);
  ಇಲ್ಲದಿದ್ದರೆ wheels(LOW, LOW, LOW, LOW, 0);
}

ಶೂನ್ಯ command() {
  String ದತ್ತಾಂಶ = server.arg("data");
  ಪೂರ್ಣಾಂಕ ಮೊದಲ = ದತ್ತಾಂಶ.indexOf(','), ಎರಡನೇ = ದತ್ತಾಂಶ.indexOf(',', ಮೊದಲ + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  ಆದರೆ (ಮೊದಲ < 1 || ಎರಡನೇ < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); ಹಿಂತಿರುಗಿ; }
  ಅಕ್ಷರ direction = ದತ್ತಾಂಶ.charAt(0);
  ದೀರ್ಘ duration = ದತ್ತಾಂಶ.substring(ಮೊದಲ + 1, ಎರಡನೇ).toInt();
  ಪೂರ್ಣಾಂಕ ವೇಗ = constrain(ದತ್ತಾಂಶ.substring(ಎರಡನೇ + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, ವೇಗ);
  delay(duration);
  drive('S', 0);
}

ಶೂನ್ಯ setup() {
  Serial.begin(115200);
  ಸ್ಥಿರಾಂಕ ಪೂರ್ಣಾಂಕ pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  ಗಾಗಿ (ಪೂರ್ಣಾಂಕ ಸೂಚ್ಯಂಕ = 0; ಸೂಚ್ಯಂಕ < 6; ಸೂಚ್ಯಂಕ++) pinMode(pins[ಸೂಚ್ಯಂಕ], OUTPUT);
  drive('S', 0);
  WiFi.begin(ಜಾಲ_name, ಜಾಲ_password);
  ಆಗ (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/cmd", command);
  server.begin();
}

ಶೂನ್ಯ loop() { server.handleClient(); }
