# ET-Collar
Electronic Tracking Collar


# Purpose:

ET-Collar is a deivce designed to securely clip on your pet's collar that will track down pet's location and ststua weather or not its moving or not, how much light your pet likes to stay in. Device gives you peace of mind to know your dog or cat is anytime.

# Component Requirements:

In order to build this project these are the essential components that you need:

- [x] Raspberry pi
- [x] TSL2561 Lux/Light Sensor
- [x] Acclerometer / LIS3DH
- [x] GP-20U7 GPS device to track location 
- [x] Jumper wires and breadboard to test out temporary circuit 
- [x] PCB board with final circuit printed on it with correct <b>address</b>
- [x] Socket Header to attach sensor and pi together on PCB
- [x] Case to hold ciruit together and prevent it from damage 

## Overall Budget will be approxmately as below:

| Component          | Cost   |
| :------------:     | :-----:| 
| Light Sensor       | $9.99  |
| Accelormeter       | $12    |
| GPS                | $80.0  |
| Raspberry pi       | $116.99|
| wires and sockets  | $0.00  |
| soldering iron     | $0.00  |
| softwares required | $0.00  |
| Parts kit          | $0.00  |

For me most of the components were provided by Humber College it costed me around $218.98

## Time Commitment 

Before we start it is important to make a schedule to keep us on track that will help us to check if everything is going as planed. 
Keep on checking if there were any delays and try to work accordingly.

# TIME/ SCedule ---


# Setup raspberry pi

Once you have got your raspberry pi start working on its functionality download required operating System and allow all the permissions required. if you're first time installing os on raspberry pi and don't know how to do it follow these setps:

---
### Setting up Raspberry Pi
After receiving the order, the first step is installing Raspian on Raspberry Pi.These are the steps for installation as given below:-

#### Step 1: Download Raspbian
It can easily take more than half an hour to download the software.Download Noobs from https://www.raspberrypi.org/downloads/ 

#### Step 2: Unzip the file
The Raspbian disc image is compressed, so you’ll need to unzip it. The file uses the ZIP64 format, so depending on how current your built-in utilities are, you need to use certain programs to unzip it.

#### Step 3: Write the disc image to your microSD card
Select the drive of your SD card in the ‘Device’ dropdown.

#### Step 4: Put the microSD card in your Pi and boot up
Select ‘Write’ and wait for the process to finish which may take around 20 minutes to complete.

---

# Hardware Setup

At this point you should have your pi ready working first we need to do is to check address and functionality of sensor used in the project. How you first connect sensor through wires to check the correct address. After you have conformed the I2C address for sensors  you can design Printed circuit board to the connect all the senosrs together for convence.

Check the address for sensors:

### Light Sensor
![c](https://user-images.githubusercontent.com/43556409/49120745-e9ab0a80-f27b-11e8-8392-84376b9dc8cc.jpeg)

### Acclerometer


### GPS


# PCB and Soldring

You can use fritizing software to design your PCB. If you don't know how to use fritizing you can use help from their website:
http://fritzing.org/learning/

The wires that are yellow in colour are on the top side of the board and orange ones are at the bottom. It is important not to cross two wires on the same side of board or in other words are in same colour. Note both sensor and Rpi should be soldered on each side of the board. Also, make sure all the wires that are touching the pi pins are to be soldered on top side hence should be same in colour same(yellow) and for sensor pins are going to be at bottom.


Next step is to get your PCB board made once you have got your PCB ready carefully solder socket headers to the PCB you have to very carefull.
Safety is the first priority so it is important to know what are you working with. If you haven't done soldering before you should get  help from someone with experience or from youtube videos.
For above design I have this PCB should look like this.


After that you can just attached your sensor and raspberry pi to PCB. Make sure all the wires are connected and your sensor is at the correct address.

# Get Data/Sensor Readings

So at this point you should have your raspberry pi and sensor ready to use to read data. To get data from sensor and display it in human readable form we have ro run a script you can program that in java/c/python. Here i am ruuning this python code over here.

```
CODE HERE

```

# Software Setup

# Firebase

[here] !https://github.com/ETCollar/ET-Collar/blob/master/Database%20structure/ecofinder-29360-export.json

# Data Display

If you run the above script you should be able to get readings on screen......



You can test sensor by changeing the reading for example use your phone's flash light to raise and cover it by your hand to decrease the amount of light on your sensor.



