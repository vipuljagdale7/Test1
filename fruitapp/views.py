import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *


# Create your views here.


def homepage(request):   
    if request.method == "POST":
        fruit_name = request.POST.get("fname")          # fname come form front end
        fruit_price = request.POST.get("fprice")
        fruit_qty = request.POST.get("fqty")
        fruit_is_available = request.POST.get("favailable")
        fruit_id = request.POST.get("fid")
        if not fruit_id:

        # print(fruit_name, type(fruit_price), fruit_qty, fruit_is_available)
            if fruit_is_available == "Yes":
                fruit_is_available = True
            else:
                fruit_is_available = False
            fruit_obj = Fruit(name=fruit_name, price=float(fruit_price), qty=int(fruit_qty), is_available=fruit_is_available)
            fruit_obj.save()
            return redirect("show_fruits")
            # return HttpResponse("Fruit added successfully...!") # manually status managein backend
        else:
            fruit_obj = Fruit.objects.get(id=fruit_id)
            fruit_obj.name = fruit_name
            fruit_obj.price = fruit_price
            fruit_obj.qty = fruit_qty
            if fruit_is_available == "Yes":
                fruit_is_available = True
            else:
                fruit_is_available = False
            fruit_obj.is_available = fruit_is_available
            fruit_obj.save()
            # return HttpResponse("Fruits updated successfully...!")
            return redirect("show_fruits")
    else:
        # return render(request, "home.html") # context

        # for bootstrap 
        return render(request, "bootstrap_practice.html") # context


def show_fruits(request):
    fruits = Fruit.objects.all()
    # fruits = ActiveF.all()
    return render(request, "show_fruits.html",{"all_fruits":fruits})        # 'is_active':False

def edit_fruit(request, pk):
    fruit_obj = Fruit.objects.get(id=pk)
    return render(request, "home.html", {"fruit": fruit_obj})


def delete_fruit(request, pk):
    fruit_obj = Fruit.objects.get(id=pk)
    fruit_obj.delete()
    return redirect(request,"show_fruits")

def soft_delete(request, pk):
    fruit_obj = Fruit.objects.get(id=pk)
    fruit_obj.is_delete = 1
    fruit_obj.save()
    return redirect(request,"show_fruits")


def available_fruit(request):
    f_obj = Fruit.available_fruits.all()
    return render(request,"available_fruit.html",{"avl_fruits":f_obj}) 

def not_available_fruit(request):
    f_obj = Fruit.not_available_fruits.all()
    return render(request,"not_available_fruit.html",{"not_avl_fruits":f_obj}) 



# from django.views import View

# class Home(View):
#     def get(self,request):
#         print("In Get method")
#         return HttpResponse("In Get method")

#     def post(self,request):
#         # print(dir(request))
#         print(request.user)
#         print("In Post method",request.body)    # request.body ---jab row data passed or request.POST - jab hm form data pass karte hai
#                                                 # decode("utf-8") -- toconvert bytes to  str
#         # print(request.FILES)
#         return HttpResponse("In Post method",status=201)

#     def put(self,request):
#         print("In Put method")
#         return HttpResponse("In Put method")

#     def delete(self,request):
#         print("In Delete method")
#         return HttpResponse("In Delete method",status=204)

#     def patch(self,request):
#         print("In Patch method")
#         return HttpResponse("In Patch method")

