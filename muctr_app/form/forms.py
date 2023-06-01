from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from .validators import *

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ['name', 'lastname', 'middlename', 'username', 'country', 'state', 'zip_code', 'address', 'citizenship', 'gender', 'date_of_birth', 'email', 'phone', 'phone_2', 'passport_series', 'changedname', 'edu_type', 'edu_level', 'edu_field', 'photo', 'passport', 'passport_translation', 'school_diploma', 'school_diploma_translation', 'info_check_agreement', 'entrance_agreement']
        labels = {
            'name': "Имя", 
            'lastname': 'Фамилия', 
            'middlename': 'Отчество', 
            'username': 'Логин', 
            'country' : 'Страна', 
            'state' : 'Город (для жителей Узбекистана)', 
            'country' : 'Страна', 
            'zip_code' : 'Почтовый индекс', 
            'address': 'Адрес', 
            'citizenship' : 'Гражданство', 
            'gender': 'Пол', 
            'date_of_birth': 'Дата рождения', 
            'email': 'Электронная почта', 
            'phone': 'Номер телефона', 
            'phone_2': 'Второй номер телефона', 
            'passport_series': 'Серия и номер паспорта', 
            'changedname': 'Документ подтверждающтй изменение имени (фамилии, отчества)',
            'edu_type': 'Форма обучения',
            'edu_level': 'Степень',
            'edu_field': 'Специальность',
            'photo': 'Фотография', 'passport': 'Паспорт', 
            'passport_translation': 'Нотариальный перевод паспорта', 
            'school_diploma': 'Аттестат', 'school_diploma_translation': 
            'Нотариальный перевод аттестата', 
            'info_check_agreement': 'Заявление о согласии на обработку персональных данных', 
            'entrance_agreement': 'Заявление о зачислении',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: Мадина"}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: Бахтиёрова"}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: Озод кизи"}),
            'username': forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример:  MadinaOB"}),
            'date_of_birth' : forms.DateInput(attrs={'class': 'form-control', "data-text": "Формат: дд/мм/гггг"}),
            'country' : forms.Select(attrs={'class': 'form-control'}),
            'state' : forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: 100000"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'data-text' : "Пример: Яккасарайский район"}),
            'citizenship' : forms.TextInput(attrs={'class': 'form-control', 'data-text' : "Пример: Узбекистан"}),
            'gender' : forms.Select(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', "data-text": "Пример: example@gmail.com"}),
            'phone' : forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: +998901234050"}),
            'phone_2' : forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: +998901234050"}),
            'changedname' : forms.FileInput(attrs={'class': 'form-control file-field', "data-text": "Загрузите документ, подтверждающий изменение вашего имени, фамилии или отчества (если вы меняли)"}),
            'passport_series' : forms.TextInput(attrs={'class': 'form-control', "data-text": "Пример: AA1234567"}),
            'edu_type' : forms.Select(attrs={'class': 'form-control'}),
            'edu_level' : forms.Select(attrs={'class': 'form-control'}),
            'edu_field' : forms.Select(attrs={'class': 'form-control'}),
            'photo' : forms.FileInput(attrs={
                'class': 'form-control file-field', 
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png

Ваше фото должно быть:

✅ Цветным
✅ Размер 3.5 x 4.5 см
✅ Сделано в течение последних 3 месяцев, чтобы отразить ваш текущий вид
"""
                }),
            'passport' : forms.FileInput(attrs={
                'class': 'form-control file-field',
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png, pdf            
"""
                }),
            'passport_translation' : forms.FileInput(attrs={
                'class': 'form-control file-field',
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png, pdf            
"""
                }),
            'school_diploma' : forms.FileInput(attrs={
                'class': 'form-control file-field',
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png, pdf            
"""
                }),
            'school_diploma_translation' : forms.FileInput(attrs={
                'class': 'form-control file-field',
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png, pdf            
"""
                }),
            'info_check_agreement' : forms.FileInput(attrs={
                'class': 'form-control file-field',
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png, pdf            
"""
                }),
            'entrance_agreement' : forms.FileInput(attrs={
                'class': 'form-control file-field',
                'data-text': 
"""Максимальный Размер Файла: 5 MB
Допустимые форматы: jpg, jpeg, png, pdf            
"""
                })
    }
        
    # def clean_name(self):
    #     data = self.cleaned_data["name"]
    #     check_blank(data)
    #     return check_name(data)

    # def clean_lastname(self):
    #     data = self.cleaned_data["lastname"]
    #     check_blank(data)
    #     return check_name(data)
    
    # def clean_middlename(self):
    #     data = self.cleaned_data["middlename"]
    #     check_blank(data)
    #     return check_name(data)
    
    # def clean_country(self):
    #     data = self.cleaned_data["country"]
    #     check_blank(data)
    #     return check_country(data)
        
    # def clean_state(self):
    #     data = self.cleaned_data["country"]
    #     check_blank(data)
    #     return check_state(self.cleaned_data['country'], data)

    # def clean_zip_code(self):
    #     data = self.cleaned_data["zip_code"]
    #     check_blank(data)
    #     return check_zip_code(data)

    # def clean_gender(self):
    #     data = self.cleaned_data["gender"]
    #     check_blank(data)
    #     return check_gender(data)
    
    # def clean_email(self):
    #     data = self.cleaned_data["email"]
    #     check_blank(data)
    #     return check_gender(data)

    # def clean_phone(self):
    #     data = self.cleaned_data["phone"]
    #     check_blank(data)
    #     return check_phone(data)
    
    # def clean_phone2(self):
    #     data = self.cleaned_data["phone2"]
    #     check_blank(data)
    #     return check_phone(data)
    
    # def clean_passport_series(self):
    #     data = self.cleaned_data["passport_series"]
    #     check_blank(data)
    #     return check_passport_series(data)
    
    # def clean_photo(self):
    #     data = self.cleaned_data["photo"]
    #     check_blank_file(data)
    #     return check_photo(data)
    
    # def clean_passport(self):
    #     data = self.cleaned_data["passport"]
    #     check_blank_file(data)
    #     return check_file(data)
    
    # def clean_passport_translation(self):
    #     data = self.cleaned_data["passport_translation"]
    #     check_blank_file(data)
    #     return check_file(data)

    # def clean_school_diploma(self):
    #     data = self.cleaned_data["school_diploma"]
    #     check_blank_file(data)
    #     return check_file(data)
    
    # def clean_school_diploma_translation(self):
    #     data = self.cleaned_data["school_diploma_translation"]
    #     check_blank_file(data)
    #     return check_file(data)
    
    # def clean_info_check_agreement(self):
    #     data = self.cleaned_data["info_check_agreement"]
    #     print(data)
    #     check_blank_file(data)
    #     return check_file(data)
    
    # def clean_entrance_agreement(self):
    #     data = self.cleaned_data["entrance_agreement"]
    #     check_blank_file(data)
    #     return check_file(data)