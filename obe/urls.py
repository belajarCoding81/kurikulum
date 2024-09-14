from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PlListView, CplListView, BkListView, MkListView, CpmkListView, Cpmk_MkListView, SubCpmk2ListView, CPLAutocomplete, Cpmk_MkViewSet, PlViewSet, ExportCSVView
# PlListView2,

app_name = "obe"

router = DefaultRouter()
router.register(r'cpmk_mk2', Cpmk_MkViewSet)
router.register(r'pl2', PlViewSet)


urlpatterns = [
    path('pl/', PlListView.as_view(), name='pl-list'),
    #path('pl2/', PlListView2.as_view(), name='pl-list2'),
    path('cpl/', CplListView.as_view(), name='cpl-list'),
    path('bk/', BkListView.as_view(), name='bk-list'),
    path('mk/', MkListView.as_view(), name='mk-list'),
    path('cpmk/', CpmkListView.as_view(), name='cpmk-list'),
    path('cpmk_mk/', Cpmk_MkListView.as_view(), name='cpmk-mk-list'),
    #path('cpmk_mk2/', Cpmk_MkViewSet.as_view(), name='cpmk-mk-viewset'),

    path('', include(router.urls)),

    path('export-csv/', ExportCSVView.as_view(), name='export-csv'),

    path('subcpmk/', SubCpmk2ListView.as_view(), name='subcpmk-list'),
    path('cpl-autocomplete/', CPLAutocomplete.as_view(), name='cpl-autocomplete'),
    # Cpmk_MkListView, SubCpmkListView, Cpl_Cpmk_MkListView


]
