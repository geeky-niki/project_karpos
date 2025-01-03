from django.shortcuts import render
from .models import daily_transection
from django.http import JsonResponse
from django.http import HttpResponse
from .api_files.serializers import karpos_serializer #serializer
from rest_framework.decorators import api_view #decoratoe
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# def view_karpos(request):
#   daily_data = daily_transection.objects.all()
#   #dict_name ={'variable' : list(variable.values())} this variable store all the data from the model_class_name
#   data = {
#     'daily_data': list(daily_data.values())
#   }
#   return JsonResponse(data)

def external_homepage(request):
    # Specify the full path to your HTML file
    file_path = r"F:\code_world\karpos\karpos_home.html"
    try:
        with open(file_path, 'r') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    except FileNotFoundError:
        return HttpResponse("<h1>File not found. Please check the file path.</h1>", status=404)

#for all at once
@api_view(['GET','POST'])
def view_karpos(request):
    if request.method == 'GET':
        daily_data = daily_transection.objects.all()
        serializer = karpos_serializer(daily_data, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = karpos_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

  #fetching dataas per id
@api_view(['GET','PUT', 'DELETE'])
def view_karpos_by_id(request, cust_id):
    if request.method == 'GET':
        try:
            daily_data = daily_transection.objects.get(cust_id = cust_id)
        except:
            return Response({'error':'not found'}, status = status.HTTP_400_BAD_REQUEST)
        serializer = karpos_serializer(daily_data)
        return Response(serializer.data)

    if request.method == 'PUT':
        daily_data = daily_transection.objects.get(cust_id = cust_id)
        serializer = karpos_serializer(daily_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        daily_data = daily_transection.objects.get(cust_id = cust_id)
        daily_data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    
