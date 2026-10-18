// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#include <AFMotor.h>

AF_DCMotor left_motor(1);
AF_DCMotor right_motor(2);

void drive(char direction, int speed) {
  left_motor.setSpeed(speed);
  right_motor.setSpeed(speed);
  if (direction == 'F') { left_motor.run(FORWARD); right_motor.run(FORWARD); }
  else if (direction == 'B') { left_motor.run(BACKWARD); right_motor.run(BACKWARD); }
  else if (direction == 'L') { left_motor.run(BACKWARD); right_motor.run(FORWARD); }
  else if (direction == 'R') { left_motor.run(FORWARD); right_motor.run(BACKWARD); }
  else { left_motor.run(RELEASE); right_motor.run(RELEASE); }
}

void setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

void loop() {
  if (!Serial.available()) return;
  String line = Serial.readStringUntil('\n');
  int first = line.indexOf(','), second = line.indexOf(',', first + 1);
  if (first < 1 || second < 0) { Serial.println("ERR expected dir,duration,pwm"); return; }
  char direction = line.charAt(0);
  long duration = line.substring(first + 1, second).toInt();
  int speed = constrain(line.substring(second + 1).toInt(), 0, 255);
  if (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    return;
  }
  drive(direction, speed);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
