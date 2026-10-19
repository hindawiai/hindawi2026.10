// Stage 3 robot (ages 16 and up): ESP32 with an L298N driver, controlled over WiFi from anywhere the network reaches.
// It serves its own control page at / for a phone, and the AyeAM control interface's endpoint,
// GET /cmd?data=<dir>,<duration>,<pwm>&seq=<n>, answering OK.
// Wiring: IN1 and IN2 to the left motor, IN3 and IN4 to the right motor, ENA and ENB to the speed (PWM) inputs; the L298N
// on its own battery, its ground joined to the ESP32's ground. Put your network's name and password below.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#ਅਨ੍ਤਰ੍ਭਾਵ <WiFi.h>
#ਅਨ੍ਤਰ੍ਭਾਵ <WebServer.h>

ਅਚਲ ਅੱਖਰ *ਜਾਲ_name = "your-network";
ਅਚਲ ਅੱਖਰ *ਜਾਲ_password = "your-password";
ਅਚਲ ਪੂਰਨ IN1 = 26, IN2 = 27, IN3 = 14, IN4 = 12, ENA = 25, ENB = 33;

WebServer server(80);

// The robot's own control page, for a phone on the same WiFi: open the address the Serial Monitor prints.
ਅਚਲ ਅੱਖਰ *PAGE =
  "<!doctype html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><title>Robot</title>"
  "<style>body{font:20px sans-serif;text-align:center;margin:12px}button{width:30%;height:70px;font-size:28px;margin:4px}"
  "input{width:80%}</style></head><body><h3>Robot</h3>"
  "<div><button onclick=\"go('F')\">&#8593;</button></div>"
  "<div><button onclick=\"go('L')\">&#8592;</button><button onclick=\"go('S')\">&#9632;</button>"
  "<button onclick=\"go('R')\">&#8594;</button></div><div><button onclick=\"go('B')\">&#8595;</button></div>"
  "<p>speed <input id='p' type='range' min='80' max='255' value='200'></p>"
  "<p>time (ms) <input id='t' type='range' min='100' max='3000' value='800'></p><p id='o'>ready</p>"
  "<script>let n=0;function go(d){fetch('/cmd?data='+d+','+t.value+','+p.value+'&seq='+(n++))"
  ".then(r=>r.text()).then(x=>o.textContent=d+': '+x).catch(e=>o.textContent='no answer: '+e)}</script>"
  "</body></html>";

ਖਾਲੀ ਪੰਨਾ() { server.send(200, "text/html", PAGE); }

ਖਾਲੀ wheels(ਪੂਰਨ ਖੱਬਾ_forward, ਪੂਰਨ ਖੱਬਾ_backward, ਪੂਰਨ ਸੱਜਾ_forward, ਪੂਰਨ ਸੱਜਾ_backward, ਪੂਰਨ ਰਫਤਾਰ) {
  digitalWrite(IN1, ਖੱਬਾ_forward); digitalWrite(IN2, ਖੱਬਾ_backward);
  digitalWrite(IN3, ਸੱਜਾ_forward); digitalWrite(IN4, ਸੱਜਾ_backward);
  analogWrite(ENA, ਰਫਤਾਰ); analogWrite(ENB, ਰਫਤਾਰ);
}

ਖਾਲੀ drive(ਅੱਖਰ direction, ਪੂਰਨ ਰਫਤਾਰ) {
  ਜੇ (direction == 'F') wheels(HIGH, LOW, HIGH, LOW, ਰਫਤਾਰ);
  ਨਹੀਂਤਾਂ ਜੇ (direction == 'B') wheels(LOW, HIGH, LOW, HIGH, ਰਫਤਾਰ);
  ਨਹੀਂਤਾਂ ਜੇ (direction == 'L') wheels(LOW, HIGH, HIGH, LOW, ਰਫਤਾਰ);
  ਨਹੀਂਤਾਂ ਜੇ (direction == 'R') wheels(HIGH, LOW, LOW, HIGH, ਰਫਤਾਰ);
  ਨਹੀਂਤਾਂ wheels(LOW, LOW, LOW, LOW, 0);
}

ਖਾਲੀ command() {
  String ਅੰਕੜੇ = server.arg("data");
  ਪੂਰਨ ਪਹਿਲਾ = ਅੰਕੜੇ.indexOf(','), ਦੂਜਾ = ਅੰਕੜੇ.indexOf(',', ਪਹਿਲਾ + 1);
  server.sendHeader("Access-Control-Allow-Origin", "*");
  ਜੇ (ਪਹਿਲਾ < 1 || ਦੂਜਾ < 0) { server.send(400, "text/plain", "ERR expected dir,duration,pwm"); ਵਾਪਸ; }
  ਅੱਖਰ direction = ਅੰਕੜੇ.charAt(0);
  ਲੰਮਾ duration = ਅੰਕੜੇ.substring(ਪਹਿਲਾ + 1, ਦੂਜਾ).toInt();
  ਪੂਰਨ ਰਫਤਾਰ = constrain(ਅੰਕੜੇ.substring(ਦੂਜਾ + 1).toInt(), 0, 255);
  server.send(200, "text/plain", "OK");
  drive(direction, ਰਫਤਾਰ);
  delay(duration);
  drive('S', 0);
}

ਖਾਲੀ setup() {
  Serial.begin(115200);
  ਅਚਲ ਪੂਰਨ pins[] = {IN1, IN2, IN3, IN4, ENA, ENB};
  ਲਈ (ਪੂਰਨ ਸੂਚਕਾਂਕ = 0; ਸੂਚਕਾਂਕ < 6; ਸੂਚਕਾਂਕ++) pinMode(pins[ਸੂਚਕਾਂਕ], OUTPUT);
  drive('S', 0);
  WiFi.begin(ਜਾਲ_name, ਜਾਲ_password);
  ਜਦੋਂ (WiFi.status() != WL_CONNECTED) delay(250);
  Serial.print("robot at http://");
  Serial.println(WiFi.localIP());
  server.on("/", ਪੰਨਾ);
  server.on("/cmd", command);
  server.begin();
}

ਖਾਲੀ loop() { server.handleClient(); }
