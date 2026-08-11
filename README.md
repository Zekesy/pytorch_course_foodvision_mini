# FoodVision Mini 🍕🥩🍣

FoodVision Mini is a computer vision application that uses a pretrained **EfficientNet-B2** model to classify images of food into three categories:

* 🍕 Pizza
* 🥩 Steak
* 🍣 Sushi

The model was trained using transfer learning with PyTorch and is deployed as an interactive **Gradio** web application.

## Demo

**Live Demo:** [FoodVision Mini](https://pytorch-course-foodvision-mini.onrender.com/)

> The demo is hosted on Render and runs inference on CPU.

## Model

The application uses **EfficientNet-B2** as the feature extractor.

The model architecture consists of:

```text
Input Image
     ↓
EfficientNet-B2
     ↓
Feature Extractor
     ↓
Dropout
     ↓
Linear Classifier
     ↓
Pizza / Steak / Sushi
```

The final classifier consists of:

```text
Dropout(p=0.3)
Linear(1408 → 3)
```

The pretrained model was fine-tuned using a subset of the Food datasets and the resulting model weights are stored in:

```text
09_pretrained_effnetb2_feature_extractor_pizza_steak_sushi_20_percent.pth
```

## Features

* Upload an image of food
* Classify the image as pizza, steak, or sushi
* Display prediction probabilities
* Display prediction/inference time
* Example images included in the Gradio interface
* CPU-compatible inference

## Project Structure

```text
foodvision-mini/
├── app.py
├── model.py
├── requirements.txt
├── examples/
│   └── ...
└── 09_pretrained_effnetb2_feature_extractor_pizza_steak_sushi_20_percent.pth
```

### `app.py`

Contains the Gradio interface and prediction function.

### `model.py`

Contains the function used to create the EfficientNet-B2 model and its image transformations.

### `examples/`

Contains example food images that can be loaded directly from the Gradio interface.

### Model weights

Contains the trained EfficientNet-B2 model weights used for inference.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/foodvision-mini.git
cd foodvision-mini
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

The Gradio application will provide a local URL that can be opened in a web browser.

## Deployment

The application is deployed using [Render](https://render.com/).

Render installs the dependencies from `requirements.txt` and starts the application using:

```bash
python app.py
```

The Gradio application is configured to listen on Render's assigned port:

```python
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000))
)
```

## Technologies

* [Python](https://www.python.org/)
* [PyTorch](https://pytorch.org/)
* [Torchvision](https://pytorch.org/vision/stable/)
* [Gradio](https://www.gradio.app/)
* [Render](https://render.com/)

## Acknowledgements

This project was created while working through the [Learn PyTorch for Deep Learning](https://www.learnpytorch.io/) course by Daniel Bourke.

The project is based on the **FoodVision Mini** model deployment section of the course.

## License

This project is intended primarily as a learning project. See the repository and associated course materials for applicable licensing information.
