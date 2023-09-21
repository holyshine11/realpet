from django.db import models
import re
import os
from django.utils.text import slugify

def get_upload_to(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    slugified_filename = slugify(base_filename)
    new_filename = f"{slugified_filename}{file_extension}"

    return os.path.join('dog_images/', new_filename)

class DogInfo(models.Model):
    class Meta:
        app_label = 'dogtag'

    guardian_nickname = models.CharField(max_length=50, null=False)
    dog_name = models.CharField(max_length=50, null=False)
    # 안심번호 추가 실패 함
    phone_number = models.CharField(max_length=20, null=False)
    
    birth_year = models.CharField(max_length=4, null=True, blank=True)
    GENDER_CHOICES = [('M', '남아'), ('F', '여아')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_neutered = models.BooleanField(default=False)
    dog_image = models.ImageField(upload_to=get_upload_to, null=True, blank=True)  # upload_to를 함수로 설정

    # 새로운 필드: 등록일과 수정일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # 휴대폰 번호 형식 검사
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', self.phone_number):
            raise ValueError("Invalid phone number format")

        # 출생년도 형식 검사
        if self.birth_year and not re.match(r'^\d{4}$', self.birth_year):
            raise ValueError("Invalid birth year format")

        super(DogInfo, self).save(*args, **kwargs)
