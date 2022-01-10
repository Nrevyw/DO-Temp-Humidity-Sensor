import io
import sys
import csv
from matplotlib import pyplot
import codecs

## Collect Data from OM-24


# CHANGE DIRECTORY
contents = csv.reader(codecs.open(r"C:\Users\bhaveshtrayakshara\Desktop\OM-24.csv", 'rU', 'utf-16'))

listform = []
for line in contents:
    listform.append(line)

a = 'Index'
i=-1

for line in listform:
    i = i+1
    string = ''.join(line)
    stringsplit = string.split('\t')
    if a==stringsplit[0]:
        start = i+1
        break


reldata = listform[start:]
reldatastr = []

time = []
temp = []
hum = []

for x in reldata:
    row = ''.join(x)
    rowsplit = row.split('\t')
    time.append(rowsplit[2])
    temp.append(float(rowsplit[4]))
    hum.append(float(rowsplit[6]))


## Compile with Arduino Data

# CHANGE DIRECTORY
with open(r"C:\Users\bhaveshtrayakshara\templog.csv", "r") as log:
    templog = log.readlines()

atime = []
atemp = []

for aline in templog:
    astringsplit = aline.split(',')
    atime.append(astringsplit[0])
    atemp.append(float(astringsplit[1]))

pyplot.close('all')

fig, ax = pyplot.subplots(nrows = 2,ncols = 1)
ax[0].plot(atime, atemp, 'b-',label = 'Arduino Temperature')
ax[0].plot(time, temp, 'r-',label = 'OM-24 Temperature')
ax[0].legend(loc="upper right")
ax[1].plot(time, hum, 'g+',label = 'OM-24 Humidity')
ax[1].legend(loc="upper right")

ax[0].set_title('Temperature Sensors')
ax[0].set(xlabel='Time (Mountain Standard Time)', ylabel='Temperature (deg C)')

ax[1].set_title('Humidity Sensor')
ax[1].set(xlabel='Time (Mountain Standard Time)', ylabel='%RH')

fig.tight_layout(pad=3.0)
plt.show()


