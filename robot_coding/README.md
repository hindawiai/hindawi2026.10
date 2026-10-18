# Robot coding in your own language

© 1993–2026 Abhishek Choudhary. All rights reserved. AyeAI. AyeAM® is his registered trademark in India; Hindawi™ is his
trademark.

Students build a small robot, program it in their own language, and drive it from a phone or a laptop. The robots and
their commands are those of the AyeAM robot control interface (ayecnse/ayeam-robot); the same commands drive the robot
simulator on ayecnse.net, so a program can be tried in the simulator before the robot is built.

## The robots, stage by stage

| Stage | Build | Ages |
|---|---|---|
| 1 | Arduino UNO with an L293D motor shield, connected by USB | 12 and up |
| 2 | Arduino UNO with WiFi | 14 and up |
| 3 | ESP32 with an L298N driver, no shield, its own WiFi | 16 and up |
| 4 | Expansion: servo gripper, robot arm, omni-wheels | 16 and up |

Stage 1, wired:

```
Arduino UNO
├── L293D motor shield
│   ├── M1: left motor
│   ├── M2: right motor
│   └── power: 6 to 12 V battery
└── USB cable to the computer
```

Stage 3:

```
ESP32
├── L298N module
│   ├── IN1, IN2: left motor
│   ├── IN3, IN4: right motor
│   ├── ENA, ENB: speed (PWM)
│   └── its own battery, ground joined to the ESP32's
└── built-in WiFi
```

The basic robot is meant to cost under 1000 rupees: an Arduino UNO, an L293D shield, two geared DC motors with wheels, a
caster wheel, a plastic chassis, a battery holder and a USB cable. Prices differ by seller; check them when buying.

## The commands

Every command is three values: **direction, time in milliseconds, speed from 0 to 255**. Direction is `F` forward, `B`
backward, `L` left, `R` right, `S` stop. `F,1000,200` drives forward for one second at speed 200.

- Stage 1 reads one command per line from the USB cable, at 115200 baud, and answers `OK`.
- Stage 3 answers the control interface over WiFi: `GET /cmd?data=F,1000,200&seq=1`, answering `OK`.

## Programming it in your language

1. Install the Arduino IDE (or `arduino-cli`).
2. In a checkout of hindawiai/hindawi2026.10, connect the IDE to your language once:
   `bash ide/arduino/install.sh --lang urdu`. Every Arduino core on the machine then builds sketches written in Urdu.
3. Open the sketch for your stage in your language: `urdu/uno_l293d_usb/uno_l293d_usb.ino`, or
   `urdu/esp32_l298n_wifi/esp32_l298n_wifi.ino`. The same sketches are here in Hindi, Telugu, Kannada, Tamil and Punjabi,
   and in English beside them.
4. Stage 1 also needs the "Adafruit Motor Shield library" (AFMotor) from the Library Manager.
5. Choose the board (Arduino UNO, or the ESP32 board you have), upload, and open the Serial Monitor at 115200 baud.
6. Type `F,1000,200`. The robot drives forward for a second and the Serial Monitor shows `OK`.

The keywords of the sketch (if, else, return, the types) and the names the student chooses are in the language. The
names of the Arduino library (`setup`, `loop`, `Serial`, `setSpeed`, `run`, `digitalWrite`) stay as the library writes
them, because the library itself is in English; giving the library names in every language is a work package.

## What has been checked, and what has not

- Both English sketches, and their Urdu, Tamil and Hindi versions after lowering through Hindawi's compilation path,
  pass a C++ syntax check against stand-in Arduino headers.
- They have not yet been compiled against the real AVR and ESP32 cores, nor run on a robot. That is the first run on a
  machine with the cores installed, and its result belongs in this file.

## Safety

Children build and drive the robots with an adult present. Batteries, chargers and motors can heat up or catch fire if
shorted; never leave a charging battery unattended.
