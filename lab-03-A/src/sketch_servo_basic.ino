//Written By DKV 3-8-19, Servo tester//
#include <Servo.h>
Servo servo1; //first servo attached to A0

int servoPos1 = 0; //starting positions for servos

void setup() {
  servo1.attach(A0); //servo attaching pins (A0)
};

void loop() {
//SERVO 1
  for(servoPos1 =0; servoPos1 < 180; servoPos1++) //When servo is a position 0, servo will rotate to 180 degrees (half rotation)
  {
    servo1.write(servoPos1);
    delay(10);
  };
  
  for(servoPos1 = 180; servoPos1 > 0; servoPos1--) //When servo is a position 180, servo will rotate to 0 degrees (beginning position)
  {
    servo1.write(servoPos1);
    delay(10); 
  };
};
