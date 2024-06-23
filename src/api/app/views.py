from app.controllers import PredictionController
from fastapi import APIRouter
from pydantic import BaseModel


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

router = APIRouter()

# Rota para predição
@router.post("/api/v1/predict")
def predict(request: PredictRequest):
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
    prediction = PredictionController.predict(features)
    return {"prediction": prediction}
