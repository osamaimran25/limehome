
from django.db import models

# Create your models here.
class YelloTaxiTrip(models.Model):
    id                     =   models.AutoField(primary_key=True)
    VendorID               = models.BigIntegerField(blank=True, null=True)
    tpep_pickup_datetime    = models.DateTimeField(blank=True, null=True)
    tpep_dropoff_datetime   = models.DateTimeField(blank=True, null=True)
    passenger_count         = models.IntegerField(blank=True, null=True)
    trip_distance           = models.FloatField(blank=True, null=True)
    RatecodeID             = models.IntegerField(blank=True, null=True)
    store_and_fwd_flag      = models.CharField(max_length=255, blank=True, null=True)
    PULocationID           = models.IntegerField(blank=True, null=True)
    DOLocationID           = models.IntegerField(blank=True, null=True)
    payment_type            = models.IntegerField(blank=True, null=True)
    fare_amount             = models.FloatField(blank=True, null=True)
    extra                   = models.FloatField(blank=True, null=True)
    mta_tax                 = models.FloatField(blank=True, null=True)
    tip_amount              = models.FloatField(blank=True, null=True)
    tolls_amount            = models.FloatField(blank=True, null=True)
    improvement_surcharge   = models.FloatField(blank=True, null=True)
    total_amount            = models.FloatField(blank=True, null=True)
    congestion_surcharge    = models.FloatField(blank=True, null=True)



    # SELECT * FROM `app_yellotaxitrip` WHERE `A`.`total_amount` < 5.0
    # YelloTaxiTrip.objects.values('tpep_pickup_datetime__hour').annotate(total_rides=Count('tpep_pickup_datetime__hour')).order_by('-todal_rides')

    # YelloTaxiTrip.objects.filter(tolls_amount__lt=5).count()




    # YelloTaxiTrip.objects.values('tpep_pickup_datetime__hour').annotate(peak_hour_rides=Count('tpep_pickup_datetime__hour')).order_by('-peak_hour_rides')





# SELECT tpep_pickup_datetime, VendorID, tpep_pickup_datetime COUNT(EXTRACT(HOUR FROM tpep_pickup_datetime)) AS c FROM app_yellotaxitrip GROUP BY tpep_pickup_datetime, VendorID, tpep_dropoff_datetime, passenger_count, trip_distance, RatecodeID,
#  store_and_fwd_flag, PULocationID, DOLocationID, payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, 
#  improvement_surcharge, total_amount, congestion_surcharge ORDER BY c DESC


# YelloTaxiTrip.objects.aggregate(Avg('tip_amount'))

