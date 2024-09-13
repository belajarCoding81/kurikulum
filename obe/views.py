from django.shortcuts import render
from dal import autocomplete
from rest_framework import viewsets

# Create your views here.
from rest_framework import generics
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK2
from .serializers import PlSerializer, CplSerializer, BkSerializer, MkSerializer, CpmkSerializer, Cpmk_MkSerializer, SubCpmk2Serializer

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


class PlViewSet(viewsets.ModelViewSet):
    # queryset = Kabupaten.objects.all().prefetch_related(
    queryset = PL.objects.all().prefetch_related(
        'cpl_pl__bk_cpl__mk_bk__cpmk_mk_mk__subcpmk2_cpmk_mk', 'cpl_pl__bk_cpl__mk_bk__cpmk_mk_mk__cpmk')
    # PlListView2(generics.ListAPIView):
    #queryset = PL.objects.prefetch_related('cpl')
    # 'pl__cpl__bk__mk__cpmk_mk__cpmk'
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


class Cpmk_MkViewSet(viewsets.ModelViewSet):
    queryset = CPMK_MK.objects.prefetch_related(
        'cpmk', 'mk', 'cpmk__cpl', 'cpmk__cpl__pl', 'mk__bk', 'mk__bk__cpl')  # Optimisasi query
    serializer_class = Cpmk_MkSerializer


class SubCpmk2ListView(generics.ListAPIView):
    queryset = SUBCPMK2.objects.all()
    serializer_class = SubCpmk2Serializer
