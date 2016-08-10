from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','email','title','image',
                 'responsibilities','bio','twitter',
                 'github','birthday']
