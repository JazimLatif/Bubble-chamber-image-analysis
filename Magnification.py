#Use the zoom.py code to work out the zoom on your screen
#the alpha and beta constants were first calculated for our whiteboard working
#the zoom program converts the whiteboard zoom to other devices so the constants can be reused
alpha=1.2208
beta=0.0115
Sevent=input("Please enter the shift in event (cm):")
Slfm=input("Please enter the shift in large fiducial marker (cm):")
z=(Sevent/Slfm)*31.6
Magnification=alpha+(beta*z)
print("The magnification on the image is:",Magnification)