# Generated by Django 4.2.1 on 2023-05-31 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0026_alter_customuser_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
