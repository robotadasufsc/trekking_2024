// Código Arduino

void setup() {
  Serial.begin(9600);  // Inicializa a comunicação serial a 9600 bps
}

void loop() {
  int valor = 42;  // Valor simulado
  Serial.println(valor);  // Envia o valor simulado para a porta serial
  delay(1000);  // Aguarda 1 segundo
}
