#include "Nintendo.h"

// Setup gamecube and controller
CGamecubeController GamecubeController1(7);
CGamecubeConsole GamecubeConsole(8);
Gamecube_Data_t data = defaultGamecubeData;

/*
   BUTTONS
   A            0
   B            1
   X            2
   Y            3
   Z            4
   L            5
   R            6
   JOYSTICK_R_X 7
   JOYSTICK_R_Y 8
   JOYSTICK_L_X 9
   JOYSTICK_L_Y 10
   Start        11

*/

// button map array
#define NUM_BUTTONS 11
byte buttonMappings[NUM_BUTTONS + 1] = {0, 0, 0, 0, 0, 0, 0, 128, 128, 128, 128, 0};

// alert led
const int LED = 13;

// Success response code
#define CODE_GOOD 12

void setup()
{
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  GamecubeController1.read();
}


int bytesReceived = 0;
int bytes[3];

void loop() {
  if (bytesReceived == 2) {
    decodeCommand(bytes[0], bytes[1]);
    bytesReceived = 0;
    Serial.write(CODE_GOOD);
  }
  while (Serial.available()) {
    char raw = Serial.read();
    raw -= 1;
    bytes[bytesReceived++] = raw;
  }

  data.report.a = buttonMappings[0];
  data.report.b = buttonMappings[1];
  data.report.x = buttonMappings[2];
  data.report.y = buttonMappings[3];
  data.report.z = buttonMappings[4];
  data.report.l = buttonMappings[5];
  data.report.r = buttonMappings[6];
  data.report.cxAxis = buttonMappings[7];
  data.report.cyAxis = buttonMappings[8];
  data.report.xAxis = buttonMappings[9];
  data.report.yAxis = buttonMappings[10];
  data.report.start = buttonMappings[11];
  // send data
  GamecubeConsole.write(data);
}


void resetButtonMappings() {
  buttonMappings[0] = 0;
  buttonMappings[1] = 0;
  buttonMappings[2] = 0;
  buttonMappings[3] = 0;
  buttonMappings[4] = 0;
  buttonMappings[5] = 0;
  buttonMappings[6] = 0;
  buttonMappings[7] = 128;
  buttonMappings[8] = 128;
  buttonMappings[9] = 128;
  buttonMappings[10] = 128;
  buttonMappings[11] = 0;
}


void decodeCommand(byte button, byte value) {
  if (button >= NUM_BUTTONS) {
    return;
  }
  buttonMappings[button] = value;
}
