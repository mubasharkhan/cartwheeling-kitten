
import numpy as np
import matplotlib.pyplot as plt


#f_name = input("Enter your first name: ")
#l_name = input("Enter your last name: ")

#print("Your full name is {} {}".format(f_name,l_name))

x = np.linspace(0,2*np.pi,50)
y = np.cos(x)
y1=np.sin(x)
y2=np.sin(np.pi/2+x)


plt.figure()
plt.plot(x,y,'bo-',linewidth = 2.0)
plt.hold('on')
plt.plot(x,y1,'r-',linewidth=2.0)
plt.plot(x,y2,'g-',linewidth=2.0)
