// Stage 1 robot (ages 12 and up): Arduino UNO with an L293D motor shield, driven over the USB cable.
// It takes the AyeAM control interface's commands, one per line: "<dir>,<duration>,<pwm>", where dir is F (forward),
// B (backward), L (left), R (right) or S (stop), duration is in milliseconds and pwm is 0 to 255. It answers OK, or ERR.
// Needs the "Adafruit Motor Shield library" (AFMotor) from the Arduino Library Manager.
// © 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India.
#ಅನ್ತರ್ಭಾವ <AFMotor.h>

AF_DCMotor ಎಡಭಾಗ_motor(1);
AF_DCMotor ಬಲಭಾಗ_motor(2);

ಶೂನ್ಯ drive(ಅಕ್ಷರ direction, ಪೂರ್ಣಾಂಕ ವೇಗ) {
  ಎಡಭಾಗ_motor.setSpeed(ವೇಗ);
  ಬಲಭಾಗ_motor.setSpeed(ವೇಗ);
  ಆದರೆ (direction == 'F') { ಎಡಭಾಗ_motor.run(FORWARD); ಬಲಭಾಗ_motor.run(FORWARD); }
  ಇಲ್ಲದಿದ್ದರೆ ಆದರೆ (direction == 'B') { ಎಡಭಾಗ_motor.run(BACKWARD); ಬಲಭಾಗ_motor.run(BACKWARD); }
  ಇಲ್ಲದಿದ್ದರೆ ಆದರೆ (direction == 'L') { ಎಡಭಾಗ_motor.run(BACKWARD); ಬಲಭಾಗ_motor.run(FORWARD); }
  ಇಲ್ಲದಿದ್ದರೆ ಆದರೆ (direction == 'R') { ಎಡಭಾಗ_motor.run(FORWARD); ಬಲಭಾಗ_motor.run(BACKWARD); }
  ಇಲ್ಲದಿದ್ದರೆ { ಎಡಭಾಗ_motor.run(RELEASE); ಬಲಭಾಗ_motor.run(RELEASE); }
}

ಶೂನ್ಯ setup() {
  Serial.begin(115200);
  drive('S', 0);
  Serial.println("READY");
}

ಶೂನ್ಯ loop() {
  ಆದರೆ (!Serial.available()) ಹಿಂತಿರುಗಿ;
  String ಸಾಲು = Serial.readStringUntil('\n');
  ಪೂರ್ಣಾಂಕ ಮೊದಲ = ಸಾಲು.indexOf(','), ಎರಡನೇ = ಸಾಲು.indexOf(',', ಮೊದಲ + 1);
  ಆದರೆ (ಮೊದಲ < 1 || ಎರಡನೇ < 0) { Serial.println("ERR expected dir,duration,pwm"); ಹಿಂತಿರುಗಿ; }
  ಅಕ್ಷರ direction = ಸಾಲು.charAt(0);
  ದೀರ್ಘ duration = ಸಾಲು.substring(ಮೊದಲ + 1, ಎರಡನೇ).toInt();
  ಪೂರ್ಣಾಂಕ ವೇಗ = constrain(ಸಾಲು.substring(ಎರಡನೇ + 1).toInt(), 0, 255);
  ಆದರೆ (direction != 'F' && direction != 'B' && direction != 'L' && direction != 'R' && direction != 'S') {
    Serial.println("ERR unknown direction");
    ಹಿಂತಿರುಗಿ;
  }
  drive(direction, ವೇಗ);
  delay(duration);
  drive('S', 0);
  Serial.println("OK");
}
