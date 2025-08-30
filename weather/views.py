from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from weather.api.open_weather import city_weather


class WeatherOnCityAPIView(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        state = request.query_params.get('state')

        if not all([city, state]):
            return Response(
                {"error": "Por favor, forneça os parâmetros como 'city' e 'state'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        weather_data = city_weather(city_name=city, state_code=state)
        if weather_data:
            return Response(weather_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Não foi possivel obter o status do clima"},
                status=status.HTTP_404_NOT_FOUND
            )