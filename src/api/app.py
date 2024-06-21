from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from typing import List
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import io
import logging
import os 
from dotenv import load_dotenv, dotenv_values

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurar boto3 para acessar o S3
s3_client = boto3.client('s3')

load_dotenv()
# fazer download do model
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
MODEL_FILE_KEY = 'modelo/model.joblib'


# Baixar e carregar o modelo do S3
def load_model_from_s3():
    try:
        logger.info(f"Baixando o modelo do bucket {AWS_BUCKET_NAME}, chave {MODEL_FILE_KEY}")
        response = s3_client.get_object(Bucket=AWS_BUCKET_NAME, Key=MODEL_FILE_KEY)
        model_data = response['Body'].read()
        model = joblib.load(io.BytesIO(model_data))
        logger.info("Modelo carregado com sucesso")
        return model
    except s3_client.exceptions.NoSuchKey:
        logger.error("Modelo não encontrado no bucket S3.")
        return None
    except s3_client.exceptions.NoSuchBucket:
        logger.error("Bucket S3 não encontrado.")
        return None
    except NoCredentialsError:
        logger.error("Credenciais AWS não encontradas.")
        return None
    except PartialCredentialsError:
        logger.error("Credenciais AWS incompletas.")
        return None
    except Exception as e:
        logger.error(f"Erro ao baixar o modelo: {e}")
        return None

model = load_model_from_s3()

# Definir o aplicativo FastAPI
app = FastAPI()


# Definir o esquema da requisição
class PredictRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_week_nights: int
    type_of_meal_plan: int
    required_car_parking_space: int
    room_type_reserved: int
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    market_segment_type: int
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int
    no_of_special_requests: int
    booking_status: int


# Rota para predição
@app.post("/api/v1/predict")
def predict(request: PredictRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo não carregado")

    # Fazer predição
    try:
        # Extrair os recursos do request e transformar em uma lista
        features = [
            request.no_of_adults,
            request.no_of_children,
            request.no_of_weekend_nights,
            request.no_of_week_nights,
            request.type_of_meal_plan,
            request.required_car_parking_space,
            request.room_type_reserved,
            request.lead_time,
            request.arrival_year,
            request.arrival_month,
            request.arrival_date,
            request.market_segment_type,
            request.repeated_guest,
            request.no_of_previous_cancellations,
            request.no_of_previous_bookings_not_canceled,
            request.no_of_special_requests,
            request.booking_status
        ]
        
        # Certificar que a entrada é um array 2D (como esperado pela maioria dos modelos sklearn)
        prediction = model.predict([features])
        # Converter os tipos numpy para tipos nativos do Python
        prediction = prediction.tolist()
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao fazer a predição: {e}")

# Para rodar a aplicação com Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
