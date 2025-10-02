# 🖼️ Image Classification with EfficientNetB1 (CIFAR-10)

This project demonstrates an end-to-end **image classification system** built with:

- **Model**: EfficientNetB1 trained on CIFAR-10
- **Backend**: FastAPI serving the model converted to **ONNX** with inference via `onnxruntime`
- **Frontend**: React app to upload and classify images
- **Deployment**: Fully containerized with **Docker** and orchestrated using **Docker Compose**

---

## 📂 Project Structure (Highlighting main folders/ files)
```plaintext
.
├── API/ # FastAPI backend
│ └── model/
| └── image_classification_model.onnx
│ ├── Dockerfile
│ ├── Image Classification.ipynb
│ ├── main.py # API code
│ └── requirements.txt
|
├── frontend/ # React frontend
│ ├── Dockerfile
│ ├── src/
│ └── App.js
├── docker-compose.yml # Multi-service setup
└── README.md
```


## 🚀 Training

The model was trained on the **CIFAR-10 dataset** using PyTorch.

- **Architecture**: EfficientNetB1
- **Epochs**: 45
- **Optimizer**: `AdamW (lr=0.001, weight_decay=0.0025)`
- **Scheduler**: `CosineAnnealingLR (T_max=40, eta_min=1e-5)`
- **Loss Function**: CrossEntropyLoss
- **Device**: GPU (if available)

Training loop snippet:

```python
for epoch in range(epochs):
    training_step(model, trainloader)
    validation_step(model, valloader)
    scheduler.step()
```

## ▶️ Running the Project

### Clone the repository

```bash
git clone https://github.com/your-username/image-classification.git
cd image-classification
```

### Build and run with Docker Compose

```bash
docker-compose up --build
```

### Access the frontend

```bash
👉 http://localhost:70
```
