from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from dal import autocomplete
from django.forms import CheckboxSelectMultiple
from .models import PL, BK, MK, CPL, CPMK, CPMK_MK, SUBCPMK2
from django_select2.forms import Select2MultipleWidget


class BKAdminForm(forms.ModelForm):
    class Meta:
        model = BK
        fields = '__all__'
        widgets = {
            'cpl': Select2MultipleWidget(attrs={'data-placeholder': 'Cari di sini'}),
        }
# Bisa dibuat Select2 ini harus pakai:
# pip install django-select2
# Buat di Form seperti di BKAdmin di atas
# class CPLAutocomplete(autocomplete.Select2QuerySetView):
# path('cpl-autocomplete/', CPLAutocomplete.as_view(), name='cpl-autocomplete'),


class CPLAdminForm(forms.ModelForm):
    class Meta:
        model = CPL
        fields = '__all__'
        widgets = {
            'pl': Select2MultipleWidget(attrs={'data-placeholder': 'Cari di sini'}),
        }


class MKAdminForm(forms.ModelForm):
    class Meta:
        model = MK
        fields = '__all__'
        widgets = {
            'cpl': Select2MultipleWidget(attrs={'data-placeholder': 'Cari di sini'}),
            # 'bk': Select2MultipleWidget(attrs={'data-placeholder': 'Cari di sini'}),
        }


class CPMK_MKAdminForm(forms.ModelForm):
    class Meta:
        model = CPMK_MK
        fields = '__all__'


class CPMKAdminForm(forms.ModelForm):
    class Meta:
        model = CPMK
        fields = '__all__'
        widgets = {
            # Karena Foreign Key maka bukan many to many
            # 'cpl': Select2MultipleWidget(attrs={'data-placeholder': 'Cari di sini'}),
        }


class PLAdminForm(forms.ModelForm):
    class Meta:
        model = PL
        fields = '__all__'


class SUBCPMK2AdminForm(forms.ModelForm):
    class Meta:
        model = SUBCPMK2
        fields = '__all__'
        widgets = {
            'cpmk_mk': Select2MultipleWidget(attrs={'data-placeholder': 'Cari di sini'}),
        }
