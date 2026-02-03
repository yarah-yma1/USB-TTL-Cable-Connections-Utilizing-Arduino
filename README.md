# USB-TTL-Cable-Connections-Utilizing-Arduino
# Arduino Dual Serial Communication with Python on Macbook

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
- [Build of Materials](#build-of-materials)
- [Experimental Procedure](#experimental-procedure)
- [Results](#results)
- [Discussion](#discussion)
- [References](#references)

## Introduction
This project demonstrates dual serial communication using an Arduino Uno through both USB (hardware serial) and a TTL adapter (software serial). Python scripts are used to identify and read data from one or multiple serial ports simultaneously, enabling external data monitoring without relying on the Arduino IDE Serial Monitor.

## Background
Serial communication is a fundamental method for transmitting data between microcontrollers and external devices. The Arduino Uno features a single hardware serial interface over USB, but additional serial ports can be implemented using the SoftwareSerial library. Python, through the PySerial library, enables real time serial data acquisition for analysis and debugging outside of embedded development environments.

## Build of Materials
- Arduino Uno
- USB Type-B cable
- TTL-to-USB serial adapter
- Jumper wires
- Computer with Python 3 installed
- VS Code

## Experimental Procedure
First step is to open up arduino ide. Create a new sketch and paste in the code found in the src folder. Afterwards open a new sketch and paste the same code. You should have two sketches up at the same time. One will be for the TTL and the other will be for USB cable. 

### Wiring and Connections
Connect the arduino uno board to the computer one side through the standard usb and the other side through the ttl side. In the directions below it will show the wiring for the arduino uno with the ttl cable. 

### Wiring Diagram
Here is the general wiring of how the arduino and ttl cable should interact [1]. It is important to note be sure to place the ttl in pins 2,3 as 0,1 is the standard use for the usb cable and the code wont be able to run both at the same time on the same pins. 
<img width="993" height="412" alt="image" src="https://github.com/user-attachments/assets/c04120d3-758b-4c5a-b012-c240973c5b4b" />
Below is a general idea of what the colors represent on a standard ttl cable.
<img width="895" height="555" alt="image" src="https://github.com/user-attachments/assets/4023c3fa-3a94-4f0c-846a-d00024cb062b" />

### Arduino Duties 
Now after you have everything connected correctly you will run the code. Make sure to select two different ports for each sketch up, one for the usb and one for the ttl. Go ahead and click upload. As soon as the comling of the code is done and you see the word "uploading" immediately click the button. This may take a couple trys, but afterwards the code will be uploaded and it should work, showing that one side is the usb communicating and the other side is the ttl comunicating. 
#### The image below represents what your screen should look like after implementing the steps above.
<img width="1168" height="661" alt="image" src="https://github.com/user-attachments/assets/88b8178a-944e-4edb-b6a6-40ce3f86301b" />

#### REST OF README WILL BE FINISHED SOON



