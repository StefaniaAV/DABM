int outPin = 10; // Pin de salida PWM
int brightness; 
void setup() {
  pinMode(outPin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  int fotoresistencia = analogRead(A0); //Para leer del pin analogo A0
  float valor = fotoresistencia*(5.0/1023.0); //Convertir a voltaje de 0 a 5
  Serial.println(valor); //Para enviar el dato a python
  
  if (Serial.available()){
    brightness = Serial.read(); //Leer puerto serial
    analogWrite(outPin, brightness);    //Ciclo de trabajo de 0 a 255 //Para escribir en el pin de salida
  }
  
  delay(50);}
