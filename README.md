# Sortify — Predictive Model

The machine-learning half of **Sortify**, an automated waste-sorting bin. A **ResNet50** image classifier reads frames captured by the ESP32-CAM and returns a material label (`cardboard`, `plastic`, `glass`, ...) that the firmware uses to drive the sorter.

Developed for the Integration 3 course — Team 11.

---

## How it fits together

```
ESP32-CAM (Sortify_ESP32)  ──image──▶  this repo (Flask + ResNet50)  ──label──▶  ESP32-CAM
                                             │
                                             └──prediction──▶  Spring Boot app (Sortify_WebApp)
                                                                      │
                                                                      ▼
                                                                PostgreSQL (history)
```

- The ESP32-CAM posts a JPEG over HTTP.
- A small Flask service resizes/compresses the image with Pillow and runs it through the trained ResNet50.
- The predicted label is returned to the ESP32 and also pushed to the Spring Boot web app for display/history.

---

## Model

A **ResNet50** convolutional network trained on a dataset of common waste materials.

| Model | Validation accuracy |
|-------|--------------------:|
| **ResNet50** (used in prod) | **96%** |
| Gaussian Naive Bayes | 37% |
| Logistic Regression | 37% |

The two baselines are kept under `other_models/` as a reference for *why* we ended up using a deep model for this task.

---

## Repository layout

```
Sortify_predictive/
├── Garbage_Classification_Pytorch.ipynb   # ResNet50 training / eval notebook
├── Test.py                                 # Simulates the ESP32 client — sends an image and prints the label
├── other_models/
│   ├── Garbage_Classification_Gauss.ipynb
│   └── Garbage_Classification_LogisticRegression.ipynb
└── test-images/
    ├── cardboard.jpeg
    └── glass.jpeg
```

`Test.py` is meant as a stand-in for the ESP32-CAM during development: it POSTs one of the sample images to the Flask service and prints the response, so the backend can be iterated on without real hardware in the loop.

---

## Requirements

- **Python 3.x**
- **PyTorch** (for training / inference with the ResNet50 model)
- **Flask** (serves the `/image` endpoint)
- **Pillow** (PIL) — image resize / compression before inference
- **Spring Boot** + **PostgreSQL** (optional, only if you also run the companion web app to store predictions)

---

## Running

Training / exploration:

```bash
jupyter notebook Garbage_Classification_Pytorch.ipynb
```

Simulated ESP32 client against your Flask backend:

```bash
python Test.py
```

---

## Related repos

- [`Sortify_ESP32`](https://github.com/souhaibothmani/Sortify_ESP32) — ESP32-CAM firmware that talks to this service.
- `Sortify_WebApp` — Spring Boot dashboard that consumes the predictions.

---

## Team

Integration 3 — Team 11 (Sortify).
