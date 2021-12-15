from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'rating')
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control text_area', 'rows': 3, }),
            'rating': forms.TextInput(attrs={'min':1,'max': '10','type': 'number'})
        }
