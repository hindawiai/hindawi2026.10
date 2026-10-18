// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#समावेश <AFMotor.h>

AF_DCMotor वाम_motor(1);
AF_DCMotor दक्षिण_motor(2);

व्योम drive(अक्षर direction, पूर्णांक speed) {
  वाम_motor.setSpeed(speed);
  दक्षिण_motor.setSpeed(speed);
  अगर (direction == 'F') { वाम_motor.run(FORWARD); दक्षिण_motor.run(FORWARD); }
  अन्यथा अगर (direction == 'B') { वाम_motor.run(BACKWARD); दक्षिण_motor.run(BACKWARD); }
  अन्यथा अगर (direction == 'L') { वाम_motor.run(BACKWARD); दक्षिण_motor.run(FORWARD); }
  अन्यथा अगर (direction == 'R') { वाम_motor.run(FORWARD); दक्षिण_motor.run(BACKWARD); }
  अन्यथा { वाम_motor.run(RELEASE); दक्षिण_motor.run(RELEASE); }
}

व्योम setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

व्योम loop() {
  अगर (!Serial.available()) वापस;
  String line = Serial.readStringUntil('\n');
  पूर्णांक first = line.indexOf(','), second = line.indexOf(',', first + 1);
  अगर (first < 1 || second < 0) { Serial.println("ERR expected dir,duration,pwm"); वापस; }
  अक्षर direction = line.charAt(0);
  दीर्घ duration = line.substring(first + 1, second).toInt();
  पूर्णांक speed = constrain(line.substring(second + 1).toInt(), 0, 255);
  अगर (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    वापस;
  }
  drive(direction, speed);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
