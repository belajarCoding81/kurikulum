from django.shortcuts import render
from dal import autocomplete

# Create your views here.
from rest_framework import generics
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK
from .serializers import PlSerializer, CplSerializer, BkSerializer, MkSerializer, CpmkSerializer, Cpmk_MkSerializer, SubCpmkSerializer, Cpl_Cpmk_MkSerializer

#from rest_framework.decorators import api_view, renderer_classes
#from rest_framework.response import Response
#from .renderers import CSVRenderer


# @api_view(['GET'])
# @renderer_classes([CSVRenderer])
# def export_csv(request):

# Ambil data dari model
#    queryset = PL.objects.all()
#    serializer = PlSerializer(queryset, many=True)

# Kembalikan data yang diserialisasi
#    return Response(serializer.data)


class PlListView(generics.ListAPIView):
    queryset = PL.objects.all()
    serializer_class = PlSerializer


class CplListView(generics.ListAPIView):
    queryset = CPL.objects.all()
    serializer_class = CplSerializer


class BkListView(generics.ListAPIView):
    queryset = BK.objects.all()
    serializer_class = BkSerializer


class CPLAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CPL.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

# PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK


class MkListView(generics.ListAPIView):
    queryset = MK.objects.all()
    serializer_class = MkSerializer


class CpmkListView(generics.ListAPIView):
    queryset = CPMK.objects.all()
    serializer_class = CpmkSerializer

#CPMK_MK, SUBCPMK, CPL_CPMK_MK


class Cpmk_MkListView(generics.ListAPIView):
    queryset = CPMK_MK.objects.all()
    serializer_class = Cpmk_MkSerializer


class SubCpmkListView(generics.ListAPIView):
    queryset = SUBCPMK.objects.all()
    serializer_class = SubCpmkSerializer


class Cpl_Cpmk_MkListView(generics.ListAPIView):
    queryset = CPL_CPMK_MK.objects.all()
    serializer_class = Cpl_Cpmk_MkSerializer
