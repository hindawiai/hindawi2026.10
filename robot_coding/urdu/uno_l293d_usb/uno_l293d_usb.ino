// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#شامل <AFMotor.h>

AF_DCMotor بائیں_motor(1);
AF_DCMotor دائیں_motor(2);

خالی drive(حرف direction, صحیح رفتار) {
  بائیں_motor.setSpeed(رفتار);
  دائیں_motor.setSpeed(رفتار);
  اگر (direction == 'F') { بائیں_motor.run(FORWARD); دائیں_motor.run(FORWARD); }
  ورنہ اگر (direction == 'B') { بائیں_motor.run(BACKWARD); دائیں_motor.run(BACKWARD); }
  ورنہ اگر (direction == 'L') { بائیں_motor.run(BACKWARD); دائیں_motor.run(FORWARD); }
  ورنہ اگر (direction == 'R') { بائیں_motor.run(FORWARD); دائیں_motor.run(BACKWARD); }
  ورنہ { بائیں_motor.run(RELEASE); دائیں_motor.run(RELEASE); }
}

خالی setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

خالی loop() {
  اگر (!Serial.available()) واپس;
  String سطر = Serial.readStringUntil('\n');
  صحیح پہلا = سطر.indexOf(','), دوسرا = سطر.indexOf(',', پہلا + 1);
  اگر (پہلا < 1 || دوسرا < 0) { Serial.println("ERR expected dir,duration,pwm"); واپس; }
  حرف direction = سطر.charAt(0);
  طویل duration = سطر.substring(پہلا + 1, دوسرا).toInt();
  صحیح رفتار = constrain(سطر.substring(دوسرا + 1).toInt(), 0, 255);
  اگر (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    واپس;
  }
  drive(direction, رفتار);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
