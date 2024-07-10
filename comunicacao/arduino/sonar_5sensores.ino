const int trigPin1 = 2;
const int echoPin1 = 3;

const int trigPin2 = 8;
const int echoPin2 = 9;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
}

void loop() {
  long duration1, distance1;
  long duration2, distance2;

  distance1 = getDistance(trigPin1, echoPin1);
  distance2 = getDistance(trigPin2, echoPin2);

  //Serial.print("Distance from sensor 1: ");
  Serial.println(distance1);
  //Serial.println(" cm");

  //Serial.print("Distance from sensor 2: ");
  Serial.println(distance2);
  //Serial.println(" cm");

  Serial.println(0);
  Serial.println(0);
  Serial.println(0);
  

  delay(250);
}

long getDistance(int trigPin, int echoPin) {
  long duration, distance;
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1; // Convert to centimeters
  
  return distance;
}