// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#అన్తర్భావ <AFMotor.h>

AF_DCMotor ఎడమవైపు_motor(1);
AF_DCMotor కుడివైపు_motor(2);

శూన్య drive(అక్షరం direction, పూర్ణాంకం వేగం) {
  ఎడమవైపు_motor.setSpeed(వేగం);
  కుడివైపు_motor.setSpeed(వేగం);
  ఒకవేళ (direction == 'F') { ఎడమవైపు_motor.run(FORWARD); కుడివైపు_motor.run(FORWARD); }
  లేకపోతే ఒకవేళ (direction == 'B') { ఎడమవైపు_motor.run(BACKWARD); కుడివైపు_motor.run(BACKWARD); }
  లేకపోతే ఒకవేళ (direction == 'L') { ఎడమవైపు_motor.run(BACKWARD); కుడివైపు_motor.run(FORWARD); }
  లేకపోతే ఒకవేళ (direction == 'R') { ఎడమవైపు_motor.run(FORWARD); కుడివైపు_motor.run(BACKWARD); }
  లేకపోతే { ఎడమవైపు_motor.run(RELEASE); కుడివైపు_motor.run(RELEASE); }
}

శూన్య setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

శూన్య loop() {
  ఒకవేళ (!Serial.available()) తిరిగి;
  String పంక్తి = Serial.readStringUntil('\n');
  పూర్ణాంకం మొదటి = పంక్తి.indexOf(','), రెండవ = పంక్తి.indexOf(',', మొదటి + 1);
  ఒకవేళ (మొదటి < 1 || రెండవ < 0) { Serial.println("ERR expected dir,duration,pwm"); తిరిగి; }
  అక్షరం direction = పంక్తి.charAt(0);
  దీర్ఘ duration = పంక్తి.substring(మొదటి + 1, రెండవ).toInt();
  పూర్ణాంకం వేగం = constrain(పంక్తి.substring(రెండవ + 1).toInt(), 0, 255);
  ఒకవేళ (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    తిరిగి;
  }
  drive(direction, వేగం);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
