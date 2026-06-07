# Laptop Price Predictor

This project contains a machine learning model and a Flask web app that predicts a laptop price from hardware and specification inputs.

## Project Structure

- `model/` - training notebook, model artifact, and Python dependencies for model work
- `web/` - Flask application, HTML template, and web app dependencies
- `src/` - source data files used during model development

## Features

- Predicts laptop price from RAM, weight, storage, display, company, CPU, GPU, operating system, and form factor inputs
- Simple web interface for entering laptop details
- Uses a pre-trained model stored in `model/predictor.pickle`

## Requirements

- Python 3.9 or newer
- `pip`

## Setup

1. Clone or download the project.
2. Open a terminal in the project root.
3. Create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

4. Install the dependencies for the web app.

```powershell
pip install -r web/requirements.txt
```

If you want to work on the model training notebook, also install the model dependencies:

```powershell
pip install -r model/requirements.txt
```

## Running the Web App

The Flask app expects to be run from the `web/` folder because it loads the model with a relative path.

```powershell
cd web
python app.py
```

Open the local address shown in the terminal, usually `http://127.0.0.1:5000/`.

## How to Use

1. Open the web app in your browser.
2. Fill in the laptop details on the form.
3. Choose the company, type, operating system, CPU, and GPU options.
4. Click **Predict Price**.
5. The predicted price will appear below the form.

## Training or Updating the Model

The notebook in `model/model_bulding.ipynb` is used to build or retrain the regression model.

When you retrain the model, make sure the exported pickle file is saved as:

```text
model/predictor.pickle
```

That is the file the Flask app loads at startup.

## Notes

- The app uses the exact feature columns expected by the trained model, so changing the model requires keeping the same input structure.
- Some values are converted in the app before prediction, and the final output is shown in rupees.

## Troubleshooting

- If the app cannot find `predictor.pickle`, confirm you started it from the `web/` directory and that `model/predictor.pickle` exists.
- If a package import fails, reinstall the dependencies with `pip install -r web/requirements.txt`.
