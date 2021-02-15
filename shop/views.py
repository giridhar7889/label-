from django.shortcuts import render
from django.http import HttpResponse
from .models import product,Contact,Orders,OrderUpdate
from math import ceil
import json



def index(request):




        allprods=[]
        catprod=product.objects.values("subcategory","id","price")

        cats={item["subcategory"] for item in catprod }

       





        for cat in cats:
                products=product.objects.filter(subcategory=cat)


                print(products)


                n = len(products)
                nslides = n // 4 + ceil((n / 4) - (n // 4))
                allprods.append([products,range(1,nslides),nslides])





        params={"allprods":allprods}

        return render(request,"shop/index.html",params)

def about(request):
        return render(request, "shop/about.html")
def contact(request):
        thank=False
        if request.method=="POST":

                name=request.POST.get("name","")

                email = request.POST.get("email", "")

                phonenumber = request.POST.get("phone", "")

                desc = request.POST.get("desc", "")

                contact=Contact(name=name,email=email,phone=phonenumber,desc=desc)
                contact.save()
                thank=True

        return render(request, "shop/contact.html",{'thank':thank})

def track(request):
        if request.method == "POST":
                order_id = request.POST.get('orderId', '')
                email = request.POST.get('email', '')
                try:
                        order = Orders.objects.filter(order_id=order_id, email=email)
                        if len(order) > 0:
                                update = OrderUpdate.objects.filter(order_id=order_id)

                                updates = []
                                for item in update:
                                        updates.append({'text': item.update_desc, 'time': item.timestamp})
                                        response = json.dumps([updates,order[0].items_json], default=str)

                                return HttpResponse(response)
                        else:
                                return HttpResponse('{}')

                except Exception as e:
                        return HttpResponse('{}')
        return render(request, "shop/track.html")







def search(request):
        return render(request, "shop/search.html")
def products(request,myid ):
        products = product.objects.filter(id=myid)

        return render(request, "shop/products.html",{"product":products[0]})
def checkout(request):
        if request.method == "POST":
                items_json = request.POST.get('itemsjson', '')
                name = request.POST.get("name", "")
                email = request.POST.get("email", "")
                address1 = request.POST.get("address1", "")
                address2 = request.POST.get("address2", "")
                city = request.POST.get("city", "")
                state = request.POST.get("state", "")
                zip = request.POST.get("zip", "")
                phone_number = request.POST.get("phone", "")
                order = Orders(items_json= items_json,name=name, email=email, address1=address1, address2=address2,
                               city=city, state=state,
                               zip=zip, Phone_number=phone_number)
                order.save()
                update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
                update.save()
                thank = True
                id = order.order_id
                return render(request, "shop/checkout.html", {"thank": thank, "id": id})





        return render(request, "shop/checkout.html")


