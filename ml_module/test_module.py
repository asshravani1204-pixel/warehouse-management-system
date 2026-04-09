from predict import predict_failure
from carbon_score import calculate_carbon_score

failure_result = predict_failure(
    delay_flag=True,
    distance_km=18,
    traffic_level="high",
    weather_condition="rain",
    failed_attempts=1
)

carbon_result = calculate_carbon_score(
    vehicle_type="van",
    distance_km=20,
    weight_kg=12,
    delivery_status="delivered"
)

print("Failure Prediction Result:")
print(failure_result)

print("\nCarbon Score Result:")
print(carbon_result)