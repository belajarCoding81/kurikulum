from .forms import CPLAdminForm, BKAdminForm, MKAdminForm, CPMKAdminForm, CPL_CPMK_MKAdminForm, SUBCPMKAdminForm
from django.contrib import admin
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK, CPL_CPMK_MK
from django.forms import CheckboxSelectMultiple
from django.db import models
#from django_select2.forms import Select2MultipleWidget
from django import forms
#from django.forms import CheckboxSelectMultiple

# Register your models here.
admin.site.register(PL)
# admin.site.register(CPL)
# admin.site.register(BK)
# admin.site.register(MK)
# admin.site.register(CPMK)
# admin.site.register(CPMK_MK)
# admin.site.register(SUBCPMK)
# admin.site.register(CPL_CPMK_MK)


class CPMKAdmin(admin.ModelAdmin):
    form = CPMKAdminForm
    search_fields = ('kodeCpmk',)


class BKAdmin(admin.ModelAdmin):
    form = BKAdminForm
    search_fields = ('kodeBk',)


class CPLAdmin(admin.ModelAdmin):
    form = CPLAdminForm
    search_fields = ('kodeCpl',)


class MKAdmin(admin.ModelAdmin):
    form = MKAdminForm
    search_fields = ('kodeMk',)


admin.site.register(BK, BKAdmin)
admin.site.register(CPL, CPLAdmin)
admin.site.register(MK, MKAdmin)
admin.site.register(CPMK, CPMKAdmin)


class CPL_CPMK_MKAdmin(admin.ModelAdmin):
    form = CPL_CPMK_MKAdminForm
    # Optional: Menambahkan fitur pencarian di admin Author
    autocomplete_fields = ['cpl', 'cpmk', 'mk', ]
    search_fields = ('cpl__kodeCpl', 'cpmk__kodeCpmk', 'mk__kodeMk',)


class SUBCPMKAdmin(admin.ModelAdmin):

    # Mengaktifkan fitur pencarian pada field author
    autocomplete_fields = ['cpl_cpmk_mk']
    #attrs = {'placeholder': 'Cari di sini'}
    readonly_fields = ('kodeSubCpmk',)  # Membuat field 'name' readonly
    #form = SUBCPMKAdminForm


admin.site.register(CPL_CPMK_MK, CPL_CPMK_MKAdmin)
admin.site.register(SUBCPMK, SUBCPMKAdmin)
