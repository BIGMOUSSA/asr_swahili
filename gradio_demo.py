import gradio as gr
import numpy as np
from utils import ASRInference  # Replace 'your_module' with the actual module where ASRInference is defined

# Create an instance of ASRInference
asr = ASRInference()

# Define a function that uses the ASRInference instance
def transcribe_audio(audio):
    # Convert audio to a NumPy array and flatten it if necessary
    #if isinstance(audio, list):
     #   audio = np.array(audio)
    #elif isinstance(audio, np.ndarray):
     #   audio = audio.ravel()  # Flatten the array
    #else:
     #   raise ValueError("Unsupported audio format")

    return asr.inference(audio)

# Create a Gradio interface
iface = gr.Interface(fn=transcribe_audio, inputs="audio", outputs="text")

if __name__ == "__main__":
    iface.launch()
    #print(transcribe_audio("audio_test.wav"))
