# Swahili Audio-to-Text ASR Model

This project leverages a dataset from ALPHA project https://github.com/besacier/ALFFA_PUBLIC/tree/master/ASR/SWAHILI to create a fine-tuned model based on the BERT Transformer for Automatic Speech Recognition (ASR) in Swahili audio. The goal is to transcribe Swahili audio into text accurately.

## Model Access

You can access the pre-trained model on Hugging Face using the following link:

**Model Name:** `Peed911/swahili_asr_audio_to_text`

Alternatively, you can use the Hugging Face Transformers library to call the model directly:

```python
# Use a pipeline as a high-level helper
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="Peed911/swahili_asr_audio_to_text")
```

Or load the model and tokenizer separately:

```python
from transformers import AutoTokenizer, AutoModelForASR

tokenizer = AutoTokenizer.from_pretrained("Peed911/swahili_asr_audio_to_text")
model = AutoModelForASR.from_pretrained("Peed911/swahili_asr_audio_to_text")
```

## Repository Contents

This Git repository contains all the files used to build and fine-tune the Swahili ASR model.

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Training

The model has already been pre-trained, so there's no need to retrain it. However, if you want to fine-tune it on a custom dataset, you can use the provided training script.

## Inference

For performing inference with the trained model, you have two options:

### Gradio

To use Gradio for audio transcription, run the following command using the provided demo script:

```bash
python gradio_demo.py
```

### FastAPI

For FastAPI-based audio transcription, run the application using the following command from the root folder:

```bash
uvicorn main:app --reload
```

Ensure that you are in the root folder when executing this command.

### Docker

You can also run the FastAPI application inside a Docker container. First, make sure you have Docker installed on your system. Then, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t swahili-asr .
   ```

   This command will build a Docker image named `swahili-asr` based on the provided Dockerfile.

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 swahili-asr
   ```

   This command will start a Docker container from the `swahili-asr` image, mapping port 8000 from the container to port 8000 on your host machine.

You can access the FastAPI application running inside the Docker container at `http://localhost`. Enjoy Swahili audio transcription with our ASR model!

Feel free to reach me on `diallomous@gmail.com` if you have any questions or need further assistance.
