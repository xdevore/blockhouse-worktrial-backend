from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CandlestickData
from .models import LineChartData
from .models import BarChartData
from .models import PieChartData

@api_view(['GET'])
def getCandlestickData(request):

    default_data = CandlestickData()  

    data = {
        'data': default_data.data['data']
    }

    return Response(data)

@api_view(['GET'])
def getLineChartData(request):

    default_data = LineChartData()  

    data = {
        'labels': default_data.data['labels'],
        'data': default_data.data['data']
    }

    return Response(data)

@api_view(['GET'])
def getBarChartData(request):

    default_data = BarChartData()  

    data = {
        'labels': default_data.data['labels'],
        'data': default_data.data['data']
    }

    return Response(data)

@api_view(['GET'])
def getPieChartData(request):

    default_data = PieChartData()  

    data = {
        'labels': default_data.data['labels'],
        'data': default_data.data['data']
    }

    return Response(data)
