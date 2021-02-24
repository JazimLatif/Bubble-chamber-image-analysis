#import required libraries
import mod_helium4_phys352 as he4
import numpy as np

Pressures_mbar = np.array([900,800,700,600,625,650,610,590,625,620,615,610,605,600,595,590,585])
TemperaturesK = he4.temperature_from_pressure_SVP(Pressures_mbar*1.0e2)
for tempindex in range(len(Pressures_mbar)):
    print('%s %.2f %s %s %.2f %s'%('At pressure of ', Pressures_mbar[tempindex],'mbar', 'temperature is: ', TemperaturesK[tempindex], 'K'))