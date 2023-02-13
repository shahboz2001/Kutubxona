from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *

def salomlash(request):
    return HttpResponse("Salom, Dunyo")
def salom_ber(request):
    data = {"ism": "Islom", "ismlar": ["Akbar", 'Davlat', 'Eldor']}
    return render(request,"salom.html",data)
def  bosh_sahifa(request):
    return render(request,'bosh_sahifa.html')
def bitta_talaba(request,son):
    data={"talaba":Talaba.objects.get(id=son)}
    return render(request, 'bitta_talaba.html', data)
def hamma_talabalar(request):
    if  request.method=="POST":
        Talaba.objects.create(
            ism=request.POST.get('i'),
            kurs=request.POST.get('k'),
            kitoblar_soni=request.POST.get('k_s'),
            bitiruvchi=False
        )
        return redirect("/talaba/")
    soz = request.GET.get('qidirish')
    if soz  is None:
        st=Talaba.objects.all()
    else:
        st=Talaba.objects.filter(ism__contains=soz)
    data={"talabalar":st}
    return render(request, 'talabalar.html',data)
def muallif(request,son):
    data={"muallif":Muallif.objects.get(id=son)}
    return render(request,'muallif.html',data)
def hamma_mualliflar(request):
    if  request.method=="POST":
        forma=Muallifform(request.POST)
        if forma.is_valid():
            Muallif.objects.create(
                ism=forma.cleaned_data.get('ism'),
                tirik=forma.cleaned_data.get('tirik'),
                kitob_soni=forma.cleaned_data.get('kitob_soni'),
                jinsi=forma.cleaned_data.get('jinsi'),
                tugulgan_sana=forma.cleaned_data.get('tugulgan_sana')
            )
        return redirect("/mualliflar/")
    soz=request.GET.get('qidirish')
    if soz is None:
        st=Muallif.objects.all()
    else:
        st=Muallif.objects.filter(ism__contains=soz)
    data={"mualliflar":st,"forma":Muallifform()}
    return render(request,'hamma_mualliflar.html',data)
def hamma_kitoblar(request):
    if request.method=="POST":
        forma=KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/kitoblar/')

    soz = request.GET.get('qidirish')
    if soz is None:
        st = Talaba.objects.all()
    else:
        st = Kitob.objects.filter(ism__contains=soz)
    data={"kitoblar":Kitob.objects.all(),"mualliflar":Muallif.objects.all(),"forma":KitobForm()}
    return render(request,"hamma_kitoblar.html",data)

def kitoblar(request,son):
    data={"kitob":Kitob.objects.get(id=son)}
    return render(request,"kitob.html",data)
def recordlar(request):
    if request.method == "POST":
        forma = RecordForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/recordlar/')

    data={"recordlar1":Record.objects.all(),
          "talabalar":Talaba.objects.all(),
          "kitoblar":Kitob.objects.all(),
          "adminlar":Admin.objects.all(), }
    return render(request,"recordlar.html",data)
def tirik(request):
    data={"tirik1":Muallif.objects.filter(tirik="ha")}
    return render(request,"tirik.html",data)
def sahifa(request):
    data={"sahifa1":Record.objects.filter(telaba__bitiruvchi="ha")}
    return render(request,"sahifa.html",data)
def janri(request):
    data={"janr":Kitob.objects.filter(janr="badiiy")}
    return render(request,"janr.html",data)
def muallif_yosh(request):
    data={"yosh":Muallif.objects.order_by("tugulgan_sana")[0:3]}
    return render(request,"muallif1.html",data)
def record(request):
    data={"record1":Record.objects.all()}
    return render(request,"bitta_recordd.html")
def talaba_ochir(request,son):
    Talaba.objects.get(id=son).delete()
    return redirect('/talaba/')
def kitob_ochir(request,son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitoblar/')
def muallif_ochir(request,son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar/')
def record_ochir(request,son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar/')
def sahifa_ochir(request,son):
    Kitob.objects.get(id=son).delete()
    return redirect('/sahifa/')

def adminlar(request):
    if request.method == "POST":
        forma = Adminform(request.POST)
        if forma.is_valid():
            Admin.objects.create(
                ism=forma.cleaned_data.get('ism'),
                ish_vaqti=forma.cleaned_data.get('ish_vaqti'))
        return redirect("/adminlar/")
    data={"admin":Admin.objects.all()}
    return render(request,"admin.html",data)
def talaba_edit(request,son):
    if request.method=="POST":
        if request.POST.get('b')=="on":
            bitiruvchi_qiymati="ha"
        else:
            bitiruvchi_qiymati="yoq"

        Talaba.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            kurs=request.POST.get('k'),
            kitoblar_soni=request.POST.get('k_s'),
            bitiruvchi=bitiruvchi_qiymati

        )
        return redirect("/talaba/")

    data={"talaba":Talaba.objects.get(id=son)}
    return render(request,'talaba_edit.html',data)
def kitob_edit(request,son):
    if request.method=="POST":
        Kitob.objects.filter(id=son).update(
            nom=request.POST.get('n'),
            sahifa=request.POST.get('s'),
            janr=request.POST.get('j'),
            muallif=Muallif.objects.get(id=request.POST.get('m'))
        )
        return redirect('/kitoblar/')

    data={"mualliflar":Muallif.objects.get(id=son),
        "kitob":Kitob.objects.get(id=son)}
    return render(request,"kitob_edit.html",data)
def admin_edit(request,son):
    if request.method=="POST":
        Admin.objects.filter(id=son).update(
        ism = request.POST.get('i'),
        ish_vaqti = request.POST.get('t')
        )
        return redirect('/adminlar/')

    data={"admin":Admin.objects.get(id=son)}
    return render(request,"admin_edit.html",data)
def muallif_edit(request,son):
    data={"muallif":Muallif.objects.get(id=son)}
    return render(request,"muallif_edit.html",data)