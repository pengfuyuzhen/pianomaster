
#include <EEPROM.h>

// Pins
const int doPin = 0;
const int rePin = 1;
const int miPin = 2;
const int faPin = 3;
const int soPin = 4;
const int laPin = 5;
const int tiPin = 6;
const int b1Pin = 7;
const int b2Pin = 8;
const int b3Pin = 9;
const int b4Pin = 10;
const int b5Pin = 11;
const int audioPin = 12;

// Durations
const int noteDuration = 500;

// Notes {do, re, mi fa, so, la, ti}
int notes[12] = {262, 294, 330, 349, 392, 440, 494,277,311,370,415,466};

const int DO = 0;
const int RE = 1;
const int MI = 2;
const int FA = 3;
const int SO = 4;
const int LA = 5;
const int TI = 6;
const int B1 = 7;
const int B2 = 8;
const int B3 = 9;
const int B4 = 10;
const int B5 = 11;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(doPin) == HIGH) {
    Serial.println("DO");
  } else if (digitalRead(rePin) == HIGH) {
    Serial.println("RE")
  } else if (digitalRead(miPin) == HIGH) {
    Serial.println("MI");
  } else if (digitalRead(faPin) == HIGH) {
    Serial.println("FA");
  } else if (digitalRead(soPin) == HIGH) {
    Serial.println("SO");
  } else if (digitalRead(laPin) == HIGH) {
    Serial.println("LA");
  } else if (digitalRead(tiPin) == HIGH) {
    Serial.println("TI");
  } else if (digitalRead(b1Pin) == HIGH) {
    Serial.println("B1");
  } else if (digitalRead(b2Pin) == HIGH) {
    Serial.println("B2");
  }else if (digitalRead(b3Pin) == HIGH) {
    Serial.println("B3");
  }else if (digitalRead(b4Pin) == HIGH) {
    Serial.println("B4");
  }else if (digitalRead(b5Pin) == HIGH) {
    Serial.println("B5");
  }else {
    noTone(audioPin);
  }
  
}

