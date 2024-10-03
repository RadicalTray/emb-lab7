#include <SoftwareSerial.h>

SoftwareSerial destSerial(17, 16);

constexpr int myBaudRate = 115200;
constexpr int theirBaudRate = myBaudRate;

void setup() {
  Serial.begin(myBaudRate);
  destSerial.begin(theirBaudRate);
  Serial.print("Hi!");
}

void loop() {
  while (Serial.available()) {
    char b = Serial.read();
    destSerial.write(b);
  }
}
