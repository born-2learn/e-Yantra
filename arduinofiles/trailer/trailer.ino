
#define LT 80
#define RT 80
#define MT 80
#define OT 500

int state=0;
//state---0 stop 1-right 2-left
int analogPin1 = 1;  
int analogPin2 = 2;
int analogPin3 = 3;
int L = 0;
int M = 0;
int R = 0;
int value = 0;

char r='5';
char c='y';
int motorA1 = 3; // Pin  2 of L293
int motorA2 = 5; // Pin  7 of L293
int motorB1 = 6; // Pin 10 of L293
int motorB2 = 9;


int vellm = 160; // Speed Of Motors (0-255)
int velrm = 160; //speed while turning as 50 isnt sufficient.
int velleft = 90;
int velright =90;

void forward(){
  analogWrite(motorA1, velrm);
    analogWrite(motorA2, 0);
    analogWrite(motorB1, vellm);
    analogWrite(motorB2, 0);
    Serial.println("Forward");
}
void right(){
  analogWrite(motorA1, velleft);
    analogWrite(motorA2, 0);
    analogWrite(motorB1, 0);
    analogWrite(motorB2, velright);
    state=1;
    Serial.println("Right");
}
void rotateleft(){
  forward();
  delay(500);
  analogWrite(motorA1, 0);
    analogWrite(motorA2, velleft);
    analogWrite(motorB1, velright);
    analogWrite(motorB2, 0);
    state=1;
    Serial.println("Left");
}
void rotateright(){
  forward();
  delay(500);
  analogWrite(motorA1, velleft);
    analogWrite(motorA2, 0);
    analogWrite(motorB1, 0);
    analogWrite(motorB2, velright);
    state=2;
    Serial.println("Right");
}

void Complete_turn()
{
  
  
  int ctr=0;
  while(ctr!=4)
  {
    right();
    lineStable();
    ctr++;
    
  }
  
}
void left(){
  analogWrite(motorA1, 0);
    analogWrite(motorA2, velleft);
    analogWrite(motorB1, velright);
    analogWrite(motorB2, 0);
    state=2;
    Serial.println("Left");
}
void back(){
   analogWrite(motorA1, 0);
    analogWrite(motorA2, vellm);
    analogWrite(motorB1, 0);
    analogWrite(motorB2, velrm);
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
    pinMode(3,OUTPUT);
    pinMode(4,OUTPUT);
    pinMode(6,OUTPUT);
    pinMode(9,OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  r='5';
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    r= Serial.read();
    
  }
  if(r=='5'){
  lineSensor();
  //Serial.println("line sensor");
  }
    
   else if(r=='0'){
    stop_car();
    Serial.println("Stop");
    if(Serial.read()!='y')
    {//Do Nothing
      }
    
  }
  else if(r=='1'){
    r='5';
    forward();
    delay(500);
    
    
    
  }
  else if(r=='2'){
    r='5';
    rotateright();
    delay(500);
    
    
    
  }
  else if(r=='3'){
    r='5';
    rotateleft();
    
    delay(1000);
    
   
  }
  else if(r=='4'){
    r='5';
    back();
    delay(500);
  }
  else if(r=='t'){
    Complete_turn();
  }
  
 // Serial.println(r);
 
  
 // lineSenor();
      delay(10);

   
   
}
void lineSensor()
{
 
  R = analogRead(analogPin1); // read the input pin
  M = analogRead(analogPin2);     // read the input pin
  L = analogRead(analogPin3);  // read the input pin

 
 Serial.print("Left: ");
  Serial.print(L);
   Serial.print(" Center: ");
    Serial.print(M);
     Serial.print(" Right: ");
      Serial.print(R);
      Serial.println();

      if(L<LT&&M>MT&&R<RT)
   {
    forward();
    state=0;
   
   }
   if(L<LT&&R>RT&&M<MT)
   {
    right();
   
   }
   if(L>LT&&R<RT&&M<MT)
   {
    left();
    
   
   }
   if(L<LT&&M<MT&&R<RT)
   {
    if(state==1){
      left();
      state=0;
    }
    if(state==2){
      right();
      state=0;
    }
    
   }
   if((L>LT&&R>RT)||(R>RT&&M>MT)||(L>LT&&M>MT)){
    stop_car();
   }

   
}

void lineStable()
{
 right();
 delay(1000);
  R = analogRead(analogPin1); // read the input pin
  M = analogRead(analogPin2);     // read the input pin
  L = analogRead(analogPin3);  // read the input pin

 
 Serial.print("Left: ");
  Serial.print(L);
   Serial.print(" Center: ");
    Serial.print(M);
     Serial.print(" Right: ");
      Serial.print(R);
      Serial.println();

      while(!(L<LT&&M>MT&&R<RT))
   {
    R = analogRead(analogPin1); // read the input pin
  M = analogRead(analogPin2);     // read the input pin
  L = analogRead(analogPin3);  // read the input pin
   
   if(L<LT&&R>RT&&M<MT)
   {
    right();
   
   }
   if(L>LT&&R<RT&&M<MT)
   {
    left();
    
   
   }
   if(L<LT&&M<MT&&R<RT)
   {
    if(state==1){
      left();
      state=0;
    }
    if(state==2){
      right();
      state=0;
    }
    
   }
   
}

  stop_car();
}
}
