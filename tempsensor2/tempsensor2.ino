#include "DHT.h"
int temperaturePin = 0;
int lightPin = 1;
int soilmoistPin = A2;
DHT dht2;
DHT dht4;
void setup()
{
  Serial.begin(9600);
  Serial.println();


  dht2.setup(2); // data pin 2
  dht4.setup(4); // data pin 4
  pinMode(soilmoistPin, INPUT);
}

void loop()
{
  delay(dht2.getMinimumSamplingPeriod());
  
  float soilmoistValue = analogRead(soilmoistPin);
  float soilmoistMapper = map(soilmoistValue,200,1024,100,0);
  float soilmoistPercent = soilmoistMapper;
  float lightLevel = analogRead(lightPin);
  
  float Vout = (lightLevel*0.0048828125);

  float RLDR = (10000*(5-Vout))/Vout;
  float Lux = (0.500/RLDR);
  
  float humidity2 = dht2.getHumidity();
  float temperature2 = dht2.getTemperature();
  float humidity4 = dht4.getHumidity();
  float temperature4 = dht4.getTemperature();
  Serial.print(humidity2, 1);
  Serial.print("\t");
  Serial.print(temperature2, 1);
  Serial.print("\t");
  Serial.print(humidity4, 1);
  Serial.print("\t");
  Serial.print(temperature4, 1);
  Serial.print("\t");
  Serial.print(RLDR, 1);
  Serial.print("\t");
  Serial.print(soilmoistPercent, 1);
  Serial.print("\t");
  Serial.println();
  Serial.flush();
}

