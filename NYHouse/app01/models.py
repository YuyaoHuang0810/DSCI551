from django.db import models


class Property(models.Model):
    Id = models.IntegerField()
    BROKERTITLE = models.CharField(max_length=255)
    TYPE = models.CharField(max_length=50)
    PRICE = models.DecimalField(max_digits=15, decimal_places=2)
    BEDS = models.IntegerField()
    BATH = models.DecimalField(max_digits=5, decimal_places=2)  # 浴室可以是小数
    PROPERTYSQFT = models.IntegerField()
    ADDRESS = models.CharField(max_length=255)
    STATE = models.CharField(max_length=50)
    MAIN_ADDRESS = models.CharField(max_length=255)
    ADMINISTRATIVE_AREA_LEVEL_2 = models.CharField(max_length=50)
    LOCALITY = models.CharField(max_length=50)
    SUBLOCALITY = models.CharField(max_length=50)
    STREET_NAME = models.CharField(max_length=255)
    LONG_NAME = models.CharField(max_length=255)
    FORMATTED_ADDRESS = models.CharField(max_length=512)
    LATITUDE = models.DecimalField(max_digits=9, decimal_places=6)
    LONGITUDE = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = 'properties'
