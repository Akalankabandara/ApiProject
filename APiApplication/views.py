from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status

class DataTypeApiView(APIView):

    def get(self, request):
        allDataTypes = list(DataType.objects.all().values())
        return Response({"Message": "List of DataTypes", "DataType List": allDataTypes})

    def post(self, request):
        if isinstance(request.data, list):
            data_list = request.data
        else:
            data_list = [request.data]

        for data in data_list:
            DataType.objects.create(
                name=data.get("Name"),
                birthdate=data.get("Birthdate"),
                score=data.get("Score"),
                grade=data.get("Grade"),
                row_number=data.get("__rowNum__")
            )
        
        DType = DataType.objects.all().values()
        return Response({"Message": "New DataTypes Added!", "DataType": list(DType)})

    def put(self, request, pk):
        try:
            instance = DataType.objects.get(pk=pk)
        except DataType.DoesNotExist:
            return Response({"Message": f"DataType with id {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DataTypeSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": f"DataType with id {pk} updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            instance = DataType.objects.all()
            instance.delete()
            return Response({"Message": f"DataType deleted successfully."})
        except DataType.DoesNotExist:
            return Response({"Message": f"DataType does not exist."}, status=status.HTTP_404_NOT_FOUND)
