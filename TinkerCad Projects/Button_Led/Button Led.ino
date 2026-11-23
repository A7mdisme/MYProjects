const int buttonPin = 2;
const int ledPin = 13; 

void setup()
{
  pinMode(2,INPUT);
  pinMode(13,OUTPUT);
}

void loop()
{
  int buttonstate = digitalRead(buttonPin);
  
    if (buttonstate == HIGH){
   digitalWrite(ledPin, HIGH);
  }
  else if (buttonstate == LOW){
   digitalWrite(ledPin, LOW);
  }
}