from django import forms
from .models import DogInfo
import re

class DogInfoForm(forms.ModelForm):
    class Meta:
        model = DogInfo
        fields = '__all__'
        widgets = {
            'guardian_nickname': forms.TextInput(attrs={'placeholder': '보호자 닉네임을 입력 하세요.'}),
            'dog_name': forms.TextInput(attrs={'placeholder': '반려동물 이름을 입력하세요.'}),
            'birth_year': forms.TextInput(attrs={'placeholder': '숫자 4자리만 입력 가능합니다. (예시 : 2012)'}),
        }
        labels = {
            'guardian_nickname': '보호자 닉네임',
            'dog_name': '반려동물 이름',
            'phone_number': '휴대폰 번호',
            'birth_year': '출생년도',
            'gender': '성별',
            'is_neutered': '중성화 여부',  
            'dog_image': '사진',
        }

    GENDER_CHOICES = [
        ('M', '남아'),
        ('F', '여아'),
    ]

    NEUTERED_CHOICES = [
        (True, '예'),
        (False, '아니오'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )

    is_neutered = forms.ChoiceField(
        choices=NEUTERED_CHOICES,
        widget=forms.RadioSelect,
        label='중성화 여부'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'placeholder': '휴대폰번호를 입력하세요. (예시 : 010-1234-1234)'})
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', phone_number):
            raise forms.ValidationError("휴대폰 번호 형식은 '010-1234-5678'과 같은 형태로 입력하세요.")
        return phone_number
