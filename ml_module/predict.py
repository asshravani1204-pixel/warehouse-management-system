def predict_failure(delay_flag, distance_km, traffic_level, weather_condition, failed_attempts):
    score = 0

    if delay_flag:
        score += 2

    if distance_km > 15:
        score += 1

    if traffic_level.lower() == "high":
        score += 2
    elif traffic_level.lower() == "medium":
        score += 1

    if weather_condition.lower() in ["rain", "storm"]:
        score += 2
    elif weather_condition.lower() == "cloudy":
        score += 1

    if failed_attempts >= 2:
        score += 2
    elif failed_attempts == 1:
        score += 1

    if score >= 6:
        return {
            "risk_level": "High Risk",
            "score": score,
            "reason": "Shipment has strong chance of delay/failure"
        }
    elif score >= 3:
        return {
            "risk_level": "Medium Risk",
            "score": score,
            "reason": "Shipment has moderate delivery risk"
        }
    else:
        return {
            "risk_level": "Low Risk",
            "score": score,
            "reason": "Shipment is likely to be delivered successfully"
        }