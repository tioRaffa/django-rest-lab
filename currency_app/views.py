from rest_framework.views import APIView
from currency_app.api.exchangerate import convert_currency
from rest_framework import status
from rest_framework.response import Response


class CurrencyConvertAPIView(APIView):
    def get(self, request):
        from_currency = request.query_params.get('from')
        to_currency = request.query_params.get('to')
        amount = request.query_params.get('amount')

        if not all([from_currency, to_currency, amount]):
            return Response(
                {'error': 'Informe os parametros: FROM e TO'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            amount = float(amount)
        except ValueError:
            return Response(
                {'error': 'O parametro amount deve ser NUMERICO!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        convertion = convert_currency(from_currency, to_currency, amount)
        if convertion:
            return Response(convertion, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Não foi possivel obter os dados de conversão.'
            }, status=status.HTTP_404_NOT_FOUND
            )
