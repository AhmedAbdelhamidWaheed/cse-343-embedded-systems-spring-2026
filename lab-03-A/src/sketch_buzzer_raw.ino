const int buzzerPin = 9;
void setup(){
  pinMode(buzzerPin, OUTPUT);
}

void loop(){
  tone(buzzerPin, 1500, 500);
  delay(1000);
}
