// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves the AyeAM control interface's endpoint, GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, and answers OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#అన్తర్భావ <WiFi.h>
#అన్తర్భావ <WebServer.h>

స్థిరరాశి అక్షరం *జాలం_name = "your-network";
స్థిరరాశి అక్షరం *జాలం_password = "your-password";
స్థిరరాశి పూర్ణాంకం IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

శూన్య wheels(పూర్ణాంకం ఎడమవైపు_forward, పూర్ణాంకం ఎడమవైపు_backward, పూర్ణాంకం కుడివైపు_forward, పూర్ణాంకం కుడివైపు_backward, పూర్ణాంకం వేగం) {
  digitalWrite(IN1, ఎడమవైపు_forward); digitalWrite(IN2, ఎడమవైపు_backward);
  digitalWrite(IN3, కుడివైపు_forward); digitalWrite(IN4, కుడివైపు_backward);
  analogWrite(ENA, వేగం); analogWrite(ENB, వేగం);
}

శూన్య drive(అక్షరం direction, పూర్ణాంకం వేగం) {
  ఒకవేళ (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, వేగం);
  లేకపోతే ఒకవేళ (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, వేగం);
  లేకపోతే ఒకవేళ (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, వేగం);
  లేకపోతే ఒకవేళ (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, వేగం);
  లేకపోతే wheels(LOW, LOW, LOW, LOW, 0);
}

శూన్య command() {
  String దత్తాంశం = server.arg("data");
  పూర్ణాంకం మొదటి = దత్తాంశం.indexOf(','), రెండవ = దత్తాంశం.indexOf(',', మొదటి + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  ఒకవేళ (మొదటి < 1 || రెండవ < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); తిరిగి; }
  అక్షరం direction = దత్తాంశం.charAt(0);
  దీర్ఘ duration = దత్తాంశం.substring(మొదటి + 1, రెండవ).toInt();
  పూర్ణాంకం వేగం = constrain(దత్తాంశం.substring(రెండవ + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, వేగం);
  delay(duration);
  drive('S', 0);
}

శూన్య setup() {
  Serial.begin(115200);
  స్థిరరాశి పూర్ణాంకం pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  కొరకు (పూర్ణాంకం సూచీ = 0; సూచీ < 6; సూచీ++) pinMode(pins[సూచీ], OUTPUT);
  drive('S', 0);
  WiFi.begin(జాలం_name, జాలం_password);
  అయితే (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/cmd", command);
  server.begin();
}

శూన్య loop() { server.handleClient(); }
