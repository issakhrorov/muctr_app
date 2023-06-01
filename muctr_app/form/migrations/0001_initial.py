# Generated by Django 4.2.1 on 2023-05-19 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('passport_series', models.CharField(max_length=9)),
                ('passport', models.FileField(upload_to=None)),
                ('passport_translation', models.FileField(upload_to=None)),
                ('school_diploma', models.FileField(upload_to=None)),
                ('school_diploma_translation', models.FileField(upload_to=None)),
                ('photo', models.FileField(upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
