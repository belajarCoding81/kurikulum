from rest_framework import serializers
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK2


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


class MkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MK
        fields = '__all__'


class CpmkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPMK
        fields = '__all__'


class Cpmk_MkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPMK_MK
        fields = '__all__'


class SubCpmk2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SUBCPMK2
        fields = '__all__'


class Cpmk2Serializer(serializers.ModelSerializer):
    #cpmk_mk_cpmk = Cpmk_Mk2Serializer(many=True)

    class Meta:
        model = CPMK
        fields = '__all__'


class Cpmk_Mk2Serializer(serializers.ModelSerializer):
    subcpmk2_cpmk_mk = SubCpmk2Serializer(many=True)
    cpmk = Cpmk2Serializer(read_only=True)  # Mengambil detail CPMK
    #mk = Mk2Serializer(read_only=True)

    #cpmk = serializers.StringRelatedField()

    class Meta:
        model = CPMK_MK
        fields = '__all__'


class Mk2Serializer(serializers.ModelSerializer):
    #bk = Bk2Serializer(read_only=True)
    cpmk_mk_mk = Cpmk_Mk2Serializer(many=True)

    class Meta:
        model = MK
        fields = '__all__'


class Bk2Serializer(serializers.ModelSerializer):
    #cpl = Cpl2Serializer(many=True, read_only=True)
    mk_bk = Mk2Serializer(many=True)  # Menampilkan mk

    class Meta:
        model = BK
        fields = '__all__'


class Cpl2Serializer(serializers.ModelSerializer):
    #pl = Pl2Serializer(many=True, read_only=True)

    bk_cpl = Bk2Serializer(many=True)
    # cpmk_cpl = Cpmk2Serializer(many=True)  # Menampilkan cpmk

    class Meta:
        model = CPL
        fields = '__all__'


class Pl2Serializer(serializers.ModelSerializer):
    cpl_pl = Cpl2Serializer(many=True)

    class Meta:
        model = PL
        fields = '__all__'


#MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK

#CPMK_MK, SUBCPMK, CPL_CPMK_MK
