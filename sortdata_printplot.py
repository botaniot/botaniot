
from numpy import loadtxt
import time
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mp
import matplotlib.dates as mdates
import datetime as dt
import dateutil.parser

import dropbox

#plt.ion()

while True:
    newtime = []
    newdate = []
    newdatetime = []
    datetime = loadtxt("datetime_file.txt", dtype='string',skiprows=1)
    temperature2data = loadtxt("temperature2_file.txt", dtype='float',skiprows=1)
    temperature4data = loadtxt("temperature4_file.txt", dtype='float',skiprows=1)
    light1data = loadtxt("light1_file.txt", dtype='float',skiprows=1)
    soilmoist1data = loadtxt("soilmoist1_file.txt", dtype='float',skiprows=1)  

    for i in np.arange(0,len(datetime),1):
        newtime.append(dateutil.parser.parse(datetime[i,1]))
        newdate.append(dateutil.parser.parse(datetime[i,0]))
        newdatetime.append((dt.datetime.combine(((dateutil.parser.parse(datetime[i,0]))),((dateutil.parser.parse(datetime[i,1]).time())))))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharey=False)
    fig.autofmt_xdate()
    ax1.plot(newdatetime, temperature2data, color='blue', label = 'Temperature 2')
    ax2.plot(newdatetime, temperature4data, color='green', label = 'Temperature 4')
    ax3.plot(newdatetime, light1data, color='orange', label = 'Light 1')
    ax4.plot(newdatetime, soilmoist1data, color='purple', label = 'Soil Moisture %')
    ax1.legend(loc='best', ncol=1, fontsize=10)
    ax2.legend(loc='best', ncol=1, fontsize=10)
    ax3.legend(loc='best', ncol=1, fontsize=10)
    ax4.legend(loc='best', ncol=1, fontsize=10)
    xfmt = mdates.DateFormatter('%d/%m %H:%M')

    ax4.xaxis.set_major_formatter(xfmt)
    ax1.set_ylabel('Temperature [C]', size = 10)
    ax2.set_ylabel('Temperature [C]', size = 10)
    ax3.set_ylabel('LDR Resistance', size=10)
    ax4.set_ylabel('Soil Moisture %', size=10)
    ax1.grid()
    ax2.grid()
    ax3.grid()
    ax4.grid()
    newdatetimestring = str(newdatetime[len(newdatetime)-1])
    fig.suptitle('BotanIot.github.io | Pushkar Sheth | HAPPY NEW YEAR 2017!!', fontsize=12)
    ax1.set_title('Update mode: Suspended | Last updated: '+newdatetimestring, fontsize = 10, color = 'blue')
    plt.xticks(fontsize = 8, rotation='vertical')

    plt.savefig('botaniotmonitor.png')
    print('saved to botaniotmonitor.png at '+newdatetimestring)
    client = dropbox.client.DropboxClient('69fnaXVMw2AAAAAAAAAADiXW9ZyNARY3guJlucKOPQAqJhCrNmh2shEkd-nSjMEh')
    print 'linked account: ', client.account_info()
    f = open('botaniotmonitor.png', 'rb')
    response = client.put_file('/Apps/biot1/botaniotmonitor.png', f, overwrite = True)
    print('uploaded!')
    time.sleep(1800)

    plt.close()



