#include <SoftwareSerial.h>

SoftwareSerial srcSerial(17, 16);

constexpr int myBaudRate = 115200;
constexpr int theirBaudRate = myBaudRate;

void setup() {
  Serial.begin(myBaudRate);
  srcSerial.begin(theirBaudRate);
  Serial.print("Hi!");
}

void loop() {
  while (srcSerial.available()) {
    char b = srcSerial.read();
    Serial.write(b);
  }
}
