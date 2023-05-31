from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Pets,Products,Register_User,Cart,Pay,Address,Order
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum








'''def view_pets_user(request):
    data=Pets.objects.all()
    return render(request,"show_pets.html",{'data':data})'''




def add_pets(request):
    if request.method=="POST" and request.FILES:
        PetType=request.POST['pettype']
        Breed=request.POST['breed']
        PhotoPet=request.FILES['petphoto']
        PetName=request.POST['petname']
        SpecialCare=request.POST['special']
        Price=request.POST['price']
        Status="0"
        add=Pets(PetType=PetType,Breed=Breed,PhotoPet=PhotoPet,PetName=PetName,SpecialCare=SpecialCare,Price=Price,Status=Status)
        add.save()
        return redirect('view_pets')
    
def view_pets(request):
    data=Pets.objects.all()
    return render(request,"pet_data.html",{'data':data})


def add_products(request):
    print('hello')
    if request.method=="POST" and request.FILES:
        ProductType=request.POST['prodtype']
        PetType=request.POST['pettype']
        PhotoProd=request.FILES['photoprod']
        Size=request.POST['size']
        Quantity=request.POST['quantity']
        Price=request.POST['price']
        Status="0"
        data=Products(ProductType=ProductType,PetType=PetType,PhotoProd=PhotoProd,Size=Size,Quantity=Quantity,Price=Price,Status=Status)
        print(data)
        data.save()
        return redirect('view_products')

def view_products(request):
    data=Products.objects.all()
    return render(request,"product_data.html",{'data':data})





def order_pay(request):
    photo=""
    petname=""
    price=""
    quantity=""


    if request.user:
        user=request.user
        carts=Cart.objects.all().filter(user=user,cart_status=0).values()
        print(carts)

        tot = carts.aggregate(total=Sum('price'))['total']
        total=str(tot)

            
        
        for i in carts:
            petname=i['petname']
            photo=i['photo']
            price=i['price']
            quantity=i['quantity']
            total=total
            order_status="1"
            details=Order(user=user,photo=photo,petname=petname,price=price,quantity=quantity,total=total,order_status=order_status)
            details.save()  
            
        return render(request,'address.html')
             

        

def payment(request):
        if request.user:
           user=request.user
        if request.method == 'POST':
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            address=request.POST['address']
            city=request.POST['city']
            State=request.POST['state']
            zip=request.POST['zip']
        details=Address(user=user,firstname=firstname,lastname=lastname,address=address,city=city,State=State,zip=zip)
        details.save()
        Data=Order.objects.all().filter(user=user).values()
        for i in Data:
            tot=i['total']
        return render(request,'payment.html',{'Data':Data,'tot':tot})

def add_to_cart_pet(request,id):
    if request.user:
        user=request.user
        cart=Cart.objects.filter(user=user,Pets=id)
        if cart.exists():
            return HttpResponse('item already in cart')
        else:
            Data=Pets.objects.all().filter(id=id).values()
            print(Data)
            for i in Data:
                PetName=i['PetName']
                PhotoPet=i['PhotoPet']
                Price=i['Price']
                p_id=i['id']
                
            pet = Pets.objects.get(id=p_id)
            cart_status="0"
            
            details=Cart(user=user,Pets=pet,photo=PhotoPet,petname=PetName,price=Price,cart_status=cart_status)
            details.save()
            return redirect('cart_page')
        
def cart_page(request):
    data=Cart.objects.all()
    return render(request,'cart.html',{'data':data})

def add_to_cart_product(request,id):
    if request.user:
        user=request.user
        cart=Cart.objects.filter(user=user,Pets=id)
        if cart.exists():
            return HttpResponse('item already in cart')
        else:
            Data=Products.objects.all().filter(id=id).values()
            print(Data)
            for i in Data:
                ProductType=i['ProductType']
                PhotoProd=i['PhotoProd']
                Price=i['Price']
                p_id=i['id']
            product = Products.objects.get(id=p_id)
            cart_status="0"
            
            details=Cart(user=user,Products=product,photo=PhotoProd,petname=ProductType,price=Price,cart_status=cart_status)
            details.save()
            return redirect('cart_page')
        

def buy_page(request,id):
    Data=Pets.objects.get(id=id)
    for i in Data:
        PetName=i['petname']
        Price=i['price']
        details=Pets(PetName=PetName,Price=Price)
        details.save()
        return redirect('orders_page')
    

def index(request):
    return render(request,"login.html")
    

def delete_pet(request,id):
    add=Pets.objects.get(id=id)
    add.delete()
    return redirect('view_pets')

def edit(request,id):
    Data=Pets.objects.get(id=id)
    return render(request,'pet_edit.html',{'Data':Data})



def edit_pet(request,id):
    if request.method=="POST":
        add=Pets.objects.get(id=id)
        add.PetType=request.POST['pettype']
        add.Breed=request.POST['breed']
        add.PhotoPet=request.POST['petphoto']
        add.PetName=request.POST['petname']
        add.SpecialCare=request.POST['special']
        add.Price=request.POST['price']
        add.save()
        return redirect('view_pets')

def register_page(request):
    return render(request,'customerregister.html')

def login_page(request):
    return render(request,'login.html')

def owner_page(request):
    return render(request,'owner_index.html')

def customer_page(request):
    return render(request,'customer_index.html')

def show_pets(request):
    data=Pets.objects.all()
    return render(request,"show_pets.html",{'data':data})

def show_products(request):
    data=Products.objects.all()
    return render(request,"show_products.html",{'data':data})

def addpets_page(request):
    return render(request,'pet.html')

def addproducts_page(request):
    return render(request,'petproduct.html')

def address_page(request):
    return render(request,'address.html')

def pay_page(request): 
    return render(request,'payment.html')

def payment_page(request):
    data=Order.objects.all()
    print(data)
    return render(request,'payment.html',{'data':data})

def otp_page(request):
    return render(request,'otp.html')

def thankyou_page(request):
    return render(request,'thankyou.html')



def search_pet(request):
    query=request.GET["query1"]
    Data=Pets.objects.filter(Breed__icontains=query)
    return render(request,'show_pets_search.html',{'Data':Data})

def search_product(request):
    query=request.GET["query1"]
    Data=Products.objects.filter(PetType__icontains=query)
    return render(request,'show_products_search.html',{'Data':Data})

def userregister(request):
    if request.method == 'POST':
        Email=request.POST['email']
        Name=request.POST['name']
        Gender=request.POST['gender']
        Username=request.POST['uname']
        Password1=request.POST['password1']
        Password2=request.POST['password2']
        role="customer"
        status="0"

        if Password1==Password2:
            if User.objects.filter(username=Username).exists():
                
                return redirect('register_page')
            
            elif User.objects.filter(email=Email).exists():
                return redirect('register_page')
            else:
                user=User.objects.create_user(username=Username,password=Password1)
                user.save()
                print(user)

                userDetail=Register_User(user=user,Email=Email,Name=Name,Gender=Gender,Username=Username,Password1=Password1,Password2=Password2,role=role,status=status)
                userDetail.save()
                print(userDetail)

                print('user created')
        else:
            return redirect('register_page')
        return redirect('login_page')
    else:
        return render(request,'customerregister.html')
    
role=''
stat=''  
def userlogin(request):
    global role
    global stat
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')

        data=User.objects.filter(username=username).values()
        print("userModeData==>",data)
        for i in data:
            u_name=i['username']
            id=i['id']

            d=Register_User.objects.filter(user_id=id).values()
            print('userdata==>',d)
            for i in d:
                stat=i['status']
                role=i['role']

            user=authenticate(username=username,password=password)

            if user is not None and role=="customer" and username==u_name and stat=="0":
                auth_login(request,user)
                return render(request,'customer_index.html')
            
            elif user is not None and username=="admin" and password=="admn123":
                return render(request,'owner_index.html')
            
            else:pass
        return render(request,'login.html')
    else:
        messages.info(request,'Invalid Credentials')
        return redirect('login_page')
        
def logout(request):
    return render(request,'login.html')
