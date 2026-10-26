from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="API de Pozos - Ciencia de Datos")

# Permitir conexiones desde React (Vite suele usar el puerto 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WellFeatures(BaseModel):
    profundidad: float
    presion_inicial: float
    temperatura: float
    etapa_fractura: int

@app.post("/predict-dynamic")
def predict_dynamic_charts(features: WellFeatures):
    # Lógica de predicción simulada (reemplazable por tu modelo .pkl)
    pred_value = float(features.profundidad * 1.5 + features.presion_inicial * 2.1 + (features.etapa_fractura * 15))

    return {
        "success": True,
        "prediccion_produccion": round(pred_value, 2),
        "unidades": "barriles equivalentes / día",
        "charts": {
            "line_chart": {
                "labels": ["Mes -4", "Mes -3", "Mes -2", "Mes -1", "Actual (Predicción)"],
                "values": [round(pred_value * 0.85, 2), round(pred_value * 0.90, 2), round(pred_value * 0.88, 2), round(pred_value * 0.95, 2), round(pred_value, 2)]
            },
            "bar_chart": {
                "labels": ["Profundidad", "Presión Inicial", "Temperatura", "Etapas de Fractura"],
                "values": [0.42, 0.28, 0.18, 0.12]
            }
        }
    }