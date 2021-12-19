from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from .models import YelloTaxiTrip
from rest_framework.response import Response
from app.serializer import TaxiTripSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

class TaxiTripView(APIView):
    # queryset = Billing.objects.all()
    serializer_class = TaxiTripSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request):
        response = dict()
        total_amount = request.query_params.get('total_amount', None)
        
        if not total_amount:
            response["status"] = "error"
            response["message"] = "total amount is required"
            return Response(status=status.HTTP_400_BAD_REQUEST, data= response)
        
        paginator = PageNumberPagination()
        paginator.page_size = 100
        
        queryset = YelloTaxiTrip.objects.filter(total_amount__lt=int(total_amount) )
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = TaxiTripSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)