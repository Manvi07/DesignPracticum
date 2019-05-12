int offset = 10;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
      int volt = analogRead(A0);// read the input
      double voltage = map(volt,0,1023, 0, 25000) + offset;
      voltage = voltage/1000;
      Serial.print("Voltage: ");
      Serial.print(voltage);//print the voltge
      Serial.println("V");
} 
