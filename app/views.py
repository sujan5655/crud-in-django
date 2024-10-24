
# Create your views here.
from django.shortcuts import render,redirect
from app.models import Profile
# Create your views here.
def profile(request):
 profile=Profile.objects.all()
 context={
    'profiles':profile
  }
 return render(request,'profile.html',context)

def createProfile(request):
 if request.method=="POST":
  name=request.POST.get('name')
  address=request.POST.get('address')
  phone_number=request.POST.get('phone_number')
  gender=request.POST.get('gender')
  Profile.objects.create(name = name,address=address,phone_number= phone_number,gender=gender)
  return redirect('/profile/')
 return render(request,'createprofile.html')

def updateProfile(request,id):
 profile=Profile.objects.get(id=id)
 if request.method=="POST":
  name=request.POST.get('name')
  address=request.POST.get('address')
  phone_number=request.POST.get('phone_number')
  gender=request.POST.get('gender')
  profile.name=name
  profile.address=address
  profile.phone_number=phone_number
  profile.gender=gender
  profile.save()  
  return redirect('/profile')
 return render(request,'updateProfile.html')

def deleteProfile(request,id):
 profile=Profile.objects.get(id=id)
 profile.delete()
 return redirect('/profile')



 

