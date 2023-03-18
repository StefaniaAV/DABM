int outPin = 10;
int brightness;
void setup() {
  pinMode(outPin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  int fotoresistencia = analogRead(A0);
  float valor = fotoresistencia*(5.0/1023.0);
  Serial.println(valor); //para enviar el dato a python
  
  if (Serial.available()){
    brightness = Serial.read();
    analogWrite(outPin, brightness);    //ciclo de trabajo de 0 a 255
  }
  
  delay(500);}
