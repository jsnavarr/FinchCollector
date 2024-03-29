from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
import uuid
import boto3
from .models import User, Phone, Meal, Photo
from .forms import PhoneForm

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'anycollector'

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def users_index(request):
  users = User.objects.all()
  return render(request, 'users/index.html', { 'users': users })

def users_detail(request, user_id):
    user = User.objects.get(id=user_id)
    user_phones = Phone.objects.filter(user_id=user.id)
    meals_user_doesnt_have = Meal.objects.exclude(id__in = user.meals.all().values_list('id'))
    print(user_phones)
    phone_form = PhoneForm()
    return render(request, 'users/detail.html', {
        'user': user, 'phone_form': phone_form, 
        'phones': user_phones, 'meals': meals_user_doesnt_have
    })

class UserCreate(CreateView):
  model = User
  fields = '__all__'
  success_url = '/users/'

class UserUpdate(UpdateView):
  model = User
  fields = ['name', 'role', 'email', 'logo', 'website']
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
    # has the user_id assigned
    new_phone = phone_form.save(commit=False)
    new_phone.user_id = user_id
    new_phone.save()
  return redirect('detail', user_id=user_id)

def remove_phone(request, user_id, phone_id):
    Phone.objects.filter(id=phone_id).delete()
    return redirect('detail', user_id=user_id)

class MealList(ListView):
  model = Meal

class MealDetail(DetailView):
  model = Meal

class MealCreate(CreateView):
  model = Meal
  fields = '__all__'

class MealUpdate(UpdateView):
  model = Meal
  fields = ['description', 'available_on']

class MealDelete(DeleteView):
  model = Meal
  success_url = '/meals/'

def assoc_meal(request, user_id, meal_id):
  # Note that you can pass a meal's id instead of the whole object
  User.objects.get(id=user_id).meals.add(meal_id)
  return redirect('detail', user_id=user_id)

def deassoc_meal(request, user_id, meal_id):
  # Note that you can pass a meal's id instead of the whole object
  User.objects.get(id=user_id).meals.remove(meal_id)
  return redirect('detail', user_id=user_id)

def add_photo(request, user_id):
	# photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to user_id or user (if you have a user object
            photo = Photo(url=url, user_id=user_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', user_id=user_id)