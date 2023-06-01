from .models import Student
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'lastname', 'passport_series', 'email', 'checked')
    list_filter = ('checked', 'country',  'state', 'gender', 'edu_type', 'edu_level', 'edu_field')

    def field6_link(self, obj):
        url = reverse('my_url_name', args=[obj.username])
        return format_html('<a href="{}">{}</a>', url, obj.username)

admin.site.register(Student, MyModelAdmin)
