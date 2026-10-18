// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves the AyeAM control interface's endpoint, GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, and answers OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#அந்தர்பாவ <WiFi.h>
#அந்தர்பாவ <WebServer.h>

மாறிலி எழுத்து *network_name = "your-network";
மாறிலி எழுத்து *network_password = "your-password";
மாறிலி முழு IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

வெறுமை wheels(முழு left_forward, முழு left_backward, முழு right_forward, முழு right_backward, முழு speed) {
  digitalWrite(IN1, left_forward); digitalWrite(IN2, left_backward);
  digitalWrite(IN3, right_forward); digitalWrite(IN4, right_backward);
  analogWrite(ENA, speed); analogWrite(ENB, speed);
}

வெறுமை drive(எழுத்து direction, முழு speed) {
  எனில் (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, speed);
  இல்லையெனில் எனில் (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, speed);
  இல்லையெனில் எனில் (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, speed);
  இல்லையெனில் எனில் (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, speed);
  இல்லையெனில் wheels(LOW, LOW, LOW, LOW, 0);
}

வெறுமை command() {
  String data = server.arg("data");
  முழு first = data.indexOf(','), second = data.indexOf(',', first + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  எனில் (first < 1 || second < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); திரும்பு; }
  எழுத்து direction = data.charAt(0);
  long duration = data.substring(first + 1, second).toInt();
  முழு speed = constrain(data.substring(second + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, speed);
  delay(duration);
  drive('S', 0);
}

வெறுமை setup() {
  Serial.begin(115200);
  மாறிலி முழு pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  க்கு (முழு index = 0; index < 6; index++) pinMode(pins[index], OUTPUT);
  drive('S', 0);
  WiFi.begin(network_name, network_password);
  போது (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/cmd", command);
  server.begin();
}

வெறுமை loop() { server.handleClient(); }
