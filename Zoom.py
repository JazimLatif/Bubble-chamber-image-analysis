  
#To calculate the adobe acrobat reader DC zoom
#Open image BubblePrint_97430049_A0
#Zoom in 66.7% and look at the fiducial markers next to the Sigma- decay to a pi+
shift=input("Please enter the shift in fiducial marker(cm):")
zoomMultiplyer=20.2/shift
AcrobatZoom=66.7*zoomMultiplyer
print("Set adobe Acrobat Reader to:",AcrobatZoom)