from django.shortcuts import render,redirect
from backend.models import categordb
from backend.models import productdb,categordb,admincontactdb
from WEBAPP.models import weblogindb
from django.contrib import messages

# Create your views here.

def viewhome(req):
    data=categordb.objects.all()
    return render(req,"HOME.html", {'data':data})
def viewaboutus(req):
    return render(req,"aboutus.html")
def viewacontactus(req):
    return render(req,"contactus.html")
def displaycategory(req):
    return render(req,"DISPLAYCATEGORIESPAGE.html")
def discategory(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"DISPLAYCATEGORIESPAGE.html",context)


def displayproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    return render(req,"singleproductpage.html",{'dat':data})

def displayloginpage(req):
    return render(req,"weblogin.html")

def saveweblogin(req):
    if req.method == "POST":
        una = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('pass1')
        password1 = req.POST.get('pass2')
        obj = weblogindb(UNAME=una, EMAIL=email, PASSWORD=password, CFMPASSWORD=password1)
        obj.save()
        messages.success(req,"REGISTER SUCESSFULLY")
        return redirect(displayloginpage)

def custumerlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username1')
        password_r = req.POST.get('password1')

        if weblogindb.objects.filter(UNAME=username_r, PASSWORD=password_r).exists():
            req.session['username1'] = username_r
            req.session['password1'] = password_r
            messages.success(req, "LOGIN SUCESSFULLY")
            return redirect(viewhome)
        else:
            messages.error(req, "INVALID USER")
            return render(req,'weblogin.html')

def weblogout(req):
    del req.session['username1']
    del req.session['password1']
    return redirect(displayloginpage)

def saveadmincontact(req):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        sub = req.POST.get('subject')
        msg = req.POST.get('message')
        obj=admincontactdb(NAME=na, EMAIL=email, SUBJECT=sub, MESSAGE=msg)
        obj.save()
        return redirect(viewacontactus)
