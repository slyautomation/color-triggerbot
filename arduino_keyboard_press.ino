#include <Keyboard.h>

const int buttonPin = 2; // The pin number where your button is connected
int buttonState = 0;     // Variable to store the button state

void setup() {
  // Initialize the button pin as an input
  pinMode(buttonPin, INPUT);
  // Initialize the keyboard
  Serial.begin(1000000); 
  Serial.setTimeout(1);
  Keyboard.begin();
}

void loop() {
  // Read the state of the button
  buttonState = digitalRead(buttonPin);
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); // Read the serial input until newline character
    input.trim(); // Remove leading and trailing spaces
    //Serial.println(input);
    // Check if the input is a valid format
    if (input == "left") {
      Keyboard.press('l');
      delay(50); // Adjust delay as needed
      Keyboard.release('l');
  // If the button is pressed
    //if (buttonState == HIGH) {
      // Press the 'L' key
    //}
    }
  }

}