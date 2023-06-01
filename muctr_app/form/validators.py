# from django.core.exceptions import ValidationError
# from .models import Student

# data = Student.objects.all()

# def check_blank(field):
#     if field == "":
#         print(data[0].email)
#         raise ValidationError("Это поле обязательное!")
    
# def check_blank_file(field):
#     if field == None:
#         print(data[0].email)
#         raise ValidationError("Это поле обязательное!")

# def check_name(name):
#     for char in name:
#         if  not (("А" <= char and char <= "Я") or ("а" <= char and char <= "я") or (char == " ") or (char == "ё") or (char == "Ë")):
#             raise ValidationError("Введите имя правильно!")
#     return name

# def check_number(number):
#     if number[0] != "+" or len(number) != 13 or not(number[1:-1].isnumeric()):
#         raise ValidationError("Укажите правильный номер!")
#     return number

# def check_country(country):
#     if country == '': 
#         raise ValidationError("Укажите страну!")
#     return country

# def check_state(country, state):
#     if country != 'UZBEKISTAN': state = ''
#     if country == 'UZBEKISTAN' and state == '':
#         raise ValidationError("Укажите город!")
#     return state

# def check_zip_code(zip_code):
#     if not zip_code.isnumeric() and len(zip_code) != 6: raise ValidationError("Укажите правильный почтовый индекс!")
#     return zip_code

# def check_gender(gender):
#     if not gender:
#         raise ValidationError("Укажите гендер!")
#     return gender

# # def check_email(email):
#     # for field in data:

#     # if not gender:
#     #     raise ValidationError("Укажите гендер!")
#     # return gender

# def check_phone(phone):
#     if len(phone) != 13:
#         raise ValidationError("Укажите правильный номер!")
#     return phone
        
# def check_passport_series(passport_series):
#     if not passport_series[2::].isnumeric() or ('A' > passport_series[0] and 'Z' < passport_series[0]) or ('A' > passport_series[1] and 'Z' < passport_series[1]):
#         raise ValidationError("Укажите правильную серию и номер паспорта!")
#     return passport_series
    
# def check_file(file):
#     if not file: return file
#     if file.__size > 5242880:
#         raise ValidationError("Файл слишком большой! Выберите другой файл!")
#     if not file.name.endswith(('.jpg', '.png', '.jpeg', 'pdf')):
#         raise ValidationError("Файл должен быть формата jpg, png или pdf!")
#     return file

# def check_photo(file):
#     if not file: return file
#     if file.__size > 5242880:
#         raise ValidationError("Файл слишком большой! Выберите другой файл!")
#     if not file.name.endswith(('.jpg', '.png', '.jpeg')):
#         raise ValidationError("Файл должен быть формата jpg, png или jpeg!")
#     return file




        