from django import forms
from .models import Laptop

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        #labels
        labels = {
            'ram': 'RAM in GB',
            'rom': 'ROM',
            'model_name': 'Model Name'
        }

        #placeholders
        widgets = {'company': forms.TextInput(attrs={'placeholder': 'for e.g : asus, sony, dell'}),
                   'model_name': forms.TextInput(attrs={'placeholder': 'for e.g :ipad, lattitude'}),
                   'ram': forms.TextInput(attrs={'placeholder': 'for e.g : 2GB, 4GB, 8GB, 12GB'}),
                   'rom': forms.TextInput(attrs={'placeholder': 'for e.g : 1SSD'}),
                   'processor': forms.TextInput(attrs={'placeholder': 'for e.g : dual core, core i3, core i5'}),
                   'price': forms.TextInput(attrs={'placeholder': 'Price of Product'}),
                   'weight': forms.TextInput(attrs={'placeholder': 'e.g : 1kg, 1.5kg, 2kg'})

        }