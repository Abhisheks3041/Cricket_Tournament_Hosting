from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse 


# Create your views here.
def home(request):
    return render(request,'home.html')



def manager(request):
    if request.method=="POST":
        mname=request.POST['fname']
        lname=request.POST['sname']
        
        phno=request.POST['phno']
        address=request.POST['M_address']
        username=request.POST['uname']
        password=request.POST['pass1']
        
        User.objects.create_user(first_name=mname,last_name=lname,phonenumber=phno,address=address,username=username,password=password,usertype=2)
        return redirect(home)
    else:
        return render(request,'manager_reg.html')
    
    
def player(request):
    return render(request,'player.html')
    
def loggin(request):
    return render(request,'catmain.html')
    



def about(request):
    return render(request,'about.html')

def support(request):
    return render(request,'support.html')




def tourguide(request):
    return render(request,'tourguide.html')

def logins(request):
    if request.method=="POST":
        usern=request.POST['uname']
        passw=request.POST['pass1']
        user=authenticate(request,username=usern,password=passw)
        print(user)
        if user is not None and user.usertype==2:
            request.session['user_id']=user.id
            login(request,user)
            return redirect(managerdash)
        elif user is not None and user.is_superuser==1:
            request.session['admin_id']=user.id
            login(request,user)
            return redirect(admindash)
        elif user is not None and user.usertype==1:
            request.session['user_id']=user.id
            login(request,user)
            return redirect(addtournament)
        else:
            return redirect(logins)
    else:
        
        return render(request,'login.html')
        
     

def create_a_tournament(request):
    return redirect(logins)

def next(request):
    return render(request,'')

def back(request):
    return render(request,'home.html')

def handle_uploaded_file(f):  
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

def managerdash(request):
    id=request.session['user_id']
    if request.method=='POST':
        tname=request.POST['tname']
        tlogo=request.FILES['tlogo']
        handle_uploaded_file(tlogo)
        Teams.objects.create(team_name=tname,team_logo=tlogo,manager_id=id)
        return redirect(managerdash)
        
        
    else:    
        return render(request,'managerdash.html')


def matm(request):
    id=request.session['user_id']
    if request.method=='POST':
        mname=request.POST['mname']
        age=request.POST['age']
        quirk=request.POST['quirk']
        blood_group=request.POST['bloodgroup']
        phone=request.POST['phone']
        Players.objects.create(player_name=mname,player_age=age,player_quirk=quirk,player_bg=blood_group,player_phno=phone,manager_id=id)
        return redirect(matm)
        
        
    else:    
        return render(request,'matm.html')

def manageredit(request):
    id=request.session['user_id']
    if request.method=='POST':
        nphone=request.POST['nphone']
        nemail=request.POST['nemail']
        naddress=request.POST['naddress']
        User.objects.filter(id=id).update(phonenumber=nphone,email=nemail,address=naddress)
        return redirect(managerdash)
    else:
        data=User.objects.filter(id=id).get()   
        return render(request,'manageredit.html',{'data':data})
    
    
def managerviewt(request):
    id=request.session['user_id']
    data=Players.objects.filter(manager_id=id).all()
    return render (request,'mvt.html',{'data':data})

def playeredit(request,id):
    if request.method=='POST':
        nphone=request.POST['nphone']
        Players.objects.filter(id=id).update(player_phno=nphone)
        return redirect(managerviewt)
    else:
        data=Players.objects.filter(id=id).get()
        return render (request,'playeredit.html',{'data':data})

def playerdel(request,id):
    Players.objects.filter(id=id).delete()       
    return redirect(managerviewt)

def logouts(request):
    logout(request)
    return redirect(logins)

def adminedit(request):
    id=request.session['admin_id']
    if request.method=='POST':
        nphone=request.POST['nphone']
        nemail=request.POST['nemail']
        User.objects.filter(id=id).update(phonenumber=nphone,email=nemail)
        return redirect(admindash)
    else:
        data=User.objects.filter(id=id).get()
        return render (request,'moderedit.html',{'data':data})


def admindash(request):
    if request.method=="POST":
        mname=request.POST['fmoname']
        lname=request.POST['smoname']
        email=request.POST['moemail']
        phno=request.POST['mophno']
        address=request.POST['moaddress']
        user_name=request.POST['mousername']
        password=request.POST['pass2']
        
        User.objects.create_user(first_name=mname,last_name=lname,email=email,phonenumber=phno,address=address,username=user_name,password=password,usertype=1)
        return redirect(admindash)
    else:
        return render(request,'admindash.html')
    
    
def viewman(request):
    data=User.objects.filter(usertype=1).all()
    return render(request,'mnviewmod.html',{'data':data})

def addtournament(request):
    id=request.session['user_id']
    if request.method=='POST':
        tournament_name=request.POST['To_name']
        tournament_prize=request.POST['To_pm']
        tournament_participants=request.POST['To_parti']
        Tournament.objects.create(tournament_name=tournament_name,prize_money=tournament_prize,team_participate=tournament_participants)
        return redirect(addtournament)
    else:    
        return render(request,'addtournament.html')
    
def viewtournament(request):
    data=Tournament.objects.all()
    return render(request,'viewtournament.html',{'data':data})


    
def tourdel(request,id):
    Tournament.objects.filter(id=id).delete()       
    return redirect(viewtournament)

def modedit(request):
     id=request.session['user_id']
     if request.method=='POST':
        nphone=request.POST['nphone']
        nemail=request.POST['nemail']
        User.objects.filter(id=id).update(phonenumber=nphone,email=nemail)
        return redirect(modedit)
     else:
        data=User.objects.filter(id=id).get()
        return render (request,'cordinatoredit.html',{'data':data})