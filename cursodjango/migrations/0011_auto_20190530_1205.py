# Generated by Django 2.2.1 on 2019-05-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursodjango', '0010_auto_20190530_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]