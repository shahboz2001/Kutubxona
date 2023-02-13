from django.db import models

class Muallif(models.Model):
    j=[("erkak","erkak"),("ayol","ayol")]
    ism=models.CharField(max_length=50)
    t = [("ha","ha"), ("yoq", "yoq")]
    tirik=models.CharField(max_length=50,choices=t)
    kitob_soni=models.PositiveIntegerField()
    jinsi=models.CharField(max_length=50,choices=j)
    tugulgan_sana=models.DateField()
    def __str__(self):
        return self.ism
class Talaba(models.Model):
    b=[("ha","ha"),("yoq","yoq")]
    ism=models.CharField(max_length=50)
    bitiruvchi=models.CharField(max_length=50,choices=b)
    kitoblar_soni=models.PositiveIntegerField(default=0)
    kurs=models.PositiveIntegerField()
    def __str__(self):
        return self.ism
class Admin(models.Model):
    ism=models.CharField(max_length=50)
    ish_vaqti=models.TimeField()
    def __str__(self):
        return self.ism
class Kitob(models.Model):
    nom=models.CharField(max_length=100)
    sahifa=models.PositiveIntegerField()
    muallif=models.ForeignKey(Muallif,on_delete =models.CASCADE)
    janr=models.CharField(max_length=100,)
    def __str__(self):
        return self.nom
class Record(models.Model):
    q=[("ha","ha"),("yoq","yoq")]
    telaba=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    qaytarish_sanasi=models.DateField()
    qayterdi=models.CharField(max_length=50,choices=q)
    def __str__(self):
        return self.olingan_sana
# class Nashriyot(models.Model):
#     nom=models.CharField(max_length=50)
#     manzil=models.CharField(max_length=100)
#     def __str__(self):
#         return self.nom
# class Kitob1(models.Model):
#     nom=models.CharField(max_length=50)
#     narx=models.BigIntegerField()
#     kelgan_sana=models.DateField()
#     nashriyot=models.ForeignKey(Nashriyot,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.nom
# class Sotuvchi(models.Model):
#     ism=models.CharField(max_length=50)
#     tel=models.CharField(max_length=13)
#     def __str__(self):
#         return self.ism
# class Sotuv(models.Model):
#     kitob=models.ForeignKey(Kitob1,on_delete=models.CASCADE)
#     sotuvchi=models.ForeignKey(Sotuvchi,on_delete=models.CASCADE)
#     sana=models.DateField()
