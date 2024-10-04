#include <Arduino.h>

#define RXD1 (16)
#define TXD1 (17)

constexpr int baudrate = 115200;

void setup() {
  Serial.begin(baudrate);
  Serial1.begin(baudrate, SERIAL_8N1, RXD1, TXD1);
}

void loop() {
  if (Serial1.available()) {
    Serial.write(Serial1.read());
  }
}
