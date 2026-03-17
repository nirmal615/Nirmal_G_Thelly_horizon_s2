
#include <Servo.h>

Servo myServo;

int potPin = A0;
int ledPin = 7;

void setup()
{
  myServo.attach(9);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int potValue = analogRead(potPin);

  int angle = map(potValue, 0, 1023, 0, 180);

  if(angle > 68)
  {
    angle = 68;
    digitalWrite(ledPin, HIGH);
  }
  else
  {
    digitalWrite(ledPin, LOW);
  }

  myServo.write(angle);

  delay(20);
}
