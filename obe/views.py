import csv
from django.http import HttpResponse

from django.shortcuts import render
from dal import autocomplete
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import generics
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK2
from .serializers import PlSerializer, CplSerializer, BkSerializer, MkSerializer, CpmkSerializer, Cpmk_MkSerializer
from .serializers import Pl2Serializer, Cpl2Serializer, Bk2Serializer, Mk2Serializer, Cpmk2Serializer, Cpmk_Mk2Serializer, SubCpmk2Serializer

# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.response import Response
# from .renderers import CSVRenderer


# @api_view(['GET'])
# @renderer_classes([CSVRenderer])
# def export_csv(request):

# Ambil data dari model
#    queryset = PL.objects.all()
#    serializer = PlSerializer(queryset, many=True)

# Kembalikan data yang diserialisasi
#    return Response(serializer.data)

class ExportCSVView(APIView):
    def get(self, request, *args, **kwargs):
        # Ambil data queryset
        pl = PL.objects.all()
        serializer = PlSerializer(pl, many=True)

        # Siapkan response HTTP untuk file CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pl.csv"'

        # Buat writer untuk menulis CSV
        writer = csv.writer(response)
        # Header CSV
        writer.writerow(['id', 'kodePl', 'deskripsi', 'aktif'])

        # Tulis data ke dalam file CSV
        for item in serializer.data:
            writer.writerow([item['id'], item['kodePl'],
                            item['deskripsi'], item['aktif']])

        return response


class PlListView(generics.ListAPIView):
    queryset = PL.objects.all()
    serializer_class = PlSerializer


# class PlViewSet(viewsets.ModelViewSet):
#    queryset = PL.objects.all()
#    serializer_class = Pl2Serializer

class PlViewSet(viewsets.ModelViewSet):
    queryset = PL.objects.all().prefetch_related(
        'cpl_pl__bk_cpl__mk_bk__cpmk_mk_mk__cpmk__cpmk_mk_cpmk', 'cpl_pl__bk_cpl__mk_bk__cpmk_mk_mk__subcpmk2_cpmk_mk'
    )
    serializer_class = Pl2Serializer


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

# CPMK_MK, SUBCPMK, CPL_CPMK_MK


class Cpmk_MkListView(generics.ListAPIView):
    queryset = CPMK_MK.objects.all()
    serializer_class = Cpmk_MkSerializer


# class Cpmk_MkViewSet(viewsets.ModelViewSet):
#    queryset = CPMK_MK.objects.prefetch_related(
#        'cpmk', 'mk', 'cpmk__cpl', 'cpmk__cpl__pl', 'mk__bk', 'mk__bk__cpl')  # Optimisasi query
#    serializer_class = Cpmk_MkSerializer

class Cpmk_MkViewSet(viewsets.ModelViewSet):
    queryset = CPMK_MK.objects.prefetch_related(
        'cpmk', 'mk', 'mk__bk', 'mk__bk__cpl', 'mk__bk__cpl__pl')
    #cpmk = CPMK_MK.objects.prefetch_related('cpmk', 'mk', 'mk__bk', 'mk__bk__cpl', 'mk__bk__cpl__pl' )
    serializer_class = Cpmk_Mk2Serializer


class SubCpmk2ListView(generics.ListAPIView):
    queryset = SUBCPMK2.objects.all()
    serializer_class = SubCpmk2Serializer
