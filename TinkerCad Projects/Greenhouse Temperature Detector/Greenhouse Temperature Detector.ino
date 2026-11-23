const int tmpS = A0;
const int ledPin = 7;
const int tmpAbove = 31;
const int tmpBelow = 30;
bool detection = false;
const int vbr = 4; 
void setup()
{
  pinMode(tmpS,INPUT);
  pinMode(ledPin,OUTPUT);
  pinMode(vbr,OUTPUT);
  digitalWrite(vbr,LOW);
  digitalWrite(ledPin,LOW);
  Serial.begin(9600);
}

void loop()
{
  
  int tempstate = analogRead(tmpS);
  float voltage = tempstate * (5.0/1024.0);
  float tmpC = (voltage - 0.5) * 100.0;
  
  if (tmpC >= tmpAbove){
   detection = true; 
  }else if (tmpC <= tmpBelow){
   detection = false; 
  }
  if(detection){
   digitalWrite(ledPin, HIGH);
   digitalWrite(vbr, HIGH);
  } else {
   digitalWrite(ledPin , LOW); 
   digitalWrite(vbr, LOW);
  }
  
  Serial.print("Temperature: ");
  Serial.print(tmpC,1);
  Serial.println(" C");

  delay(250);
}