// Bluetooth HC-05 type II for AT Command
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11);
int in = A0;

void setup() {
  pinMode(in, INPUT);
  
  // for HC-05 with EN pin
  Serial.begin(9600);
//  Serial.println("Enter AT commands: ");
  BTSerial.begin(38400);  // Default bound rate: 38400 bps
}

void loop() {

  byte val = map(analogRead(in), 0, 1023, 0, 255);
  BTSerial.write(val);
  Serial.println(analogRead(in));
  Serial.println(val);
  
  delay(40);
  
//  // Read HC-05 and send to Arduino Serial Monitor
  if (BTSerial.available()) {
    Serial.write(BTSerial.read());
  }

  // Read Serial and send to HC-05
  if (Serial.available()) {
    BTSerial.write(Serial.read());
  }
}