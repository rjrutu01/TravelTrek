from django.shortcuts import render,redirect,HttpResponse
from traveltrekapp.models import destination,book_now,feedback
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required 
from django.core.mail import get_connection,EmailMessage
from django.conf import settings
import random

# Create your views here.


def create_destination(request):
    if request.method == 'GET':
        return render(request,'create_destination.html')
    else:
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        request.session['image']=image
        category=request.POST['category']
        
        p=destination.objects.create(name=name,description=description,price=price,image=image,category=category)
        p.save()
        
        return redirect('/read_destination')
    
def index(request):
    d=destination.objects.all()
    context={}
    context['data']=d
    return render(request,'index.html',context)
    
def read_destination(request):
    p=destination.objects.all()
    context={}
    context['data']=p
    return render(request,'read_destination.html',context)

def user_destination(request):
    p=destination.objects.all()
    context={}
    context['data']=p
    return render(request,'user_destination.html',context)
    
def delete_destination(request,rid):
    p=destination.objects.filter(id=rid)
    p.delete()
    return redirect('/read_destination')

def update_destination(request,rid):
    if request.method == 'GET':
        p=destination.objects.filter(id=rid)
        context={}
        context['data']=p
        return render(request,'update_destination.html',context)
    else:
        name=request.POST['uname']
        description = request.POST['udescription']
        price = request.POST['uprice']
        category=request.POST['ucategory']
        
        p=destination.objects.filter(id=rid)
        p.update(name=name,description=description,price=price,category=category)

        return redirect('/read_destination')

    
    

def sign_up(request):
    if request.method=='GET':
        return render(request,'sign_up.html')
    else:
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password==confirm_password:
            u=User.objects.create(username=username,email=email,first_name=first_name,last_name=last_name)
            u.set_password(password)
            u.save()
            return redirect('/')
        else:
            context={}
            context['error']='Password and Confirm password does not match'
            return render(request,'sign_up.html',context)
        
        
def sign_in(request):
    if request.method =='GET':
        return render(request,'sign_in.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context={}
            context['error']='Username and password not found'
            return render(request,'sign_in.html',context)
        
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def create_book(request,rid):
    if request.method=='GET':
        return render(request,'booking.html')
    else:
        p=destination.objects.get(id=rid)
        book=book_now.objects.filter(destination=p,user=request.user).exists()
        if book:
            return redirect('/read_destination')
        else:
            user=User.objects.get(username=request.user)
            
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            person=request.POST['person']
            
            total_price=p.price * int(person)
            
            b=book_now.objects.create(user=user,destination=p,total_price=total_price,name=name,email=email,phone=phone,person=person)
            b.save()
                
            return redirect('/read_book')
        
@login_required(login_url='/login')
def read_book(request):
    if request.user.is_staff:
        book=book_now.objects.all()
    else:
        book=book_now.objects.filter(user=request.user)
    context={}
    context['data']=book
    return render(request,'read_booking.html',context)

def delete_book(request,rid):
    book=book_now.objects.get(id=rid)
    book.delete()
    return redirect('/read_book')

def update_book(request,rid):
    book=book_now.objects.get(id=rid)
    if request.method=='GET':
        context={}
        context['data']=book
        return render(request,'update_booking.html',context)
    else:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        person=request.POST['person']
        
        b=book_now.objects.filter(id=rid)
        b.update(name=name,email=email,phone=phone,person=person)
        
        return redirect('/read_book')
    
def create_feedback(request,rid):
    Destination=destination.objects.get(id=rid)
    feed=feedback.objects.filter(user=request.user,destination=Destination).exists()
    if feed:
        return HttpResponse('review already exist')
    else:
        if request.method =='GET':
            return render(request,'create_feedback.html')
        else:
            title=request.POST['title']
            content=request.POST['content']
            rating=request.POST['rate']
            image=request.FILES['image']
            
            d=destination.objects.get(id=rid)
            Feedback=feedback.objects.create(destination=d,title=title,content=content,rating=rating,image=image,user=request.user)
            Feedback.save()
            
            return HttpResponse('Review Added')
        
def read_feedback(request):
    p=feedback.objects.all()
    context={}
    context['review']=p
    return render(request,'read_feedback.html',context)
        
def read_destination_deatails(request,rid):
    Destination=destination.objects.filter(id=rid)
    d=destination.objects.get(id=rid)
    
    n=feedback.objects.filter(destination=d).count()
    Feedback=feedback.objects.filter(destination=d)
    sum=0
    for x in Feedback:
        sum+=x.rating
    
    try:
        avg=int(sum/n)
        avg_r=sum/n
    except:
        print('No feedback')
        
    context={}
    context['data']=Destination
    if n==0:
        context['avg']='5'
    else:
        context['avg_rating']=avg
        context['avg']=avg_r
    return render(request,'read_destination_detail.html',context)

def forget_password(request):
    if request.method=='GET':
        return render(request,'forget_password.html')
    else:
        email=request.POST['email']
        request.session['email']=email
        user=User.objects.filter(email = email).exists()
        if user:
            otp=random.randint(1000,9999)
            request.session['otp']=otp
            with get_connection(
                host =settings.EMAIL_HOST,
                port =settings.EMAIL_PORT,
                username =settings.EMAIL_HOST_USER,
                password =settings.EMAIL_HOST_PASSWORD,
                use_tls =settings.EMAIL_USE_TLS
                
            ) as connection:
                subject ="OTP Verificaton"
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[email]
                message = f"Your OTP is {otp}.Do not share with other"
                
                EmailMessage(subject,message,email_from,recipient_list,connection=connection).send()
            
            return redirect('/otp_verification')
        else:
            context={}
            context['error']='User does not Exist'
            return render(request,'forget_password.html',context)
        
def otp_verification(request):
    if request.method=='GET':
        return render(request,'otp_verification.html')
    else:
        otp=int(request.POST['otp'])
        email_otp=int(request.session['otp'])
        
        if otp == email_otp:
            return redirect('/new_password')
        else:
            context={}
            context['error']='OTP does not match'
            return render(request,'otp_verification.html',context)


def new_password(request):
    if request.method == "GET":
        return render(request,'new_password.html')
    else:
        email=request.session['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        user=User.objects.get(email=email)
        if password == confirm_password:
            user.set_password(password)
            user.save()
            return redirect('/login')
        else:
            context={}
            context['error']='Password and confirm password does not match'
            return render(request,'new_password.html',context)
        
            


    
        
    
        
        
        

        
   

        
        