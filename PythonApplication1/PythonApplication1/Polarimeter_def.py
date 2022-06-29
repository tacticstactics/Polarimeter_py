#Polarimeter_def.py


import numpy as np


def proc1(param=0.01,m=256):


    tcol = np.zeros((m,1)); # time
    
    Etcol = np.ones(m, dtype=complex);#*2

       
    Signalcol = np.ones(m, dtype=complex);#*2


    freq = 4
    omega = 2*np.pi*freq
 
    print('omega=', omega, 'Hz')

    #Pulsewidth
    tau = 0.4 

    # PD signal. Proportional to optical power
    #Signal = 0


    for ii in range(m):


        delay1 = 0.025*ii-1.6      

        s = 0
        
        for jj in range(m):

            time1 = 0.025*jj-1.6
            tcol[(jj)] = time1
            
            Et = np.exp(1j * omega * time1) * np.exp(-1.38 * (time1/tau)**2)
            
            Etcol[(jj)] = Et
            
            #Et = math.sin(omega * time1)     
            

            td = time1 + delay1

            Etd = np.exp(1j * omega * td) * np.exp(-1.38 * (td/tau)**2)                          
     

            s += (abs(Et+Etd)**2)**2            

              #Signalcol[(ii)] = Etd
            Signalcol[(ii)] = s

                    #print(Signalcol)

    return tcol, Etcol,Signalcol


