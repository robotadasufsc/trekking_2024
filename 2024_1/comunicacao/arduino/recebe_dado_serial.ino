// Código Arduino

int ledPin = 13;  // Pino onde o LED está conectado

void setup() {
  pinMode(ledPin, OUTPUT);  // Configura o pino do LED como saída
  Serial.begin(9600);       // Inicializa a comunicação serial a 9600 bps
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();  // Lê o comando recebido via serial

    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Liga o LED
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Desliga o LED
    }
  }
}
