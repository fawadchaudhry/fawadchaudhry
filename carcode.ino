#include <Servo.h>
Servo myservo;  
int pos = 0;  
int value = 0;
void setup() {
  pinMode(34,OUTPUT); //input
  pinMode(35,OUTPUT); //input
  pinMode(12,OUTPUT);  //PWM
  pinMode(36,OUTPUT); //input
  pinMode(37,OUTPUT); //input
  pinMode(13,OUTPUT);  //PWM 
  pinMode(22,OUTPUT);
  pinMode(23,OUTPUT);
  pinMode(24,OUTPUT);
  pinMode(30,OUTPUT);
  pinMode(31,OUTPUT);
  pinMode(32,OUTPUT);
  myservo.attach(11);
  Serial.begin(9600);  //default value for hc 05
}

void loop() {
   if(Serial.available()>0){
value = Serial.read();
  }
   if(value == '1'){ 
 digitalWrite(34,LOW);
 digitalWrite(35,HIGH);
 digitalWrite(36,LOW);
 digitalWrite(37,HIGH);
 analogWrite(12,255);
 analogWrite(13,255);
 delay(3);
  }
   if(value == '2'){
 digitalWrite(34,LOW);
 digitalWrite(35,LOW);
 digitalWrite(36,LOW);
 digitalWrite(37,HIGH);
 analogWrite(12,0);
 analogWrite(13,255);
 delay(3);
  }
   if(value == '3'){
 digitalWrite(34,LOW);
 digitalWrite(35,LOW);
 digitalWrite(36,LOW);
 digitalWrite(37,LOW);
 analogWrite(12,0);
 analogWrite(13,0);
 delay(3);
  }
   if(value == '4'){
 digitalWrite(34,LOW);
 digitalWrite(35,HIGH);
 digitalWrite(36,LOW);
 digitalWrite(37,LOW);
 analogWrite(12,255);
 analogWrite(13,0);
 delay(3);
  }
   if(value == '5'){
 digitalWrite(34,HIGH);
 digitalWrite(35,LOW);
 digitalWrite(36,HIGH);
 digitalWrite(37,LOW);
 analogWrite(12,255);
 analogWrite(13,255);
 delay(3);
  }
  if(value == '6'){
 digitalWrite(22,HIGH);
 digitalWrite(23,HIGH);
 digitalWrite(24,HIGH);
 digitalWrite(30,HIGH);
 digitalWrite(31,HIGH);
 digitalWrite(32,HIGH);
 delay(3);
  }
  if(value == '7'){
 digitalWrite(22,LOW);
 digitalWrite(23,LOW);
 digitalWrite(24,LOW);
 digitalWrite(30,LOW);
 digitalWrite(31,LOW);
 digitalWrite(32,LOW);
 delay(3);
  }
  if(value == '8'){
  digitalWrite(34,LOW);
  digitalWrite(35,LOW);
  digitalWrite(36,LOW);
  digitalWrite(37,LOW);
  analogWrite(12,0);
  analogWrite(13,0);
  delay(3);
  pos+=90;
  myservo.write(pos);
  delay(3000);
  pos+=90;
  myservo.write(pos);
  delay(3000);
  pos-=90;
  myservo.write(pos);
  delay(3000);
  pos-=90;
  myservo.write(pos);
  delay(3000);
  value == '3';
  }
} 
