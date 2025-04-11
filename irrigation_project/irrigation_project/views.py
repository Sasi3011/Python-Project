from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Plant, UserInput, IrrigationLog
from .serializers import UserInputSerializer
from .utils import get_weather_data
from .ai_engine import calculate_water_need

class IrrigationDecision(APIView):
    def post(self, request):
        location = request.data['location']
        plant_id = request.data['plant']
        plant = Plant.objects.get(id=plant_id)
        weather = get_weather_data(location)
        water_needed = calculate_water_need(plant.water_required_lph, weather)
        
        user_input = UserInput.objects.create(location=location, plant=plant, water_used=water_needed)
        IrrigationLog.objects.create(location=location, plant_name=plant.name, water_given=water_needed)

        return Response({'message': 'Irrigation decision made', 'water': water_needed})
