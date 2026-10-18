// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves the AyeAM control interface's endpoint, GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, and answers OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#include <WiFi.h>
#include <WebServer.h>

const char *network_name = "your-network";
const char *network_password = "your-password";
const int IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

void wheels(int left_forward, int left_backward, int right_forward, int right_backward, int speed) {
  digitalWrite(IN1, left_forward); digitalWrite(IN2, left_backward);
  digitalWrite(IN3, right_forward); digitalWrite(IN4, right_backward);
  analogWrite(ENA, speed); analogWrite(ENB, speed);
}

void drive(char direction, int speed) {
  if (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, speed);
  else if (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, speed);
  else if (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, speed);
  else if (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, speed);
  else wheels(LOW, LOW, LOW, LOW, 0);
}

void command() {
  String data = server.arg("data");
  int first = data.indexOf(','), second = data.indexOf(',', first + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  if (first < 1 || second < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); return; }
  char direction = data.charAt(0);
  long duration = data.substring(first + 1, second).toInt();
  int speed = constrain(data.substring(second + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, speed);
  delay(duration);
  drive('S', 0);
}

void setup() {
  Serial.begin(115200);
  const int pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  for (int index = 0; index < 6; index++) pinMode(pins[index], OUTPUT);
  drive('S', 0);
  WiFi.begin(network_name, network_password);
  while (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/cmd", command);
  server.begin();
}

void loop() { server.handleClient(); }
