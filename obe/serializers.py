from rest_framework import serializers
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK2


#MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK
class SubCpmk2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SUBCPMK2
        fields = '__all__'


class Cpmk_MkSerializer(serializers.ModelSerializer):
    subcpmk2_cpmk_mk = SubCpmk2Serializer(many=True)
    cpmk = serializers.StringRelatedField()

    class Meta:
        model = CPMK_MK
        fields = '__all__'


class MkSerializer(serializers.ModelSerializer):
    cpmk_mk_mk = Cpmk_MkSerializer(many=True)

    class Meta:
        model = MK
        fields = '__all__'


class CpmkSerializer(serializers.ModelSerializer):
    cpmk_mk_cpmk = Cpmk_MkSerializer(many=True)

    class Meta:
        model = CPMK
        fields = '__all__'

#CPMK_MK, SUBCPMK, CPL_CPMK_MK


class BkSerializer(serializers.ModelSerializer):
    # cpl = CplSerializer(many=True)  # Menampilkan cpl
    mk_bk = MkSerializer(many=True)  # Menampilkan mk

    class Meta:
        model = BK
        fields = '__all__'


class CplSerializer(serializers.ModelSerializer):
    bk_cpl = BkSerializer(many=True)
    # pl = PlSerializer(many=True)  # Menampilkan pl
    cpmk_cpl = CpmkSerializer(many=True)  # Menampilkan cpmk

    class Meta:
        model = CPL
        fields = '__all__'


class PlSerializer(serializers.ModelSerializer):
    cpl_pl = CplSerializer(many=True)

    class Meta:
        model = PL
        fields = '__all__'
