from django import forms
from .models import Mesaj

class IletisimForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ['isim', 'email', 'konu', 'mesaj']
        
        # Her alan için Tailwind sınıfları (widget) tanımlıyoruz
        # Bu sayede HTML'de class="..." yazmakla uğraşmayacağız.
        widgets = {
            'isim': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:border-blue-500',
                'placeholder': 'Adınız Soyadınız'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:border-blue-500',
                'placeholder': 'ornek@email.com'
            }),
            'konu': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:border-blue-500',
                'placeholder': 'Mesajınız ne hakkında?'
            }),
            'mesaj': forms.Textarea(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-600 rounded-lg p-3 focus:outline-none focus:border-blue-500 h-32',
                'placeholder': 'Mesajınızı buraya yazın...'
            }),
        }