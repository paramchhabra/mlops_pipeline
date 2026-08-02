import os
import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from mlProject.pipeline.prediction import PredictionPipeline

app = FastAPI(title="Wine Quality Prediction API")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/train")
async def train():
    os.system("python main.py")
    return {"message": "Training Successful!"}


@app.get("/predict", response_class=HTMLResponse)
async def predict_form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...),
):
    try:
        data = np.array([
            fixed_acidity,
            volatile_acidity,
            citric_acid,
            residual_sugar,
            chlorides,
            free_sulfur_dioxide,
            total_sulfur_dioxide,
            density,
            pH,
            sulphates,
            alcohol
        ]).reshape(1, 11)

        prediction = PredictionPipeline().predict(data)

        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "prediction": str(prediction)
            }
        )

    except Exception as e:
        print(f"Prediction Error: {e}")
        return templates.TemplateResponse(
            "results.html",
            {
                "request": request,
                "prediction": "Something went wrong!"
            }
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",      # change "app" if your filename is different
        host="0.0.0.0",
        port=8080,
        reload=True
    )