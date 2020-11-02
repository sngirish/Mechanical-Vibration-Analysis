import numpy as np
import matplotlib.pyplot as plt


#Define system properties
m = 1.0
k = 25.0
zeta = 0.02 #Damping ratio c/2*sqrt(k*m)

#Frequency range w vector
w = np.arange(1, 10, 0.02)

#Function to calculate SDOF receptance amplitude
def r_amp(k, m, zeta, w):
    c = 2 * zeta * np.sqrt(k * m)
    return 1/np.sqrt((k - m * w**2)**2 + (w * c)**2)
    
#Function to calculate SDOF receptance phase angle
def r_phase(k, m, zeta, w):
    c = 2 * zeta * np.sqrt(k * m)
    return np.arctan(- w * c / (k - m * w**2))

#Function to calculate real part of receptance FRF
def r_real(k, m, zeta, w):
    c = 2 * zeta * np.sqrt(k * m)
    return (k - m*w**2)/((k - m * w**2)**2 + (w * c)**2)

#Function to calculate imaginary part of receptance FRF
def r_img(k, m, zeta, w):
    c = 2 * zeta * np.sqrt(k * m)
    return (-c*w)/((k - m * w**2)**2 + (w * c)**2)

#Function to set plot properties and showing Bode plot for SDOF system
def plot_RFRF(w, r_amp, r_phase):
    fig, ax = plt.subplots(2, sharex = 'col', sharey = 'row')
    ax[0].plot(w, r_amp)
    ax[1].plot(w, r_phase)
    ax[0].set(ylabel = 'Amplitude (m/N)')
    ax[1].set(ylabel = 'Phase angle (rad)', xlabel = 'Frequency (Hz)', title = "Phase angle vs Frequency", xticks = np.arange(0,11,1))

    plt.text(0.1, 0.9, 'Receptance Amplitude', transform = ax[0].transAxes)
    plt.text(0.1, 0.9, 'Receptance Phase', transform = ax[1].transAxes)
    #plt.show()
    
#plot_RFRF(w, r_amp(k, m, zeta, w), r_phase(k, m, zeta, w))
#plt.savefig("C:/Users/e1206659/Pictures/bode_plot.png")


#Function to calculate SDOF mobility amplitude
def m_amp(w, r_amp):
    return w * r_amp

#Function to calculate SDOF inertance amplitude
def i_amp(w, r_amp):
    return (w**2) * r_amp

# Amplitude Bode plots SDOF system - Linear
def plot_frf_amp_linear(w, r_amp, m_amp, i_amp):
    fig, ax = plt.subplots(3, figsize=(9, 12), sharex = 'col', sharey = 'row')

    ax[0].plot(w, r_amp)
    plt.text(0.8, 0.9, 'Receptance', transform=ax[0].transAxes)
    
    ax[1].plot(w, m_amp)
    plt.text(0.8, 0.9, 'Mobility', transform=ax[1].transAxes)
    
    ax[2].plot(w, i_amp)
    plt.text(0.8, 0.9, 'Inertance', transform=ax[2].transAxes)
    
    ax[0].set(ylabel = 'Amplitude (m/N)')
    ax[1].set(ylabel = 'Amplitude (m/s/N)')
    ax[2].set(ylabel = 'Amplitude (m/s^2/N)', xlabel = 'Frequency (Hz)', xscale = 'linear')

#plot_frf_amp_linear(w, r_amp(k, m, zeta, w), m_amp(w, r_amp(k, m, zeta, w)), i_amp(w, r_amp(k, m, zeta, w)))
#plt.savefig("C:/Users/e1206659/Pictures/amp_comparison_frf_linear.png")    

# Amplitude Bode plots SDOF system - log-log
def plot_frf_amp_log(w, r_amp, m_amp, i_amp):
    fig, ax = plt.subplots(3, figsize=(9, 12), sharex = 'col', sharey = 'row')

    r_amp = 20*np.log10(r_amp)
    m_amp = 20*np.log10(m_amp)
    i_amp = 20*np.log10(i_amp)
    ax[0].plot(w, r_amp)
    plt.text(0.8, 0.9, 'Receptance', transform=ax[0].transAxes)
    
    ax[1].plot(w, m_amp)
    plt.text(0.8, 0.9, 'Mobility', transform=ax[1].transAxes)
    
    ax[2].plot(w, i_amp)
    plt.text(0.8, 0.9, 'Inertance', transform=ax[2].transAxes)
    
    ax[0].set(ylabel = 'dB (20 log10) Amplitude (m/N)')
    ax[1].set(ylabel = 'dB (20 log10) Amplitude (m/s/N)')
    ax[2].set(ylabel = 'dB (20 log10) Amplitude (m/s^2/N)', xlabel = 'Frequency (Hz)', xscale = 'log')
    #plt.show()
    
#plot_frf_amp_log(w, r_amp(k, m, zeta, w), m_amp(w, r_amp(k, m, zeta, w)), i_amp(w, r_amp(k, m, zeta, w)))
#plt.savefig("C:/Users/e1206659/Pictures/amp_comparison_frf_log.png")

def plot_frf_amp_log_compare2(w, r_amp1, r_amp2):

    r_amp1 = 20*np.log10(r_amp1)
    r_amp2 = 20*np.log10(r_amp2)

    plt.plot(w, r_amp1, label = 'M = 1 Kg')
    plt.plot(w, r_amp2, label = 'M = 0.4 Kg')

    plt.xlabel('Frequency (Hz)')
    plt.ylabel('dB (20 log10) Amplitude (m/N)')
    plt.title('Receptance Amplitude')
    plt.legend()
    plt.xscale('log')
    #plt.show()
    
    
#plot_frf_amp_log_compare2(w, r_amp(k, m, zeta, w), r_amp(k, m*0.4, zeta, w))
#plt.savefig("C:/Users/e1206659/Pictures/amp_comparison_frf_log_compare2.png")

def nyquist_plot(r_real, r_img):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    #spine placement data centered
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    
    plt.plot(r_real, r_img, marker = '+')
    plt.axis('square')
    plt.xlabel('Real part', horizontalalignment='left', position=(1,25))
    plt.ylabel('Imaginary part')
    plt.title('Receptance Nyquist Plot')

   # plt.xscale('log')
    plt.show()
    
nyquist_plot(r_real(k, m, zeta, w), r_img(k, m, zeta, w))
