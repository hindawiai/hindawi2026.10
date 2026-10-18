// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#அந்தர்பாவ <AFMotor.h>

AF_DCMotor left_motor(1);
AF_DCMotor right_motor(2);

வெறுமை drive(எழுத்து direction, முழு speed) {
  left_motor.setSpeed(speed);
  right_motor.setSpeed(speed);
  எனில் (direction == 'F') { left_motor.run(FORWARD); right_motor.run(FORWARD); }
  இல்லையெனில் எனில் (direction == 'B') { left_motor.run(BACKWARD); right_motor.run(BACKWARD); }
  இல்லையெனில் எனில் (direction == 'L') { left_motor.run(BACKWARD); right_motor.run(FORWARD); }
  இல்லையெனில் எனில் (direction == 'R') { left_motor.run(FORWARD); right_motor.run(BACKWARD); }
  இல்லையெனில் { left_motor.run(RELEASE); right_motor.run(RELEASE); }
}

வெறுமை setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

வெறுமை loop() {
  எனில் (!Serial.available()) திரும்பு;
  String line = Serial.readStringUntil('\n');
  முழு first = line.indexOf(','), second = line.indexOf(',', first + 1);
  எனில் (first < 1 || second < 0) { Serial.println("ERR expected dir,duration,pwm"); திரும்பு; }
  எழுத்து direction = line.charAt(0);
  long duration = line.substring(first + 1, second).toInt();
  முழு speed = constrain(line.substring(second + 1).toInt(), 0, 255);
  எனில் (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    திரும்பு;
  }
  drive(direction, speed);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
