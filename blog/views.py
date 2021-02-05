from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.


def index(request):

        return render(request,"blog/index.html")

def product(request):
        products = product.objects.all()
        return render(request,"shop/test.html",{"products":products})

