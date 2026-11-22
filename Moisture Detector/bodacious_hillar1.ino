const int sensorPin = A0;
const int startWateringBelow = 300;
const int stopWateringAbove = 500;

bool watering = false; 

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  int moisture = analogRead(sensorPin);
  
  if (moisture < startWateringBelow) {
    watering = true;
  }
  else if (moisture > stopWateringAbove) {
    watering = false;
  }
  
  digitalWrite(LED_BUILTIN, watering ? HIGH : LOW); //serial is the name the code uses to communicate with my computer
  
  Serial.print("Moisture reading: "); 
  Serial.print(moisture);
  Serial.println(watering? " | Sprinkler ON" : " | Sprinkler OFF");
              //println is the same as the ? it means if the water condition is true then display Sprinkler On, otherwise display Sprinkler OFF   
  delay(500);
                 }