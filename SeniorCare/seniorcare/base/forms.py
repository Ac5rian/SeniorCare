from django.forms import ModelForm, widgets
from .models import senior_list
from django import forms

class register_form(ModelForm):
  class Meta:
    model=senior_list
    fields= '__all__'
    widgets= {
      'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'required': True, 'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'required': True,'class': 'form-control'}),
      'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name', 'required': True, 'class': 'form-control'}),
      'suffix': forms.TextInput(attrs={'placeholder': 'Suffix', 'required': True,'class': 'form-control'}),
      'age': forms.NumberInput(attrs={'placeholder': 'Age', 'required': True, 'class': 'form-control'}),
      'sex': forms.TextInput(attrs={'placeholder': 'Sex', 'required': True, 'class': 'form-control form-select'}),
      'birth_date': forms.DateInput(attrs={'placeholder': 'Birth Date yyyy-mm-dd', 'required': True, 'class': 'form-control'}),
      'address': forms.TextInput(attrs={'placeholder': 'Address', 'required': True, 'class': 'form-control'}),
      'OSCA_ID': forms.NumberInput(attrs={'placeholder': 'OSCA_ID', 'required': True, 'class': 'form-control'}),
    }
  def clean_OSCA_ID(self):
    OSCA_ID = self.cleaned_data.get('OSCA_ID')    
    for instance in senior_list.objects.all():
      if instance.OSCA_ID == OSCA_ID:
        raise forms.ValidationError(str(OSCA_ID) + ' is already exist')
        
    return OSCA_ID
    