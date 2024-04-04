#PLOTTING LIVE DATA IN REAL-TIME
#The live plotting function is capable of producing high-speed , high-quality , real-time data visualization in Python
#For example
# 1)social media data
# 2)Audio data 
# 3)Stock market data
# 4)Temperature data
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation  # It will repeatedly call our function to refresh the chart

plt.style.use('fivethirtyeight')#Provide style to a graph


index=count()#Give next value after count a number of each time

#Function to update the data
def animate(i):
    data=pd.read_csv('data.csv')#it will read data from csv file
    #accessing values
    x=data['x_vals']
    y1=data['total_1']
    y2=data['total_2']
   
    #clear axis
    plt.cla()

    #define and adjust graph
    plt.plot(x,y1,label='channel 1')
    plt.plot(x,y2,label='channel 2')

    plt.title("Plotting of live data in Real-Time")
    #locate the label of graph at given location
    plt.legend(loc='upper left')
    #padding in animation
    plt.tight_layout()

#animate
ani=FuncAnimation(plt.gcf(),animate,interval=1000)
#.gcf() will give current figure,animate-function which is we wanted to run,interval-set an interval of 1000 milisec at FuncAnimation

#for some padding
plt.tight_layout()
#shows the plot
plt.show()
