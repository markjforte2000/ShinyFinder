// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

// This example code is in the public domain.

// 04-Feb-2018 mcarter adapted
#include <Wire.h>
#include "Nintendo.h"

const int ledPin = 13; // onboard LED
static_assert(LOW == 0, "Expecting LOW to be 0");

//This makes the controller bidirection data line on pin number8
CGamecubeConsole GamecubeConsole(8);      //Defines a "Gamecube Console" sending data to the console on pin 8
Gamecube_Data_t data = defaultGamecubeData;   //Structure for data to be sent to console

//This is needed but you don't need a controller on pin 7
CGamecubeController GamecubeController1(7);

void setup() {
  Wire.begin(0x8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // turn it off
  Serial.begin(9600);
  GamecubeController1.read();
}




bool pressA = true;
unsigned long currentTime;
unsigned long lastPress = 0;
unsigned long pressWaitTime = 50;

void loop() {

  // get data from i2c
//  byte command;
//  bool gotData = false;
//  while (Wire.available()) { // loop through all but the last
//    gotData = true;
//    command = Wire.read(); // receive byte as a character
//  }
//  if(gotData){
//    processCommand(command);
//  }

  delay(50);
  generateGamecubeData();

  GamecubeConsole.write(data);
}


// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  byte command;
  while (Wire.available()) { // loop through all but the last
    digitalWrite(13, HIGH);
    command = Wire.read(); // receive byte as a character
  }
  processCommand(command);
}
