// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#ਅਨ੍ਤਰ੍ਭਾਵ <AFMotor.h>

AF_DCMotor ਖੱਬਾ_motor(1);
AF_DCMotor ਸੱਜਾ_motor(2);

ਖਾਲੀ drive(ਅੱਖਰ direction, ਪੂਰਨ ਰਫਤਾਰ) {
  ਖੱਬਾ_motor.setSpeed(ਰਫਤਾਰ);
  ਸੱਜਾ_motor.setSpeed(ਰਫਤਾਰ);
  ਜੇ (direction == 'F') { ਖੱਬਾ_motor.run(FORWARD); ਸੱਜਾ_motor.run(FORWARD); }
  ਨਹੀਂਤਾਂ ਜੇ (direction == 'B') { ਖੱਬਾ_motor.run(BACKWARD); ਸੱਜਾ_motor.run(BACKWARD); }
  ਨਹੀਂਤਾਂ ਜੇ (direction == 'L') { ਖੱਬਾ_motor.run(BACKWARD); ਸੱਜਾ_motor.run(FORWARD); }
  ਨਹੀਂਤਾਂ ਜੇ (direction == 'R') { ਖੱਬਾ_motor.run(FORWARD); ਸੱਜਾ_motor.run(BACKWARD); }
  ਨਹੀਂਤਾਂ { ਖੱਬਾ_motor.run(RELEASE); ਸੱਜਾ_motor.run(RELEASE); }
}

ਖਾਲੀ setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

ਖਾਲੀ loop() {
  ਜੇ (!Serial.available()) ਵਾਪਸ;
  String ਸਤਰ = Serial.readStringUntil('\n');
  ਪੂਰਨ ਪਹਿਲਾ = ਸਤਰ.indexOf(','), ਦੂਜਾ = ਸਤਰ.indexOf(',', ਪਹਿਲਾ + 1);
  ਜੇ (ਪਹਿਲਾ < 1 || ਦੂਜਾ < 0) { Serial.println("ERR expected dir,duration,pwm"); ਵਾਪਸ; }
  ਅੱਖਰ direction = ਸਤਰ.charAt(0);
  ਲੰਮਾ duration = ਸਤਰ.substring(ਪਹਿਲਾ + 1, ਦੂਜਾ).toInt();
  ਪੂਰਨ ਰਫਤਾਰ = constrain(ਸਤਰ.substring(ਦੂਜਾ + 1).toInt(), 0, 255);
  ਜੇ (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    ਵਾਪਸ;
  }
  drive(direction, ਰਫਤਾਰ);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
