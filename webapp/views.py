from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login



def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')        

def about(request):
    return render(request,'about.html')    


def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('loginpage')
    else:
        return render(request,'signup.html')

#User login functionality view
def login1(request):
	if request.method =='POST':
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(username=username,password=password)
          if user is not None:
              if user.is_staff:
                  login(request,user)
                  return redirect('admin1')
              else:
                  login(request,user)
                  auth.login(request, user)
                  messages.info(request, f'Welcome {username}')
                  return redirect('about')
          else:
              messages.info(request,'invalid username or password')	
              return redirect('loginpage')

                
          
            
                    
		
	

#User logout functionality view
def logout(request):
	auth.logout(request)
	return redirect('home')

def admin1(request):
    return render(request,'admin.html')  