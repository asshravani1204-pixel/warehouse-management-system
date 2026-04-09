def calculate_carbon_score(vehicle_type, distance_km, weight_kg, delivery_status):
    emission_factor = {
        "bike": 0.02,
        "scooter": 0.05,
        "van": 0.12,
        "truck": 0.20
    }

    vehicle = vehicle_type.lower()

    if vehicle not in emission_factor:
        return {
            "error": "Unsupported vehicle type"
        }

    base_emission = emission_factor[vehicle] * distance_km * weight_kg / 10

    if delivery_status.lower() == "failed":
        base_emission *= 1.2

    if base_emission < 5:
        score_label = "Low"
    elif base_emission < 12:
        score_label = "Medium"
    else:
        score_label = "High"

    return {
        "vehicle_type": vehicle_type,
        "distance_km": distance_km,
        "weight_kg": weight_kg,
        "delivery_status": delivery_status,
        "estimated_emission": round(base_emission, 2),
        "carbon_score": score_label
    }