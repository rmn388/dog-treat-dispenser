#include <Servo.h>

Servo piston;
int pos_in = 180;
int pos_alert = 150;
int pos_out = 15;
int alert_input = 0;
int old_alert_input = 0;
int treat_input = 0;
int old_treat_input = 0;
const int pi_alert = 7; //17 on pi
const int pi_treat = 8; //18 on pi

void setup() {
  piston.attach(A0); //Servo Output
  piston.write(pos_in);
  piston.detach();
  pinMode(pi_treat, INPUT); //Raspberry Pi treat pin
  pinMode(pi_alert, INPUT); //Raspberry Pi alert pin
  
}


void loop() {
  alert_input = digitalRead(pi_alert);
  treat_input = digitalRead(pi_treat);
  if (alert_input > old_alert_input){
    piston.attach(3);
      for (int x=0; x<3; x++){
      
      piston.write(pos_alert);
      delay(150);
      piston.write(pos_in);
      delay(150);
    }
   piston.detach(); 
  }
  
  if (treat_input > old_treat_input){
    piston.attach(3);
    piston.write(pos_out);
    delay(1000);
    piston.write(pos_in);
    delay(1000);
    piston.detach(); 
  }
  
  old_alert_input = alert_input;
  old_treat_input = treat_input;
}