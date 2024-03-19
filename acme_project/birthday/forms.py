from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__' 
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
    