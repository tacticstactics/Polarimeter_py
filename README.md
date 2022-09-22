# Polarimeter_py

Python code of Mueller matrix dual-rotating retarder polarimeter
https://opg.optica.org/ao/abstract.cfm?uri=ao-31-31-6676

This polarimeter consisis of rotating quarter waveplate, polarizer and photo detector.

1. Polarization State along XY plane
2. Photo detector time domain signal
3. fast Fourir Transform (fft) of photo detector time domain signal
4. Peak Search of fft signal (Under development)


![Figure_1](https://user-images.githubusercontent.com/30459885/191657713-83d6a2b4-ddbe-4aea-b46a-6bc7c83ba059.png)
Figure 1. Typical elliptical polarization

![Figure_2](https://user-images.githubusercontent.com/30459885/191658302-63b957cb-49f8-4d32-b8ab-c1e9f2151e10.png)
Figure 2. Linear Polarization of upward

![Figure_3](https://user-images.githubusercontent.com/30459885/191658382-4db51861-d9d8-4b7c-8aea-66fe3e8eb32e.png)
Figure 3. Linear Polarization of downward

![Figure_4](https://user-images.githubusercontent.com/30459885/191660134-7e7cb4ee-3e56-4d9c-a8aa-2857fd4dbb79.png)
Figure 4. Right handed cicular polarization  

![Figure_5](https://user-images.githubusercontent.com/30459885/191660175-5cd95c25-ad08-4b02-892a-37d91747d789.png)
Figure 5. Right handed cicular polarization  


Analysis:

The time domain sinal consists of two frequency: low frequency f1 and high frequency f2.

Magnitude of f1 and f2 determines ellipcity.

Phase of f1 time domain signal determines semisphere: North or South.

Phase of f2 time domain signal determines azimath of polarization state.


