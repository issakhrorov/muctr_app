# Generated by Django 4.2.1 on 2023-05-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0017_alter_student_passport_alter_student_passport_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
