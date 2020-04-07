import django_filters
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters, status, generics
from rest_framework.decorators import detail_route, api_view, renderer_classes
from rest_framework_swagger import renderers
from rest_framework.response import Response
from .models import Iris
from .serializer import IrisSerializer
import pickle

def index(request):
    return render("Hello REST_API!!!!")

class IrisViewSet(viewsets.ModelViewSet):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer

@api_view(['POST'])
def predict(request):
    """
    Iris 推論API

    ---
    Parameters:
    - name: sepal_length
        description: Foobar long description goes here
        required: true
        type: int
        paramType: form
    """
    serializer = IrisSerializer(data=request.data)
    if serializer.is_valid():
        with open("/ml_model/model.pkl","rb") as f:
            model = pickle.load(f)
        data = [request.data[i] for i in ["sepal_length", "sepal_width", "petal_length", "petal_width"]]
        result = model.predict([data])[0]
        return Response(data={"result": result}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
