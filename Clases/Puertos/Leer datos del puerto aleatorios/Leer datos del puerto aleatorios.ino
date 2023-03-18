int ps;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  ps = random(20, 45); //crea un numero aleatorio
  Serial.println(ps); //se manda al puerto
  delay(1000);

}
