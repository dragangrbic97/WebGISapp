from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import SolarPanel, WindPowerPlant, LastUser


class SolarPanelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SolarPanel
        geo_field = 'geometry'
        fields = '__all__'
        read_only_fields = ('id', 'creation_date', 'modification_date')


class WindPowerPlantSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WindPowerPlant
        geo_field = 'geometry'
        fields = '__all__'
        read_only_fields = ('id', 'creation_date', 'modification_date')


class ChoiceSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
    name = serializers.CharField(max_length=24)

    class Meta:
        fields = ('code', 'name')


class LastUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastUser
        fields = ('creation_date', 'modification_date')


class ShapeFileWindPowerPlantSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner_name', required=True)
    manuf = serializers.CharField(source='manufacturer', required=True)
    note = serializers.CharField(source='note', required=False)
    entity = serializers.CharField(source='entity', required=False)
    canton = serializers.CharField(source='canton', required=False)
    city = serializers.CharField(source='city', required=False)
    zone = serializers.CharField(source='zone', required=False)
    altitude = serializers.FloatField(source='altitude', required=False)
    wind_direc = serializers.FloatField(source='wind_direction', required=False)
    power_supp = serializers.FloatField(source='power_supplied', required=False)

    class Meta:
        model = WindPowerPlant
        fields = ('owner_name', 'manuf', 'note', 'entity', 'canton', 'city', 'zone', 'altitude', 'wind_direc', 'power_supp')





