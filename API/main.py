from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import onnxruntime as ort
from PIL import Image
import numpy as np
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],          
    allow_headers=["*"],          
)

ort_session = ort.InferenceSession("image_classification_model.onnx")

classes = ['plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship', 'truck']


mean = np.array([0.49139968, 0.48215827, 0.44653124], dtype=np.float32)
std = np.array([0.24703233, 0.24348505, 0.26158768], dtype=np.float32)

def preprocess_image(image_bytes):
    image = Image.open(image_bytes).convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image).astype("float32") / 255.0
    image = (image - mean) / std 
    image = np.transpose(image, (2, 0, 1))
    image = np.expand_dims(image, axis=0)
    return image.astype(np.float32)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file = await file.read()
    image = preprocess_image(io.BytesIO(file))
    predicted_class =  np.argmax(ort_session.run(None, {"image": image})[0])
    return {"predicted_class": classes[predicted_class]}

    