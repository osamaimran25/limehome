from app.models import YelloTaxiTrip
from rest_framework import serializers




class TaxiTripSerializer(serializers.ModelSerializer):

    class Meta:
        model = YelloTaxiTrip
        fields = '__all__'