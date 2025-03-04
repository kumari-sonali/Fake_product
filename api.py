import os
import gdown
import zipfile
import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import RobertaTokenizer, RobertaForSequenceClassification

app = FastAPI()

file_id = "188LAdSrPHLZh27-JpFQrKOjToVOQoYK2" 
model_dir = "roberta_fake_review_model"
model_zip = f"{model_dir}.zip"

# Check if the model folder exists, else download and extract
if not os.path.exists(model_dir):
    print("Downloading model from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", model_zip, quiet=False)

    # Extract the model
    with zipfile.ZipFile(model_zip, "r") as zip_ref:
        zip_ref.extractall(".")

    os.remove(model_zip)  # Clean up the zip file

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained(model_dir)
model = RobertaForSequenceClassification.from_pretrained(model_dir)
model.eval()  

# request body
class ReviewInput(BaseModel):
    text: str

def preprocess(text):
    """Tokenize input text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    return inputs

#Predicting the fakeness of review
def predict(text):     
    inputs = preprocess(text)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        prediction = torch.argmax(probabilities, dim=1).item()
    
    label = "Genuine Review" if prediction == 1 else "Fake Review"
    confidence = probabilities[0][prediction].item()
    return {"label": label, "confidence": confidence}

# API Endpoint
@app.post("/predict/")
def predict_review(review: ReviewInput):
    return predict(review.text)
