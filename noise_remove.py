import noisereduce as nr
from scipy.io import wavfile
import numpy as np
from scipy.signal import butter, lfilter
 
# Function to apply a low-pass filter to improve audio quality
def low_pass_filter(data, rate, cutoff=5000, order=5):
    nyquist = 0.5 * rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data
 
# Function to normalize the audio to improve clarity
def normalize_audio(data):
    norm_data = data / np.max(np.abs(data), axis=0)
    return np.int16(norm_data * 32767)
 
# Function to remove background noise
def remove_background_noise(input_audio_path):
    # Load the audio file
    rate, data = wavfile.read(input_audio_path)
 
    # Apply non-stationary noise reduction (suited for dialogue preservation)
    print("Removing background noise and retaining dialogue...")
    reduced_noise = nr.reduce_noise(y=data, sr=rate, stationary=False, prop_decrease=1.0,
                                    thresh_n_mult_nonstationary=2, sigmoid_slope_nonstationary=10)
 
    return rate, reduced_noise
 
# Function to improve the quality of the audio
def improve_audio_quality(data, rate):
    # Apply a low-pass filter to remove high-frequency noise
    print("Applying low-pass filter to reduce high-frequency noise...")
    filtered_audio = low_pass_filter(data, rate, cutoff=5000)
 
    # Normalize the audio for better clarity
    print("Normalizing the audio...")
    normalized_audio = normalize_audio(filtered_audio)
 
    return normalized_audio
 
# Main function to process the audio
def process_audio(input_audio_path, output_audio_path):
    # Step 1: Remove background noise
    rate, reduced_noise = remove_background_noise(input_audio_path)
 
    # Step 2: Improve audio quality
    print("Improving audio quality...")
    improved_audio = improve_audio_quality(reduced_noise, rate)
 
    # Save the cleaned and improved audio file
    wavfile.write(output_audio_path, rate, improved_audio)
    print(f"Processed audio saved to: {output_audio_path}")
 
# Define file paths
input_audio_file = 'Vasool-Raja.wav'  # Input file path
output_audio_file = 'output_cleaned_audio1.wav'  # Output file path
 
# Run the audio processing pipeline
process_audio(input_audio_file, output_audio_file)
 
