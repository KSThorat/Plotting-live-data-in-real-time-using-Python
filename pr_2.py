
import csv  #generation of csv file
import random  #generate random data
import time

#initialization
x_vals=0
total_1=1000
total_2=1000

fieldnames=["x_vals","total_1","total_2"]#headers for csv file

#it will create csv file and write data in the form of dictionary format
with open('data.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

        info = {
            "x_vals":x_vals,
            "total_1":total_1,
            "total_2":total_2
            }
        #shows values in row
        csv_writer.writerow(info)
        #print appended values in this format
        print(x_vals,total_1,total_2)

        #increament by 1
        x_vals +=1
        total_1=total_1+random.randint(-6,8) #for updown variation
        total_2=total_2+random.randint(-5,6)

    time.sleep(1)#suspend execution in 1 sec

        
