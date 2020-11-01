import numpy as np
import matplotlib.pyplot as plt

#Define system properties
m = 1.0
k = 25.0
zeta = 0.02 #Damping ratio c/2*sqrt(k*m)

#Frequency range w vector
w = np.arange(1, 10, .1)

#Function to calculate SDOF receptance amplitude
def r_amp(k, m, zeta, w):
    c = 2 * zeta * np.sqrt(k * m)
    return 1/np.sqrt((k - m * w ** 2)** 2 + (w * c)** 2)
    
#Function to calculate SDOF receptance phase angle
def r_phase(k, m, zeta, w):
    c = 2 * zeta * np.sqrt(k * m)
    return np.arctan(- w * c / (k - m * w ** 2))

#Function to set plot properties and showing Bode plot for SDOF system
def plot_RFRF(w, r_amp, r_phase):
    fig, ax = plt.subplots(2, sharex = 'col', sharey = 'row')
    ax[0].plot(w, r_amp)
    ax[1].plot(w, r_phase)
    ax[0].set(ylabel = 'Amplitude (m/N)')
    ax[1].set(ylabel = 'Phase angle (rad)', xlabel = 'Frequency (Hz)', \
              title = "Phase angle vs Frequency", xticks = np.arange(0,11,1))

    plt.text(0.1, 0.9, 'Receptance Amplitude', transform = ax[0].transAxes)
    plt.text(0.1, 0.9, 'Receptance Phase', transform = ax[1].transAxes)
    plt.show()
    
plot_RFRF(w, r_amp(k, m, zeta, w), r_phase(k, m, zeta, w))
