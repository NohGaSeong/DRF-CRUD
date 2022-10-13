from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Address
from .serializers import AddressSerializers

def address_list(request):
    if request.method == 'GET':
        query_set = Address.objects.all()
        serializer = AddressSerializers(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse(serializer.errors, status = 400)

