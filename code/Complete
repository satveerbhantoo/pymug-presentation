# import for api call
import requests 
import json
import time
import matplotlib.pyplot as plt
import datetime

# enabling animations on jupyter notebook
%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'

# initialise a figure
fig = plt.figure()

# adding a subplot
# 1x2 grid at position 1
ax = fig.add_subplot(111)

# show plot
fig.show()


while True:
    x, y, z = [], [], []

    url = ' http://84550860.ngrok.io/readings'
    response = requests.get(url).json()
    
   
    for reading in response:
        x.append(reading['time'])
        y.append(reading['temp'])
        z.append(reading['humidity'])
    
    ax.plot(x, y, color='b')
    ax.plot(x, z, color='r')
    
    plt.xticks(rotation=45, ha='right')
    
    fig.canvas.draw()    
    time.sleep(1)
    
plt.close()
