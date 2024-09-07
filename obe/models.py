from django.db import models
from django.db.models import Max

# Create your models here.


class PL(models.Model):
    kodePl = models.CharField(max_length=10, unique=True)
    deskripsi = models.TextField(null=True, blank=True)
    aktif = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = '1. PL (Profil Lulusan)'

    def __str__(self):
        return self.kodePl + ' - ' + self.deskripsi


class CPL(models.Model):
    kodeCpl = models.CharField(max_length=10, unique=True)
    deskripsi = models.TextField(null=True, blank=True)
    aktif = models.BooleanField(default=True, blank=False, null=False)
    pilUnsur = [('S', 'Sikap'),
                ('P', 'Pengetahuan'),
                ('K', 'Keterampilan')]
    unsur = models.CharField(choices=pilUnsur, max_length=1)
    pl = models.ManyToManyField(PL)

    class Meta:
        verbose_name_plural = '2. CPL (Capaian Pembelajaran Lulusan)'

    def __str__(self):
        return self.kodeCpl + ' - ' + self.deskripsi


class BK(models.Model):
    kodeBk = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=250)
    pilAcuan = [('1', 'SN DIKTI'),
                ('2', 'CS2023'),
                ('3', 'Panduan Universitas'),
                ('4', 'Sumber Lain')]
    acuan = models.CharField(choices=pilAcuan, max_length=1)
    aktif = models.BooleanField(default=True, blank=False, null=False)
    cpl = models.ManyToManyField(CPL)

    class Meta:
        verbose_name_plural = '3. BK (Bahan Kajian)'

    def __str__(self):
        return self.kodeBk + '-' + self.nama


class MK(models.Model):
    bk = models.ForeignKey(BK, on_delete=models.CASCADE)
    kodeMk = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=150)
    sks = models.SmallIntegerField(null=False, blank=False)
    semester = models.SmallIntegerField(null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    aktif = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = '5. MK (Mata Kuliah)'

    def __str__(self):
        return self.kodeMk + '-' + self.nama


class CPMK(models.Model):
    cpl = models.ForeignKey(CPL, on_delete=models.CASCADE)
    kodeCpmk = models.CharField(max_length=10, unique=True)
    deskripsi = models.TextField(null=True, blank=True)
    aktif = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = '4. CPMK (Capaian Pembelajaran Mata Kuliah)'

    def __str__(self):
        return self.kodeCpmk + ' - ' + self.deskripsi


class CPMK_MK(models.Model):
    cpmk = models.ForeignKey(CPMK, on_delete=models.CASCADE)
    mk = models.ForeignKey(MK, on_delete=models.CASCADE)
    mbkm = models.BooleanField(default=False, blank=True, null=True)
    bobotMbkm = models.SmallIntegerField(null=True, blank=True)
    partisipasi = models.BooleanField(
        default=False, blank=True, null=True, help_text='Komponen Kehadiran/Quiz')
    bobotPartisipasi = models.SmallIntegerField(null=True, blank=True)
    observasi = models.BooleanField(
        default=False, blank=True, null=True, help_text='Praktek/Tugas')
    bobotObservasi = models.SmallIntegerField(null=True, blank=True)
    unjukKerja = models.BooleanField(
        default=False, blank=True, null=True, help_text='Presentasi')
    bobotUnjukKerja = models.SmallIntegerField(null=True, blank=True)
    uts = models.BooleanField(default=False, blank=True, null=True)
    bobotUts = models.SmallIntegerField(null=True, blank=True)
    uas = models.BooleanField(default=False, blank=True, null=True)
    bobotUas = models.SmallIntegerField(null=True, blank=True)
    tesLisan = models.BooleanField(
        default=False, blank=True, null=True, help_text='Tugas Kelompok')
    bobottesLisan = models.SmallIntegerField(null=True, blank=True)

    tahapPenilaian = models.CharField(max_length=250, null=True, blank=True)
    teknikPenilaian = models.CharField(max_length=250, null=True, blank=True)
    instrumen = models.CharField(max_length=250, null=True, blank=True)
    kriteria = models.CharField(max_length=250, null=True, blank=True)
    bobot = models.CharField(max_length=250, null=True, blank=True)

    aktif = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = '6. CPMK - MK'

    def __str__(self):
        return self.cpmk.kodeCpmk + ' - ' + self.mk.kodeMk + ' - ' + self.mk.nama + ' - ' + self.cpmk.deskripsi


class SUBCPMK2(models.Model):
    cpmk_mk = models.ForeignKey(CPMK_MK, on_delete=models.CASCADE,
                                help_text='Ketik Kode CPMK dan MK pada kotak search di atas untuk mempermudah penginputan')
    kodeSubCpmk = models.CharField(max_length=50, blank=True, unique=True)
    deskripsi = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = '7. SUB CPMK'

    def save(self, *args, **kwargs):
        if not self.kodeSubCpmk:
            # Ambil kode parent
            parent_code = self.cpmk_mk.cpmk.kodeCpmk + '_' + self.cpmk_mk.mk.kodeMk

            # Cari kode anak dengan prefix parent_code tertinggi
            max_code = SUBCPMK2.objects.filter(
                cpmk_mk=self.cpmk_mk).aggregate(Max('kodeSubCpmk'))

            if max_code['kodeSubCpmk__max']:
                # Ekstrak angka terakhir dari kode
                last_number = int(max_code['kodeSubCpmk__max'].split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1

            # Buat kode baru dengan format ParentCode-001, ParentCode-002, dll.
            self.kodeSubCpmk = f"{parent_code}-{new_number:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.cpmk_mk.cpmk.kodeCpmk + ' - ' + self.cpmk_mk.mk.kodeMk + ' - '+self.kodeSubCpmk + ' - ' + self.deskripsi
