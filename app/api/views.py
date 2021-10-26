import numpy as np
#import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response

class WeightPrediction(APIView):
    def post(self, request):
        data = request.data
        height = data['height']
        gender = data['gender']
        if gender == 'Male':
            gender = 0
        elif gender == 'Female':
            gender = 1
        else:
            return Response("Gender field is invalid", status=400)
        
        lin_reg_model = ApiConfig.model
        weight_predicted = lin_reg_model.predict([[gender, height]])[0][0]
        response = {"Predicted Weight": weight_predicted}
        return Response(response, status=200)