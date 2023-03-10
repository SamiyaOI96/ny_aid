from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import response
from rest_framework import viewsets
from.models import Borough
from .models import MutualAid
from .serializers import MutualaidSerializer
from .serializers import BoroughSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
#request handler
#request->response

#class BoroughGenericView(GenericAPIView):
@api_view(['GET','POST'])
def borough(request,format=None):
    if request.method=='GET':
        boroughs=Borough.objects.all()
        serializer=BoroughSerializer(boroughs,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = BoroughSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def borough_detail(request,format=None):
    if request.method=='GET':
        id = request.query_params.get("id")
        boroughsone=Borough.objects.filter(id=id)
        serializer=BoroughSerializer(boroughsone,many=True)
        return Response(serializer.data)
    # elif request.method == 'DELETE':
    #     boroughsone.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','PUT','DELETE'])
def mutual_aid(request,format=None,):
    print(request.method)
    # mutualaids=MutualAid.objects.all()
    # serializer=MutualaidSerializer(mutualaids,many=True)
    # try:
    #     mutualaids = MutualAid.objects.get(pk=pk)
    # except MutualAid.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        id = request.query_params.get("borough_id")
        boroughs=MutualAid.objects.filter(borough_id=id)
        serializer=MutualaidSerializer(boroughs,many=True)
        return Response(serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    elif request.method=='POST':
        id = request.query_params.get("borough_id")
        requestData=request.data
        requestData["borough"]=id
        serializer = MutualaidSerializer(data=requestData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PUT':
        mutualaids=MutualAid.objects.all()
        serializer = MutualaidSerializer(mutualaids, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.query_params.get("id")
        mutualaids=MutualAid.objects.filter(id=id)
        mutualaids.delete()
        print("hello!")
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','POST','DELETE'])
def aid_detail(request,format=None):


    if request.method=='GET':
    
        id = request.query_params.get("id")
        mutualaids=MutualAid.objects.filter(id=id)
        serializer = MutualaidSerializer(mutualaids,many=True)
        
        return Response(serializer.data)
    
    elif request.method=='POST':
        id = request.query_params.get("borough_id")
        requestData=request.data
        requestData["borough"]=id
        serializer = MutualaidSerializer(data=requestData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    elif request.method=='PUT':
        id = request.query_params.get("id")
        mutualaids=MutualAid.objects.filter(id=id)
        serializer = MutualaidSerializer(mutualaids, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        id = request.query_params.get("id")
        print(id)
        mutualaids=MutualAid.objects.filter(id=id)
        serializer = MutualaidSerializer(mutualaids,many=True)
        mutualaids.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







