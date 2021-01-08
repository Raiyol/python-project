from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Bike
from .serializers import BikeSerializer

# Create your views here.


def predict_rbc(unscaled_data):
    import joblib
    colonnes = ["Hour", "Temperature", "Humidity", "WS", "Visibility",
                "SR", "Rainfall", "Snowfall", "Holiday", "Seasons", "WD", "Month"]
    path_to_model = "./pkl/model_svr.pkl"
    path_for_scaler = "./pkl/scaler.pkl"
    unscaled_data = [[unscaled_data[colonne] for colonne in colonnes]]
    print(unscaled_data)
    model = joblib.load(path_to_model)
    scaler = joblib.load(path_for_scaler)
    donnees_scalees = scaler.transform(unscaled_data)
    bike_count = model.predict(donnees_scalees)
    return bike_count[0]


@csrf_exempt
def predict(request):
    """
    Renvoie un bike avec le bike count prédit
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BikeSerializer(data=data)
        if serializer.is_valid():
            data["RBC"] = predict_rbc(data)
            serializer = BikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def bike_list(request):
    """
    List all houses, or create a new Bike.
    """
    if request.method == 'GET':
        houses = Bike.objects.all()
        serializer = BikeSerializer(houses, many=True)
        reponse = JsonResponse(serializer.data, safe=False)
        return reponse

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def bike_detail(request, pk):
    """
    Retrieve, update or delete a bike.
    """
    try:
        bike = Bike.objects.get(pk=pk)
    except Bike.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BikeSerializer(bike)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BikeSerializer(bike, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bike.delete()
        return HttpResponse(status=204)
