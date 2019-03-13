from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .forms import PhoneForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def users_index(request):
  users = User.objects.all()
  return render(request, 'users/index.html', { 'users': users })

def users_detail(request, user_id):
  user = User.objects.get(id=user_id)
  phone_form = PhoneForm()
  return render(request, 'users/detail.html', {'user': user, 'phone_form': phone_form})

class UserCreate(CreateView):
  model = User
  fields = '__all__'
  success_url = '/users/'

class UserUpdate(UpdateView):
  model = User
  fields = ['name', 'role', 'email', 'logo', 'website']
#   form = UserForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the cat_id assigned
#     new_user = form.save(commit=False)
#     new_user.user_id = user_id
#     new_user.save()
#   success_url = '/users/'

class UserDelete(DeleteView):
  model = User
  success_url = '/users/'

# class UserForm(forms.Form):
#     name = forms.ImageField()
#     second_image = forms.ImageField()
#     third_image = forms.ImageField()
#     fourth_image = forms.ImageField()

def add_phone(request, user_id):
  # create the ModelForm using the data in request.POST
  phone_form = PhoneForm(request.POST)
  # validate the form
  if phone_form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_phone = phone_form.save(commit=False)
    new_phone.user_id = user_id
    new_phone.save()
  return redirect('detail', user_id=user_id)
