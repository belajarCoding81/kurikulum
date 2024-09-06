from rest_framework import serializers
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK


class PlSerializer(serializers.ModelSerializer):
    class Meta:
        model = PL
        fields = '__all__'


class CplSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPL
        fields = '__all__'


class BkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BK
        fields = '__all__'


#MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK

class MkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MK
        fields = '__all__'


class CpmkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPMK
        fields = '__all__'

#CPMK_MK, SUBCPMK, CPL_CPMK_MK


class Cpmk_MkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPMK_MK
        fields = '__all__'


class SubCpmkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SUBCPMK
        fields = '__all__'


class Cpl_Cpmk_MkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPL_CPMK_MK
        fields = '__all__'
