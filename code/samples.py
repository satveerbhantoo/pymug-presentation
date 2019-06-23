import requests 
import json 
import time
import matplotlib.pyplot as plt
import random
import requests 
import json 


%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()


while True:
    x, y = [], []

    url = ' http://84550860.ngrok.io/readings'
    response = requests.get(url).json()
    
   
    for reading in response:
        x.append(reading['time'])
        y.append(reading['temp'])
    print(x)
    print(y)
    
    ax.plot(x, y, color='b')
    
    plt.xticks(rotation=45, ha='right')
    fig.canvas.flush_events()
    fig.canvas.draw()    
    time.sleep(1)
    
plt.close()




//mpl
import requests 
import json 
import time
import matplotlib.pyplot as plt
import random
import requests 
import json 


%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
plt.ion()

while True:
    x, y = [], []

    url = ' http://84550860.ngrok.io/readings'
    response = requests.get(url).json()
    
   
    for reading in response:
        x.append(reading['time'])
        y.append(reading['temp'])
        ax.plot(x, y, color='b')   
    
    plt.xticks(rotation=45, ha='right')
    fig.canvas.flush_events()
    fig.canvas.draw()    
    time.sleep(1)
    
plt.close()














import time
import matplotlib.pyplot as plt
import random
import requests 
import json 


%matplotlib notebook
plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0
x, y = [], []

while True:
    x.append(i)
    y.append(random.randint(1,101))
    
    ax.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    ax.set_xlim(left=max(0, i-50), right=i+50)
    
    time.sleep(0.1)
    i += 1
    
plt.close()


import requests 
import json 

url = 'http://1233d94b.ngrok.io/readings'
response = requests.get(url).json()
print(response)
