int analogPin1 = 1;  
int analogPin2 = 2;
int analogPin3 = 3;

int Lef = 0;
int Mid = 0;
int Rig = 0;
int value = 0;


void setup() {
  Serial.begin(9600);

  // put your setup code here, to run once:

}
void loop() {
  // put your main code here, to run repeatedly:
  lineSenor();
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
