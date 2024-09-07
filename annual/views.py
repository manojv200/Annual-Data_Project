from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from annual.models import AnnualProduction


# Create your views here.

class ResponseApi(APIView):
    def get(self, request):
        data = request.GET
        well_no = data.get("well")
        annual_data = AnnualProduction.objects.filter(api_well_number=int(well_no)).first()
        response = {
            'oil': annual_data.total_oil,
            'gas': annual_data.total_gas,
            'brine': annual_data.total_brine,
        }
        return Response(response)
