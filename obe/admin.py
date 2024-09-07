from .forms import CPLAdminForm, BKAdminForm, MKAdminForm, CPMKAdminForm, CPMK_MKAdminForm, SUBCPMK2AdminForm, PLAdminForm
from django.contrib import admin
from .models import PL, CPL, BK, MK, CPMK, CPMK_MK, SUBCPMK2
from django.forms import CheckboxSelectMultiple
from django.db import models
#from django_select2.forms import Select2MultipleWidget
from django import forms

#from django_filters import FilterSet, ModelChoiceFilter
#from django.forms import CheckboxSelectMultiple

# Register your models here.
# admin.site.register(PL)
# admin.site.register(CPL)
# admin.site.register(BK)
# admin.site.register(MK)
# admin.site.register(CPMK)
# admin.site.register(CPMK_MK)
# admin.site.register(SUBCPMK)
# admin.site.register(CPL_CPMK_MK)


class CPMKAdmin(admin.ModelAdmin):
    form = CPMKAdminForm
    search_fields = ('kodeCpmk', 'deskripsi')


class PLAdmin(admin.ModelAdmin):
    form = PLAdminForm
    search_fields = ('kodePl', 'deskripsi')


class BKAdmin(admin.ModelAdmin):
    form = BKAdminForm
    search_fields = ('kodeBk', 'nama')


class CPLAdmin(admin.ModelAdmin):
    form = CPLAdminForm
    search_fields = ('kodeCpl', 'deskripsi')


class MKAdmin(admin.ModelAdmin):
    form = MKAdminForm
    search_fields = ('kodeMk', 'nama')


admin.site.register(PL, PLAdmin)
admin.site.register(BK, BKAdmin)
admin.site.register(CPL, CPLAdmin)
admin.site.register(MK, MKAdmin)
admin.site.register(CPMK, CPMKAdmin)


class CPMK_MKAdmin(admin.ModelAdmin):
    form = CPMK_MKAdminForm
    # Optional: Menambahkan fitur pencarian di admin Author
    list_filter = ['cpmk', 'mk', 'mk__nama', 'cpmk__deskripsi', ]
    autocomplete_fields = ['cpmk', 'mk', ]
    search_fields = ('cpmk__kodeCpmk', 'mk__kodeMk',
                     'mk__nama', 'cpmk__deskripsi',)

    class Media:
        css = {
            # Path ke CSS yang baru dibuat
            'all': ('admin/css/custom_admin.css',)
        }
        # Path ke JavaScript yang baru dibuat
        js = ('admin/js/filter_toggle.js',)


class SUBCPMK2Admin(admin.ModelAdmin):
    # Mengaktifkan fitur pencarian pada field author
    autocomplete_fields = ['cpmk_mk']
    # Filter untuk membantu pencarian lebih spesifik
    list_filter = ['cpmk_mk__mk__nama', 'cpmk_mk__cpmk__deskripsi', ]
    #attrs = {'placeholder': 'Cari di sini'}
    readonly_fields = ('kodeSubCpmk',)  # Membuat field 'name' readonly
    #form = SUBCPMKAdminForm
    search_fields = ('cpmk_mk__cpmk__kodeCpmk',
                     'cpmk_mk__mk__kodeMk', 'cpmk_mk__cpmk__deskripsi', 'deskripsi', 'kodeSubCpmk')

    class Media:
        css = {
            # Path ke CSS yang baru dibuat
            'all': ('admin/css/custom_admin.css',)
        }
        # Path ke JavaScript yang baru dibuat
        js = ('admin/js/filter_toggle.js',)


admin.site.register(CPMK_MK, CPMK_MKAdmin)
admin.site.register(SUBCPMK2, SUBCPMK2Admin)
