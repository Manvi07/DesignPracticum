import serial

serial_port = '/dev/ttyACM0';
baud_rate = 9600; 
write_to_file = "output.txt";

output_file = open(write_to_file, "w+");
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline();
    line = line.decode("utf-8")                 #ser.readline returns a binary, convert to string
    print(line);
    output_file.write(line);