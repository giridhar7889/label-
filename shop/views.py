from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact
from math import ceil

# Create your views here.

def index(request):
        #products=product.objects.all()




        allprods=[]
        catprod=product.objects.values("subcategory","id")

        cats={item["subcategory"] for item in catprod}

        for cat in cats:
                products=product.objects.filter(subcategory=cat)

                print(products)
                n = len(products)
                nslides = n // 4 + ceil((n / 4) - (n // 4))
                allprods.append([products,range(1,nslides),nslides])



        #params = {'no_of_slides':nslides,'range':range(1,nslides),'products': products}
        #allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
        params={"allprods":allprods}

        return render(request,"shop/index.html",params)

def about(request):
        return render(request, "shop/about.html")
def contact(request):
        if request.method=="POST":
                print(request)
        name=request.POST.get("name","")

        email = request.POST.get("email", "")

        phonenumber = request.POST.get("phone", "")

        desc = request.POST.get("desc", "")

        contact=Contact(name=name,email=email,phone=phonenumber,desc=desc)
        contact.save()

        return render(request, "shop/contact.html")

def track(request):
        return render(request, "shop/track.html")
def search(request):
        return render(request, "shop/search.html")
def products(request,myid ):
        products = product.objects.filter(id=myid)

        return render(request, "shop/products.html",{"product":products[0]})
def checkout(request):
        return render(request, "shop/checkout.html")


