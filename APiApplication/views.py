from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status
import pandas as pd
import json
import logging

class DataTypeApiView(APIView):
    
    logger = logging.getLogger(__name__)

    def get(self, request):
        allDataTypes = list(DataType.objects.all().values())
        return Response({"Message": "List of DataTypes", "DataType List": allDataTypes})

    def post(self, request):
        if isinstance(request.data, list):
            data_list = request.data
        else:
            data_list = [request.data]

        logging.info(data_list)

        for data in data_list:
            DataType.objects.create(
                name=data.get("Name"),
                birthdate=data.get("Birthdate"),
                score=data.get("Score"),
                grade=data.get("Grade"),
                row_number=data.get("__rowNum__")
            )

        # Convert JSON data to DataFrame
        df = pd.DataFrame(data_list)
        
        logging.info("Data types before inference:")
        logging.info(df.dtypes)

        for col in df.columns:
            # Attempt to convert to numeric first
            df_converted = pd.to_numeric(df[col], errors='coerce')
            if not df_converted.isna().all():  # If at least one value is numeric
                df[col] = df_converted
                continue

            # Attempt to convert to datetime
            try:
                df[col] = pd.to_datetime(df[col], format='%Y-%m-%d')
                continue
            except (ValueError, TypeError):  # Corrected typo here
                pass

            # Check if the column should be categorical
            if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
                df[col] = pd.Categorical(df[col])
      
        logging.info(df)
        logging.info("\nData types after inference:")
        logging.info(df.dtypes)
        
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
