# ET-Collar
Electronic Tracking Collar


# Purpose:

ET-Collar is a deivce designed to securely clip on your pet's collar that will track down pet's location and ststua weather or not its moving or not, how much light your pet likes to stay in. Device gives you peace of mind to know your dog or cat is anytime.

# Component Requirements:

In order to build this project these are the essential components that you need:

- [x] Raspberry pi
- [x] TSL2561 Lux/Light Sensor
- [x] Acclerometer
- [x] GPS device to track location 
- [x] Jumper wires and breadboard to test out temporary circuit 
- [x] PCB board with final circuit printed on it with correct <b>address</b>
- [x] Socket Header to attach sensor and pi together on PCB
- [x] Case to hold ciruit together and prevent it from damage 

## Overall Budget will be approxmately as below:

| Component          | Cost   |
| :------------:     | :-----:| 
| TSL2561            | $9.99  |
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

At this point you should have your pi ready working first we need to do is to check address and functionality of sensor used in the project. How you first connect sensor through wires to check the correct address 
