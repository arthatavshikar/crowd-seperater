#include <AFMotor.h> 

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);

void setup(){
motor1.setSpeed(200);
motor2.setSpeed(200);
Serial.begin(9600);
}

void loop() { 
  int count = Serial.parseInt();
  if (count>1){
motor1.run(FORWARD);   
motor2.run(FORWARD);
delay(2000); 
motor1.run(RELEASE);
motor2.run(RELEASE);
}

}
