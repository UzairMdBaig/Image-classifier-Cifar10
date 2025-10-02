from fastapi import FastAPI, UploadFile, File, Depends
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

ort_session = ort.InferenceSession("model/image_classification_model.onnx")

classes = ['plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship', 'truck']


mean = np.array([0.49139968, 0.48215827, 0.44653124], dtype=np.float32)
std = np.array([0.24703233, 0.24348505, 0.26158768], dtype=np.float32)

def preprocess_image(file: UploadFile = File(...)):
    content = file.file.read()
    image = Image.open(io.BytesIO(content)).convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image).astype("float32") / 255.0
    image = (image - mean) / std 
    image = np.transpose(image, (2, 0, 1))
    image = np.expand_dims(image, axis=0)
    return image.astype(np.float32)

@app.post("/predict")
async def predict(image: np.ndarray = Depends(preprocess_image)):
    predicted_class =  np.argmax(ort_session.run(None, {"image": image})[0])
    return {"predicted_class": classes[predicted_class]}

    