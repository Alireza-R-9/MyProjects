import numpy as np
import matplotlib.pyplot as plt
import time


def basd_modulation(t, signal):
    # Implement BASD modulation logic
    basd_signal = np.zeros_like(signal)
    for i in range(len(signal)):
        if signal[i] >= 0:
            basd_signal[i] = 1
        else:
            basd_signal[i] = -1
    return basd_signal


def bosd_modulation(t, signal):
    # Implement BOSD modulation logic
    bosd_signal = np.zeros_like(signal)
    for i in range(len(signal)):
        if signal[i] >= 0:
            bosd_signal[i] = 1
        else:
            bosd_signal[i] = 0
    return bosd_signal


def boosd_modulation(t, signal):
    # Implement BOOSD modulation logic
    boosd_signal = np.zeros_like(signal)
    for i in range(len(signal)):
        if signal[i] >= 0:
            boosd_signal[i] = 1
        else:
            boosd_signal[i] = -1
    return boosd_signal


def calculate_snr(signal, noise):
    # Calculate SNR
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Main script

# Generating the original signal
t = np.arange(-1, 8, 0.1)
original_signal = np.sin(2 * np.pi * t)

# Adding noise to the signal
noise = np.random.normal(0, 0.1, len(t))
noisy_signal = original_signal + noise

# Modulating using BASD, BOSD, BOOSD
basd_signal = basd_modulation(t, noisy_signal)
bosd_signal = bosd_modulation(t, noisy_signal)
boosd_signal = boosd_modulation(t, noisy_signal)

# Plotting results
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, original_signal, 'b', label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, noisy_signal, 'g', label='Noisy Signal')
plt.title('Noisy Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, basd_signal, 'r', label='BASD Signal')
plt.title('BASD Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t, bosd_signal, 'm', label='BOSD Signal')
plt.plot(t, boosd_signal, 'y', label='BOOSD Signal')
plt.title('BOSD and BOOSD Modulated Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()

# Calculating SNR for each modulation technique
snr_basd = calculate_snr(basd_signal, noise)
snr_bosd = calculate_snr(bosd_signal, noise)
snr_boosd = calculate_snr(boosd_signal, noise)

print(f"SNR for BASD: {snr_basd:.2f} dB")
print(f"SNR for BOSD: {snr_bosd:.2f} dB")
print(f"SNR for BOOSD: {snr_boosd:.2f} dB")
