import serial

ser1 = serial.Serial('/dev/cu.usbmodem11101', 9600, timeout=1)
ser2 = serial.Serial('/dev/cu.usbserial-1130', 9600, timeout=1)

try:
    while True:
        if ser1.in_waiting > 0:
            line = ser1.readline().decode('utf-8').rstrip()
            print(f"port1: {line}")
        
        if ser2.in_waiting > 0:
            line = ser2.readline().decode('utf-8').rstrip()
            print(f"port2: {line}")
            
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser1.close()
    ser2.close()
