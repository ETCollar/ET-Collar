from pyrebase import pyrebase
import smbus
import time
import math
from datetime import datetime
from pytz import timezone
from uuid import getnode as get_mac


# defination of firebase connection
config = {
    "apiKey": "AIzaSyCC1VCy28n6ztDLauYS1SPN0suiBPNpnDQ",
    "authDomain": "ecofinder-29360.firebaseapp.com",
    "databaseURL": "https://ecofinder-29360.firebaseio.com",
    "projectId": "ecofinder-29360",
    "storageBucket": "ecofinder-29360.appspot.com",
    "messagingSenderId": "1021640576680"
    }

firebase = pyrebase.initialize_app(config)
dp = firebase.database()
# Get I2C bus
bus = smbus.SMBus(1)

# LIS3DHTR address, 0x18(24)
# Select control register1, 0x20(32)
#		0x27(39)	Power ON mode, Data rate selection = 10 Hz
#					X, Y, Z-Axis enabled
bus.write_byte_data(0x18, 0x20, 0x27)
# LIS3DHTR address, 0x18(24)
# Select control register4, 0x23(35)
#		0x00(00)	Continuous update, Full-scale selection = +/-2G
bus.write_byte_data(0x18, 0x23, 0x00)

time.sleep(0.5)
t=0;
u=0;
sTot=0;

# LIS3DHTR address, 0x18(24)
# Read data back from 0x28(40), 2 bytes
while 1:
    # X-Axis LSB, X-Axis MSB
    data0 = bus.read_byte_data(0x18, 0x28)
    data1 = bus.read_byte_data(0x18, 0x29)
    bus = smbus.SMBus(1)
    # Convert the data
  
    bus.write_byte_data(0x49, 0x00 | 0x80, 0x03) #initilize light sensor readings
    
    data3 = bus.read_i2c_block_data(0x49, 0x0C | 0x80, 2)    #read Light Sensor data
    data4 = bus.read_i2c_block_data(0x49, 0x0E | 0x80, 2)

    xAccl = data1 * 256 + data0
    if xAccl > 32767 :
            xAccl -= 65536
    # LIS3DHTR address, 0x18(24)
     # Read data back from 0x2A(42), 2 bytes
    # Y-Axis LSB, Y-Axis MSB
    data0 = bus.read_byte_data(0x18, 0x2A)
    data1 = bus.read_byte_data(0x18, 0x2B)
    # Convert the data
    yAccl = data1 * 256 + data0
    if yAccl > 32767 :
            yAccl -= 65536
    # LIS3DHTR address, 0x18(24)
    # Read data back from 0x2C(44), 2 bytes
    # Z-Axis LSB, Z-Axis MSB
    data0 = bus.read_byte_data(0x18, 0x2C)
    data1 = bus.read_byte_data(0x18, 0x2D)
    # Convert the data
    zAccl = data1 * 256 + data0
    if zAccl > 32767 :
            zAccl -= 65536
    xAccl2=(xAccl/4)/4096;
    yAccl2=(yAccl/4)/4096;
    zAccl2=(zAccl/4)/4096;
    
    tAccl=math.sqrt(xAccl*xAccl+yAccl*yAccl+zAccl*zAccl)
    v=u+tAccl*t;
    s=((v*v)-(u*u))/(2*tAccl);
    u=v;
    t=5;
    sTot+=s;

    tAccl=math.sqrt(xAccl2*xAccl2+yAccl2*yAccl2+zAccl2*zAccl2)
    print("----------Animal Data-----------")
    print("Total accelaration is: %d" %tAccl)
    
    if tAccl>=1:
        status = "Moving"
    else:
        status = "Idling"
   
     
    print("Status: "+status)

    ch0 = data3[1] * 256 + data3[0]
    ch1 = data4[1] * 256 + data4[0]
    lReading = ch0 - ch1
    
    lux = str(lReading)
    print ("Lux Value :%d lux" %lReading)#light print data

    if lReading >= 1000:
        light = "Sunlight"
    elif (lReading > 100 and lReading < 500):
        light = "Indoor"
    else:
        light = "Dark"
    
    print("Light: "+light)
    nt=datetime.now(timezone('US/Eastern'))
    UpdateTime = nt.strftime("%Y-%m-%d %H:%M:%S")
    location = "43.811657, 79.735212"
    mac = get_mac()
    path = "AnimalData/"+str(mac)
    print("Mac: %d"%mac)
    dp.child(path).update({"Time":UpdateTime, "Status":status, "Lux":lux, "Light":light, "Location":location})
    print(UpdateTime)
    print("\n")

    
    time.sleep(5)
