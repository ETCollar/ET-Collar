# ET-Collar
Electronic Tracking Collar


# Purpose:

ET-Collar is a device designed to be clipped on your pet's collar that will track down pet's location and status whethere or not its moving or not, the kind of lighiting your pet likes. Device gives you the possibility to track your dog/cat so anyone can be more relaxed knowing where their loved pets are.

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

The overall time taken to complete the hardware part was 15 hours, to complete the android application it took around 30 hours spanned in 4 months
However, if anyone wants to replicate the project it should take no longer than seven hours to complete, of course all the required materials should be by hand.
Moreover, the estimated completion time consider that the source code, PCB design, instruction for DB set up and android application are provided and working. If changes are made, more time needs to be added for the completion of the project.

# Setup raspberry pi

Once you have got your raspberry pi. Start working on its functionality, download required operating System and allow all the permissions required. If it is the first time installing OS on raspberry pi and do not know how to do it follow these steps:

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

At this point you should have your pi ready and working. First we need to do is to check address and functionality of the sensors used in the project. So first connect your sensor through wires to the PI in order to check the correct address. After you have confirmed the I2C address for sensors  you can design Printed circuit board and connect all the senosors together together through PCB.

# PCB and Soldring

You can use fritizing to design your PCB. If you don't know how to use fritizing you can follow the guidelines on this website:
http://fritzing.org/learning/

The wires that are yellow are on the top side of the board and orange ones are at the bottom. It is important not to cross two wires on the same side of board or in other words are in same colour. Note both sensor and Rpi should be soldered on each side of the board. Also, make sure all the wires that are touching the PI pins are to be soldered on top side hence: should be same in colour same(yellow) and for sensor pins are going to be at bottom.
[gerber.zip](https://github.com/ETCollar/ET-Collar/files/2946933/gerber.zip)

![thumbnail](https://user-images.githubusercontent.com/47256700/54046513-9150a680-41a2-11e9-82ff-e4f8a9e4a066.png)

Next step, once the PCB is board is available, is to carefully solder socket headers to the PCB you have to be very carefull.
Safety is the first priority so it is important to know what are you working with. If you haven't done soldering before you should get  help from someone with experience or from youtube videos.
For above design PCB should look like this.
Bottom Side

![bottom](https://user-images.githubusercontent.com/47256700/54046880-9b26d980-41a3-11e9-9bf9-af228a05244b.png)

Top Side

![top](https://user-images.githubusercontent.com/47256700/54046888-9e21ca00-41a3-11e9-9080-d36badd45084.png)



After that you can just attached your sensor and raspberry pi to PCB. Make sure all the wires are connected and your sensor is at the correct address.

Connect sensors to PCB and to RPI as well.


![pcb](https://user-images.githubusercontent.com/47256700/54047013-ee009100-41a3-11e9-8dae-4faf894e930e.png)


# Get Data/Sensor Readings

So at this point you should have your raspberry pi and sensor ready to use to read data. To get data from sensor and display it in human readable form we have ro run a script you can program that in java/c/python. Here i am ruuning this python code over here.

```
CODE HERE

```



# Software Setup

The overall time taken to complete the hardware part was 15 hours, to complete the android application it took around 30 hours spanned in 4 months
However, if anyone wants to replicate the project it should take no longer than seven hours to complete, of course all the required materials should be by hand.
Moreover, the estimated completion time consider that the source code, PCB design, instruction for DB set up and android application are provided and working. If changes are made, more time needs to be added for the completion of the project.


# Firebase

[Database Structure](https://github.com/ETCollar/ET-Collar/blob/master/Database%20structure/ecofinder-29360-export.json)

## Create new Firebase Project 

![image](https://user-images.githubusercontent.com/47256700/54047180-69624280-41a4-11e9-89e8-a317544acf44.png)

![image](https://user-images.githubusercontent.com/47256700/54047193-6d8e6000-41a4-11e9-9a4b-d3b7296a5a9c.png)

![image](https://user-images.githubusercontent.com/47256700/54047200-72ebaa80-41a4-11e9-944d-52072ed78a28.png)

![image](https://user-images.githubusercontent.com/47256700/54047211-7848f500-41a4-11e9-9a68-e270f442f402.png)

![image](https://user-images.githubusercontent.com/47256700/54047218-7bdc7c00-41a4-11e9-9378-1be089cc4a7d.png)

![image](https://user-images.githubusercontent.com/47256700/54047231-8139c680-41a4-11e9-916f-9833e56e531d.png)

![image](https://user-images.githubusercontent.com/47256700/54047236-86971100-41a4-11e9-93ec-b805e4388f9d.png)

![image](https://user-images.githubusercontent.com/47256700/54047244-8e56b580-41a4-11e9-908e-12082a1f2cad.png)



# Data Display

If you run the above script you should be able to get readings on the screen......

# Android App display

If everything is working fine you should get following screen on APP
Select Status it will ask you to choose devices that are added to your account.

![astatus](https://user-images.githubusercontent.com/47256700/54047821-18534e00-41a6-11e9-88f9-05385f572abb.png)

After you have selected you device's MAC address press get data to display data.

![status](https://user-images.githubusercontent.com/47256700/54047820-18534e00-41a6-11e9-979c-5903e3b3794e.PNG)

Press map button to show animal's position on map

![map](https://user-images.githubusercontent.com/47256700/54047819-18534e00-41a6-11e9-9592-5b36784b9a2b.png)



You can test sensor by changeing the reading for example use your phone's flash light to raise and cover it by your hand to decrease the amount of light on your sensor.



