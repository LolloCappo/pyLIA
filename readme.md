Digital lock-in analysis
---------------------------------------------

Perform digital lock-in analysis


Simple examples
---------------

Here is a simple example on how to use the code:

	pip install pyLIA

	import numpy as np
	import matplotlib.pyplot as plt
	import pyLIA

	data = np.load('camera.npy') ## Thermal acquisition
	sampling_freq = 400  ## Sampling freqency of the thermal video [Hz]
	load_freq = 55  ## Load freqency of the excitation test [Hz]

	mag, ph = pyLIA.LIA(data,sampling_freq,load_freq)

	plt.figure()
	plt.imshow(mag)
	cbar = plt.colorbar()
	cbar.set_label('[unit]')

	plt.figure()
	plt.imshow(ph)
	cbar = plt.colorbar()
	cbar.set_label('[deg]')
    

Reference:

Non-stationarity index in vibration fatigue: Theoretical and experimental research; L. Capponi, M. Česnik, J. Slavič, F. Cianetti, M. Boltežar; International Journal of Fatigue 104, 221-230
https://www.sciencedirect.com/science/article/abs/pii/S014211231730316X
