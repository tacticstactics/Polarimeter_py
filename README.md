# Polarimeter_py


https://github.com/user-attachments/assets/4ffc6628-28ac-45f0-9c63-f8f451fef694


Python code of Mueller matrix dual-rotating retarder polarimeter

https://opg.optica.org/ao/abstract.cfm?uri=ao-31-31-6676

This polarimeter consisits of three elements:

1) rotating quarter waveplate
2) polarizer
3) photo detector.

Photo detector signal is fourier transformed. After transformation, azimath and phase of polarized light are calculated using amplitude and phase of frequency signals.

Below are calculation results.

From Left to Right:
1. Polarization State in XY plane
2. Photo detector time domain signal
3. Fast Fourir Transform (fft) of photo detector time domain signal
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
Figure 5. Left handed cicular polarization  


Analysis:

The time domain sinal consists of two frequency: low frequency f1 and high frequency f2.

Magnitude of f1 and f2 determines ellipcity.

Phase of f1 time domain signal determines semisphere: North or South.

Phase of f2 time domain signal determines azimath of polarization state.

![Figure_2](https://user-images.githubusercontent.com/30459885/225231663-54c264f6-09fc-497e-a0ba-1fb88e7feb9e.png)

Poincaré sphere









