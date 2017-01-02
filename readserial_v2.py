import serial
import time
import string
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.animation as animation

def read_serial(ser, len):
    while True:
        if ser.inWaiting() > 0:
            break;
        time.sleep(30)
    return ser.read(len)


ser = serial.Serial('COM18', 9600)
time.sleep(0.5)
serial_number = 0






while True:
    ser.flushInput()
    read_serial = ser.readline()
    splitter = read_serial.split()
    try:
        temperature2 = splitter[1];
    except TypeError:
        temperature2 = 0;
    except IndexError:
        temperature2 = 0;
    except ValueError:
        temperature2 = 0;
    
    try:
        humidity2 = splitter[0];
    except TypeError:
        humidity2 = 0;
    except IndexError:
        humidity2 = 0;
    except ValueError:
        humidity2 = 0;

    try:
        temperature4 = splitter[3];
    except TypeError:
        temperature4 = 0;
    except IndexError:
        temperature4 = 0;
    except ValueError:
        temperature4 = 0;
        
    try:
        humidity4 = splitter[2];
    except TypeError:
        humidity4 = 0;
    except IndexError:
        humidity4 = 0;
    except ValueError:
        humidity4 = 0;

    try:
        light1 = splitter[4];
    except TypeError:
        light1 = 0;
    except IndexError:
        light1 = 0;
    except ValueError:
        light1 = 0;

    try:
        soilmoist1 = splitter[5];
    except TypeError:
        soilmoist1 = 0;
    except IndexError:
        soilmoist1 = 0;
    except ValueError:
        soilmoist1 = 0;
      
    #break
    datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    serial_number += 1
    print int(serial_number)
    print datetime
    print 'temperature2 = ',temperature2
    print 'humidity2 = ',humidity2
    print 'temperature4 = ',temperature4
    print 'humidity4 = ',humidity4
    print 'light1 = ',light1
    print 'soilmoist11 = ',soilmoist1
    srfile = open("serialnumber_file.txt","a")
    srfile.write("\n")
    srfile.write(str(serial_number))
    srfile.close()

    t2file = open("temperature2_file.txt","a")
    t2file.write("\n")
    t2file.write(str(temperature2))
    t2file.close()

    h2file = open("humdity2_file.txt","a")
    h2file.write("\n")
    h2file.write(str(humidity2))
    h2file.close()

    t4file = open("temperature4_file.txt","a")
    t4file.write("\n")
    t4file.write(str(temperature4))
    t4file.close()

    h4file = open("humdity4_file.txt","a")
    h4file.write("\n")
    h4file.write(str(humidity4))
    h4file.close()

    l1file = open("light1_file.txt","a")
    l1file.write("\n")
    l1file.write(str(light1))
    l1file.close()

    l1file = open("soilmoist1_file.txt","a")
    l1file.write("\n")
    l1file.write(str(soilmoist1))
    l1file.close()

    dtfile = open("datetime_file.txt","a")
    dtfile.write("\n")
    dtfile.write(str(datetime))
    dtfile.close()


    time.sleep(30)
