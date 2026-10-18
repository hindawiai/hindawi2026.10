// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves the AyeAM control interface's endpoint, GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, and answers OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#समावेश <WiFi.h>
#समावेश <WebServer.h>

स्थिर अक्षर *network_name = "your-network";
स्थिर अक्षर *network_password = "your-password";
स्थिर पूर्णांक IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

व्योम wheels(पूर्णांक वाम_forward, पूर्णांक वाम_backward, पूर्णांक दक्षिण_forward, पूर्णांक दक्षिण_backward, पूर्णांक speed) {
  digitalWrite(IN1, वाम_forward); digitalWrite(IN2, वाम_backward);
  digitalWrite(IN3, दक्षिण_forward); digitalWrite(IN4, दक्षिण_backward);
  analogWrite(ENA, speed); analogWrite(ENB, speed);
}

व्योम drive(अक्षर direction, पूर्णांक speed) {
  अगर (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, speed);
  अन्यथा अगर (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, speed);
  अन्यथा अगर (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, speed);
  अन्यथा अगर (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, speed);
  अन्यथा wheels(LOW, LOW, LOW, LOW, 0);
}

व्योम command() {
  String तथ्य = server.arg("data");
  पूर्णांक first = तथ्य.indexOf(','), second = तथ्य.indexOf(',', first + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  अगर (first < 1 || second < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); वापस; }
  अक्षर direction = तथ्य.charAt(0);
  दीर्घ duration = तथ्य.substring(first + 1, second).toInt();
  पूर्णांक speed = constrain(तथ्य.substring(second + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, speed);
  delay(duration);
  drive('S', 0);
}

व्योम setup() {
  Serial.begin(115200);
  स्थिर पूर्णांक pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  क्रम (पूर्णांक सूचकांक = 0; सूचकांक < 6; सूचकांक++) pinMode(pins[सूचकांक], OUTPUT);
  drive('S', 0);
  WiFi.begin(network_name, network_password);
  जबतक (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/cmd", command);
  server.begin();
}

व्योम loop() { server.handleClient(); }
