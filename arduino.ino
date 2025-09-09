#define NUM_PIN_DIGITAL 2 // Number of the digital pins of the arduino card or the max number you want
#define NUM_PIN_ANALOG 1 // Number of the analog pins of the arduino card or the max number you want
#define ANALOG_PRECISION 3 // Difference of value from the analogRead to be take in account
#define COMMUNICATION_SPEED 38400 // Communication speed in bits/s

// Memory of the digital & analog pins used (setup at the initialisation)
int real_digital_pins_nb[NUM_PIN_DIGITAL];
int nb_digital_pins_high = 0;
int real_analog_pins_nb[NUM_PIN_ANALOG];
int nb_analog_pins_high = 0;

// Stock of the different pins values
int digital_pins_memory[NUM_PIN_DIGITAL];
int analog_pins_memory[NUM_PIN_ANALOG];

void setup() {
    // Set the communication speed
    Serial.begin(COMMUNICATION_SPEED);

    //Serial.print("[Start Void Setup]\n");

    // Setup variables
    for (int i = 0; i < NUM_PIN_DIGITAL; real_digital_pins_nb[i] = 0, digital_pins_memory[i] = 0, i++);
    for (int i = 0; i < NUM_PIN_ANALOG; real_analog_pins_nb[i] = 0, analog_pins_memory[i] = 0, i++);

    // Analyse of the digital pins
    //Serial.println("Digital pins information:");
    for (int digital_pin = 2; digital_pin - 2 < NUM_PIN_DIGITAL; digital_pin++) {
  	    // Get the pin status
        int pin_status = digitalRead(digital_pin);

        // display the pin information
        /*
        Serial.print(pin_status);
        Serial.print(": ");
        Serial.println(pin_status == HIGH ? "HIGH" : "LOW");
        Serial.print(" - Pin n°");
        Serial.print(digital_pin);
        */

        // Save the HIGH digital pins
        if(pin_status == HIGH)
            real_digital_pins_nb[nb_digital_pins_high++] = digital_pin;
    }

    // Display the HIGH digital pins found
    /*
    Serial.print("Digital pins HIGH: ");
    for (int i = 0; i < nb_digital_pins_high; i++) {
        Serial.print(real_digital_pins_nb[i]);
    	if (i + 1 < nb_digital_pins_high) Serial.print(", ");
    }
    Serial.println("\n");
    */

    // Analyse of the analog pins
    //Serial.println("Analog pins information:");
    for (int analog_pin = 0; analog_pin < NUM_PIN_ANALOG; analog_pin++) {
  	    // Get the pin status
        int pin_status = analogRead(analog_pin);

        // display the pin information
        /*
        Serial.print(pin_status);
        Serial.print(" - Pin n°A");
        Serial.print(analog_pin);
        Serial.print(": ");
        Serial.println(pin_status >= 1 ? "HIGH" : "LOW");
        */

        // Save the HIGH analog pins
        if(pin_status >= 1)
            real_analog_pins_nb[nb_analog_pins_high++] = analog_pin;
    }

    // Display the HIGH digital pins found
    /*
    Serial.print("Analog pins HIGH: ");
    for (int i = 0; i < nb_analog_pins_high; i++) {
   	    Serial.print("A");
        Serial.print(real_analog_pins_nb[i]);
        if (i + 1 < nb_analog_pins_high) Serial.print(", ");
    }
    Serial.println("\n");
    */

    //Serial.print("[End Void Setup]\n");
}

void loop()
{
    int pin_status = 0;

    // Digital
    for (int i = 0; i < nb_digital_pins_high; i++) {
    	pin_status = digitalRead(real_digital_pins_nb[i]);
  	    if (pin_status != digital_pins_memory[i]) {
  	        digital_pins_memory[i] = pin_status;
  	        Serial.println(String(real_digital_pins_nb[i]) + ":" + String(pin_status == 1 ? 0 : 1));
        }
    }

    // Analog
    for (int i = 0; i < nb_analog_pins_high; i++) {
        pin_status = analogRead(real_analog_pins_nb[i]);
        if (pin_status > analog_pins_memory[i] + ANALOG_PRECISION || pin_status < analog_pins_memory[i] - ANALOG_PRECISION) {
  	        analog_pins_memory[i] = pin_status;
  	        Serial.println("A" + String(real_analog_pins_nb[i]) + ":" + String(pin_status));
        }
    }
}