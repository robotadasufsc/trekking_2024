void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  int v1 = random(100);
  int v2 = random(100);
  int v3 = random(100);
  int v4 = random(100);
  int v5 = random(100);
  //int vetor[] = {v1, v2, v3, v4, v5};
  Serial.println(v1);
  Serial.println(v2);
  Serial.println(v3);
  Serial.println(v4);
  Serial.println(v5);
  delay(10);
}
