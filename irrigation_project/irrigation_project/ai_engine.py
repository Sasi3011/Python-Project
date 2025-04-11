def calculate_water_need(plant_lph, weather_data):
    """
    Calculates adjusted water based on plant need and current humidity.
    """
    humidity = weather_data.get('humidity', 50)
    # Reduce water if humidity is high
    if humidity > 70:
        return plant_lph * 0.7
    elif humidity < 30:
        return plant_lph * 1.2
    return plant_lph
