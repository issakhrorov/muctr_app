# Generated by Django 4.2.1 on 2023-05-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0014_alter_student_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='entrance_agreement',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='info_check_agreement',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.FileField(blank=True, null=True, unique=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport_translation',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='school_diploma_translation',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
    ]
