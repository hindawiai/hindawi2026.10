// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves the AyeAM control interface's endpoint, GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, and answers OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#شامل <WiFi.h>
#شامل <WebServer.h>

ثابت حرف *جال_name = "your-network";
ثابت حرف *جال_password = "your-password";
ثابت صحیح IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

خالی wheels(صحیح بائیں_forward, صحیح بائیں_backward, صحیح دائیں_forward, صحیح دائیں_backward, صحیح رفتار) {
  digitalWrite(IN1, بائیں_forward); digitalWrite(IN2, بائیں_backward);
  digitalWrite(IN3, دائیں_forward); digitalWrite(IN4, دائیں_backward);
  analogWrite(ENA, رفتار); analogWrite(ENB, رفتار);
}

خالی drive(حرف direction, صحیح رفتار) {
  اگر (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, رفتار);
  ورنہ اگر (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, رفتار);
  ورنہ اگر (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, رفتار);
  ورنہ اگر (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, رفتار);
  ورنہ wheels(LOW, LOW, LOW, LOW, 0);
}

خالی command() {
  String ڈیٹا = server.arg("data");
  صحیح پہلا = ڈیٹا.indexOf(','), دوسرا = ڈیٹا.indexOf(',', پہلا + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  اگر (پہلا < 1 || دوسرا < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); واپس; }
  حرف direction = ڈیٹا.charAt(0);
  طویل duration = ڈیٹا.substring(پہلا + 1, دوسرا).toInt();
  صحیح رفتار = constrain(ڈیٹا.substring(دوسرا + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, رفتار);
  delay(duration);
  drive('S', 0);
}

خالی setup() {
  Serial.begin(115200);
  ثابت صحیح pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  برائے (صحیح اشاریہ = 0; اشاریہ < 6; اشاریہ++) pinMode(pins[اشاریہ], OUTPUT);
  drive('S', 0);
  WiFi.begin(جال_name, جال_password);
  جب (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/cmd", command);
  server.begin();
}

خالی loop() { server.handleClient(); }
