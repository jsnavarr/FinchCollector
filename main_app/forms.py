from django.forms import ModelForm
from .models import Phone

class PhoneForm(ModelForm):
  class Meta:
    model = Phone
    fields = ['number']