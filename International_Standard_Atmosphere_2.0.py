import matplotlib.pyplot
#Temperature gradient values in Kelvin per metre:
a_val=[-0.0065,0,0.0010,0.0028,0,-0.0028,-0.0020,0]
#[Troposphere, Tropopause, First part of Stratosphhere, Second part of
# Stratosphere, Stratopause, First part of mesosphere, Second part of 
# Mesosphere, Mesopause]

#ISA at sea level:
Pi=101325   #Pascals
Di=1.225    #Kg per cubic metre    
Ti=288.15   #Kelvin

#Constants:
g=9.80665   #Acceleration due to gravity   
R=287.0     #Molar gas constant for air
e=2.71828   #Euler's constant

#Altitudes
alt=[11000,20000,32000,47000,51000,71000,84000,90000,0]
#[Troposphere, Tropopause, First part of Stratosphhere, Second part of
# Stratosphere, Stratopause, First part of mesosphere, Second part of 
# Mesosphere, Mesopause, Sea level]

#variables
Pf,Tf,Df = 0,0,0
#Pressure final, Temperature final, Density final

counter = 0

def sphere(h,Pi,Di,Ti):
    global counter,a_val,Pf,Tf,Df
    if h>alt[counter]:
        x=alt[counter]
    else:
        x=h
    a=a_val[counter]
    exp=-g/(R*(a))
    Tf=Ti+a*(x-alt[counter-1])
    Pf=Pi*((Tf/Ti)**exp)
    Df=Pf/(R*Tf)
    if h>alt[-2]:
        print("Altitude out of range")
    elif h>alt[counter]:
        if counter in [0,3,6]:
            counter+=1
            pause(h,Pf,Df,Tf)
        else:
            counter+=1
            sphere(h,Pf,Df,Tf)
    else:
        return (Pf,Df,Tf)

def pause(h,Pi,Di,Ti):
    global counter,a_val,Pf,Tf,Df
    if h>alt[counter]:
        x=alt[counter]
    else:
        x=h
    Tf=Ti
    exp=(-(g*(x-alt[counter-1]))/(R*Tf))
    Pf=Pi*(e**exp)
    Df=Pf/(R*Tf)
    if h>alt[-2]:
        print("Altitude out of range")
    elif h>alt[counter]:
        if counter in [0,3,6]:
            counter+=1
            pause(h,Pf,Df,Tf)
        else:
            counter+=1
            sphere(h,Pf,Df,Tf)
    else:
        return (Pf,Df,Tf)

'''
h=int(input("Enter Altitude (metres): "))
sphere(h,Pi,Di,Ti)

print("Pressure: ",Pf," Pascals")
print("Temperature: ",Tf," Kelvin")
print("Air Density: ",Df," Kg/m^3")
'''
#h = int(input("Enter Altitude (metres): "))
h=90000
height=[]
temperature=[]
pressure=[]
density=[]
for i in range(h):
    counter=0
    sphere(i,Pi,Di,Ti)
    height.append(i)
    temperature.append(Tf)
    density.append(Df*240) #constant for scaling
    pressure.append(Pf/347) #constant for scaling

axes = matplotlib.pyplot.gca()
axes.set_xlabel('Altitude in metres')
axes.set_ylabel('Temperature, Pressure, Air Density')  
matplotlib.pyplot.plot(height,temperature)
matplotlib.pyplot.plot(height,pressure)
matplotlib.pyplot.plot(height,density)
matplotlib.pyplot.show()


