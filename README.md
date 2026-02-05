# USB-TTL-Cable-Connections-Utilizing-Arduino
# Arduino Dual Serial Communication with Python on Macbook

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
- [Build of Materials](#build-of-materials)
- [Experimental Procedure and Results](#experimental-procedure-and-results)
- [Discussion](#discussion)
- [References](#references)

## Introduction
This project demonstrates dual serial communication using an Arduino Uno through both USB (hardware serial) and a TTL adapter (software serial). Python scripts are used to identify and read data from one or multiple serial ports simultaneously, enabling external data monitoring without relying on the Arduino IDE Serial Monitor. This tutorial will consist of 2 parts. The first part will consist of reading in from one port the USB hardware serial and the second part will consist of running both a TTL and USB serial.

## Background
Serial communication is a fundamental method for transmitting data between microcontrollers and external devices. The Arduino Uno features a single hardware serial interface over USB, but additional serial ports can be implemented using the SoftwareSerial library. Python, through the PySerial library, enables real time serial data acquisition for analysis and debugging outside of embedded development environments.

## Build of Materials 
- Arduino Uno
- USB Type-B cable
- TTL-to-USB serial adapter
- Jumper wires
- Computer with Python installed + Arduino IDE
- VS Code

## Experimental Procedure and Results
First step is to open up arduino ide. Create a new sketch and paste in the code found in the src folder named serialMonitorTest.ino. For the first part you will run the code with the hardware serial the USB cable. 
For the second part you will open a new sketch and paste the same code. You should have two sketches up at the same time. One will be for the TTL and the other will be for USB cable. 

### Wiring and Connections
Connect the arduino uno board to the computer one side through the standard usb and the other side through the ttl side (for second part of experiment). In the directions below it will show the wiring for the arduino uno with the ttl cable. 

### Wiring Diagram
Here is the general wiring of how the arduino and ttl cable should interact [1]. It is important to note be sure to place the ttl in pins 2,3 as 0,1 is the standard use for the usb cable and the code wont be able to run both at the same time on the same pins. 
<img width="993" height="412" alt="image" src="https://github.com/user-attachments/assets/c04120d3-758b-4c5a-b012-c240973c5b4b" />
Below is a general idea of what the colors represent on a standard ttl cable [2].
<img width="895" height="555" alt="image" src="https://github.com/user-attachments/assets/4023c3fa-3a94-4f0c-846a-d00024cb062b" />

### Arduino Duties 
Now after you have everything connected correctly you will run the code. Make sure to select two different ports for each sketch up, one for the usb and one for the ttl (for part two, you can do the following step with just the usb cable for part one and then repeat the steps to do part two with two sketches). Go ahead and click upload. As soon as the compling of the code is done and you see the word "uploading" immediately click the button. This may take a couple trys, but afterwards the code will be uploaded and it should work, showing that one side is the usb communicating and the other side is the ttl comunicating. 
#### The image below represents what your screen should look like after implementing the steps above (results).
<img width="1168" height="661" alt="image" src="https://github.com/user-attachments/assets/88b8178a-944e-4edb-b6a6-40ce3f86301b" />

### Checking In Python 
To confirm three Python files have been provided to interface with the serial connection. Run the python scripts listed below in a python terminal. The scripts are found in the src folder. 
- loopCOM.py --> loop through all COM ports to see what’s on them
- readCOM.py –-> read a specific, target COM port
- twoCOM.py –-> read two COM ports
#### The images below shows the outputs/results of the following scripts. 
- This one is for the loopCOM.py in which it confirms the port names. 
-- <img width="488" height="164" alt="image" src="https://github.com/user-attachments/assets/6858026d-639d-4458-a507-eb2b03ccafc6" />
- This one is for readCOM.py in which it confirms that a specific port is being read 
-- <img width="489" height="103" alt="image" src="https://github.com/user-attachments/assets/d761a1b9-51bd-4feb-adfc-1a036af0d491" />
- This one is for twoCOM.py in which it confirms both ports are being read, in the image serial is usb and serial1 is through ttl.
-- <img width="497" height="86" alt="image" src="https://github.com/user-attachments/assets/988d5b3a-3a72-43c1-b7d7-887a3442c774" />
## Discussion
It is important to understand serial communication is exptremly important when utlizing microcontrollers in projects. The project shows that an arduino uno can sucessfuly implement a dual serial communication by putting serial hardware and serial software together through utlizing a ttl cable and usb. There was also a sucessful use of python through serial communication confirming through various checks. Overall, the project sucessfully shows dual serial communication through an arduino uno is possible!
## References 







