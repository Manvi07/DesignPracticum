const int currentPin = A0;
int sensitivity = 185;
int value = 0;
int offsetVoltage = 2500;
double voltage = 0;
double currentValue = 0;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(A0, OUTPUT);
//    lcd.begin(16, 2);
//    lcd.print(" Current Sensor ");
//    lcd.setCursor(0,1);
//    lcd.print("  with Arduino  ");
}

void loop() {
  // put your main code here, to run repeatedly:
      value = analogRead(currentPin);
      voltage = (value / 1024.0) * 5000;
      currentValue = ((voltage - offsetVoltage) / sensitivity);
      
      Serial.print("Raw Sensor Value = " );
      Serial.print(value);

//      lcd.clear();
      delay(2000);

//      lcd.setCursor(0,0);
//      lcd.print("RAW Value =     ");
//      lcd.setCursor(12,0);
//      lcd.print(adcValue);
//      delay(2000);
      
      Serial.print("\t Voltage(mV) = ");
      Serial.print(voltage,3);         //3 specifies precesion

      
      delay(2000);
//      lcd.setCursor(0,0);
//      lcd.print("V in mV =       ");
//      lcd.setCursor(10,0);
//      lcd.print(adcVoltage,1);
//      delay(2000);
      
      Serial.print("\t Current(mA) = ");
      Serial.println(currentValue,3);

//      lcd.setCursor(0,0);
//      lcd.print("Current =       ");
//      lcd.setCursor(10,0);
//      lcd.print(currentValue,2);
//      lcd.setCursor(14,0);
//      lcd.print("A");

      delay(2500);
}
