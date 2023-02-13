from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('hello/', salom_ber),
    path('', bosh_sahifa),
    path('talaba/<int:son>', bitta_talaba),
    path('muallif/<int:son>', muallif),
    path('mualliflar/', hamma_mualliflar),
    path('kitoblar/', hamma_kitoblar),
    path('kitob/<int:son>', kitoblar),
    path('recordlar/', recordlar),
    path('tirik/', tirik),
    path('sahifa/', sahifa),
    path('janr/', janri),
    path('yosh/', muallif_yosh),
    path('record/', record),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('talabalar/', hamma_talabalar),
    path('kitob_ochir/<int:son>/', kitob_ochir),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('record_ochir/<int:son>/', record_ochir),
    path('record_ochir/<int:son>/', sahifa_ochir),
    path('adminlar/', adminlar),
    path('talaba_edit/<int:son>/', talaba_edit),
    path('kitob_edit/<int:son>/', kitob_edit),
    path('talaba_edit/<int:son>/', talaba_edit),
    path('muallif_edit/<int:son>/', muallif_edit),



]