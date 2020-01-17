
/*
 * BUTTONS
 * A            0
 * B            1
 * X            2
 * Y            3
 * Z            4
 * L            5
 * R            6
 * JOYSTICK_R_X 7
 * JOYSTICK_R_Y 8
 * JOYSTICK_L_X 9
 * JOYSTICK_L_Y 10
 * Start        11
 * 
 */

#define NUM_BUTTONS 12
byte buttonMappings[NUM_BUTTONS] = {0, 0, 0, 0, 0, 0, 128, 128, 128, 128, 0, 0};


/*
 * Generates button press command
 */
void processCommand(byte command) {
  byte button = command / 16;
  byte value = command - (16 * button);
  Serial.print("Setting button: ");
  Serial.print(button);
  Serial.print(" to: ");
  Serial.println(value);
  buttonMappings[button] = value;
}


void generateGamecubeData() {
    cleanData();
    data.report.a = buttonMappings[0];
    data.report.b = buttonMappings[1];
    data.report.x = buttonMappings[2];
    data.report.y = buttonMappings[3];
    data.report.z = buttonMappings[4];
    data.report.start = buttonMappings[11];
    data.report.r = buttonMappings[6];
    data.report.l = buttonMappings[5];
    data.report.left = 0;
    data.report.xAxis = buttonMappings[9];
    data.report.yAxis = buttonMappings[10];
    data.report.cxAxis = buttonMappings[7];
    data.report.cyAxis = buttonMappings[8];

//  while(queueHasNextElement()) {
//    Command command = getNextInput();
//    switch(command.button) {
//      case 0:
//        data.report.a = command.value;
//        break;
//      case 1:
//        data.report.b = command.value;
//        break;
//      case 2:
//        data.report.x = command.value;
//        break;
//      case 3:
//        data.report.y = command.value;
//        break;
//      case 4:
//        data.report.z = command.value;
//        break;
//      case 5:
//        data.report.l = command.value;
//        break;
//      case 6:
//        data.report.r = command.value;
//        break;
//      case 7:
//        data.report.cxAxis = command.value;
//        break;
//      case 8:
//        data.report.cyAxis = command.value;
//        break;
//      case 9:
//        data.report.xAxis = command.value;
//        break;
//      case 10:
//        data.report.yAxis = command.value;
//        break;
//      case 11:
//        data.report.start = command.value;
//        break;
//      default:
//        break;
//    }
//  }

}

void cleanData() {
  int pinA = 0;
  int pinB = 0;
  int pinX = 0;
  int pinY = 0;
  int pinZ = 0;
  int pinSTART = 0;

  int pinR = 0;
  int pinL = 0;
  int pinRLIGHT = 0;

  int pinLEFT = 0;
  int pinRIGHT = 0;
  int pinUP = 0;
  int pinDOWN = 0;

  int pinX1 = 0;
  int pinX2 = 0;
  int pinY1 = 0;
  int pinY2 = 0;

  int pinCLEFT = 0;
  int pinCRIGHT = 0;
  int pinCUP = 0;
  int pinCDOWN = 0;

  int pinxAxisC = 128;
  int pinyAxisC = 128;
  
  int pinxAxis = 128;
  int xmod = 0;
  int pinyAxis = 128;

  int rightOne = 0;
  int leftOne = 0;
  int downOne = 0;

  int pinSWITCH = 0;
  
  data.report.a = pinA;
  data.report.b = pinB;
  data.report.x = pinX;
  data.report.y = pinY;
  data.report.z = pinZ;
  data.report.start = pinSTART;
  data.report.r = pinR;
  data.report.l = pinL;
  data.report.left = pinRLIGHT;
  data.report.xAxis = pinxAxis;
  data.report.yAxis = pinyAxis;
  data.report.cxAxis = pinxAxisC;
  data.report.cyAxis = pinyAxisC;
}
