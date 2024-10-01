# Audio Processing Tool

This tool processes audio files to remove background noise and improve audio quality. It utilizes the `noisereduce` library for noise reduction and applies a low-pass filter for enhanced clarity.

## Features

- **Background Noise Removal**: Reduces unwanted background noise while preserving dialogue.
- **Low-Pass Filtering**: Applies a low-pass filter to eliminate high-frequency noise.
- **Audio Normalization**: Normalizes the audio for improved clarity.

## Requirements

- `Python 3.x`
- `numpy`
- `scipy`
- `noisereduce`

You can install the required libraries using pip:

```bash
pip install numpy scipy noisereduce
```

## Usage

1. Place your input audio file in the same directory as this script.
2. Update the `input_audio_file` variable with the name of your audio file (e.g., `Vasool-Raja.wav`).
3. Run the script. The processed audio will be saved as `output_cleaned_audio1.wav`.

```python
# Define file paths
input_audio_file = 'Vasool-Raja.wav'  # Input file path
output_audio_file = 'output_cleaned_audio1.wav'  # Output file path

# Run the audio processing pipeline
process_audio(input_audio_file, output_audio_file)
```

## Conclusion
>
> This audio processing tool effectively enhances audio quality by removing background noise, applying low-pass filtering, and normalizing volume levels. It is particularly useful for improving clarity in dialogue recordings, making it an excellent choice for podcasts, interviews, and other audio projects.

