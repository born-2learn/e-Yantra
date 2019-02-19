
#define BL 190
#define BM 315
#define BR 392
#define OT 500

int state=0;
//state---0 stop 1-right 2-left
int analogPin1 = 1;  
int analogPin2 = 2;
int analogPin3 = 3;
int Lef = 0;
int Mid = 0;
int Rig = 0;
int value = 0;


int motorA1 = 3; // Pin  2 of L293
int motorA2 = 5; // Pin  7 of L293
int motorB1 = 6; // Pin 10 of L293
int motorB2 = 9;


int velrm = 250; // Speed Of Motors (0-255)
int vellm = 250; //speed while turning as 50 isnt sufficient.
int velright = 200;
int velleft =200;

void forward(){
  analogWrite(motorA1, velrm);
    analogWrite(motorA2, 0);
    analogWrite(motorB1, vellm);
    analogWrite(motorB2, 0);
    Serial.println("Forward");
}
void right(){
  analogWrite(motorA1, velright);
    analogWrite(motorA2, 0);
    analogWrite(motorB1, 0);
    analogWrite(motorB2, velright);
    state=1;
    Serial.println("Right");
}
void left(){
  analogWrite(motorA1, 0);
    analogWrite(motorA2, velleft);
    analogWrite(motorB1, velleft);
    analogWrite(motorB2, 0);
    state=2;
    Serial.println("Left");
}
void back(){
   analogWrite(motorA1, 0);
    analogWrite(motorA2, velrm);
    analogWrite(motorB1, 0);
    analogWrite(motorB2, vellm);
    Serial.println("Backward");
}
void stop_car(){
  analogWrite(motorA1, 0);
    analogWrite(motorA2, 0);
    analogWrite(motorB1, 0);
    analogWrite(motorB2, 0);
}

void setup() {
  Serial.begin(9600);

  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  lineSenor();
      

   if(Lef<BL&&Mid>BM&&Rig<BR)
   {
    forward();
   
   }
   if(Lef>BL&&Rig<BR)
   {
    right();
   
   }
   if(Lef<BL&&Rig>BR)
   {
    left();
   
   }
   if(Lef<BL&&Mid<BM&&Rig<BR)
   {
    if(state==1){
      left();
    }
    else if(state==2){
      right();
    }
    else{
    stop_car();
    }
   }
   
}
void lineSenor()
{
  //Serial.print("you you you");
  //digitalWrite(13, HIGH);
  //Serial.println("me me me");
  Lef = analogRead(analogPin1); // read the input pin
  Mid = analogRead(analogPin2);     // read the input pin
  Rig = analogRead(analogPin3);  // read the input pin
 // value = (value1+value2+value3)/3;
 // Serial.println(value);
 
 Serial.print("Left: ");
  Serial.print(Lef);
   Serial.print(" Center: ");
    Serial.print(Mid);
     Serial.print(" Right: ");
      Serial.print(Rig);
      Serial.println();
}
