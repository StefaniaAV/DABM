void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valorPotenciometro = analogRead(A0);

  float voltaje = valorPotenciometro*(5.0/1023.0);
  //

  //
  Serial.print("Voltaje: ");
  Serial.print(voltaje);
  Serial.println(" V");

  //
  delay(100);
}
