from django.urls import path
from .views import PlListView, CplListView, BkListView, MkListView, CpmkListView, Cpmk_MkListView, SubCpmkListView, Cpl_Cpmk_MkListView, CPLAutocomplete

app_name = "obe"

urlpatterns = [
    path('pl/', PlListView.as_view(), name='pl-list'),
    path('cpl/', CplListView.as_view(), name='cpl-list'),
    path('bk/', BkListView.as_view(), name='bk-list'),
    path('mk/', MkListView.as_view(), name='mk-list'),
    path('cpmk/', CpmkListView.as_view(), name='cpmk-list'),
    path('cpmk_mk/', Cpmk_MkListView.as_view(), name='cpmk-mk-list'),
    path('subcpmk/', SubCpmkListView.as_view(), name='subcpmk-list'),
    path('cpl_cpmk_mk/', Cpl_Cpmk_MkListView.as_view(), name='cpl-cpmk-mk-list'),
    path('cpl-autocomplete/', CPLAutocomplete.as_view(), name='cpl-autocomplete'),
    # Cpmk_MkListView, SubCpmkListView, Cpl_Cpmk_MkListView


]
