from django.shortcuts import render
from django.contrib.auth.models import Users
from  django.contrib import auth

# Create your views here.
def login(request):
     if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            console.log('login başarılı')
            return redirect('index')
        else:
            console.log('kulanıcı adı veya parola yanlış')
            return redirect('login') 
     else:
        return render(request, 'user/login.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                print('bu kulanıcı ismi daha önce alınmış')
                return redirect('register')
            else:
                 if User.objects.filter(email=email).exists():
                   print('bu kulanıcı emaili daha önce alınmış')
                   return redirect('register')
                 else:
                     user =User.objects.create_user(username=username,password=password, email=email)
                     user.save()
                     print('kulanıcı oluşturuldu')
                     return register('login')
        else:
            print('şifreler eşleşmiyor')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    return render(request, 'user/logout.html')
