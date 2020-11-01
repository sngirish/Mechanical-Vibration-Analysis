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
    ax[0].set(ylabel = 'Amplitude (m)', title = "Amplitude vs Frequency")
    ax[1].set(ylabel = 'Phase angle (rad)', xlabel = 'Frequency (Hz)', title = "Phase angle vs Frequency", xticks = np.arange(0,11,1))
    plt.show()
    
#plot_RFRF(w, r_amp(k, m, zeta, w), r_phase(k, m, zeta, w))

#Function to calculate SDOF mobility amplitude
def m_amp(w, r_amp):
    return w * r_amp

#Function to calculate SDOF inertance amplitude
def i_amp(w, r_amp):
    return (w**2) * r_amp

# Amplitude Bode plots SDOF system
def plot_FRF_amp(w, r_amp, m_amp, i_amp):
    fig, ax = plt.subplots(3, figsize=(9, 12), sharex = 'col', sharey = 'row')
    ax[0].plot(w, r_amp)
    ax[1].plot(w, m_amp)
    ax[2].plot(w, i_amp)
    ax[0].set(ylabel = 'Amplitude (m)', title = "Amplitude vs Frequency")
    ax[1].set(ylabel = 'Amplitude (m/s)')
    ax[2].set(ylabel = 'Amplitude (m/s^2)', xlabel = 'Frequency (Hz)', xticks = np.arange(0,11,1))
    plt.show()
    
plot_FRF_amp(w, r_amp(k, m, zeta, w), m_amp(w, r_amp(k, m, zeta, w)), i_amp(w, r_amp(k, m, zeta, w)))
