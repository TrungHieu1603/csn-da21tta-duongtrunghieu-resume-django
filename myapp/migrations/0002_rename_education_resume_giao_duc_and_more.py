# Generated by Django 4.2.6 on 2023-11-25 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='education',
            new_name='Giao_Duc',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='full_name',
            new_name='Ho_Ten',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='experience',
            new_name='Kinh_Nghiem',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='skills',
            new_name='Ky_Nang',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='phone',
            new_name='So_Dien_Thoai',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='summary',
            new_name='Tom_Tat',
        ),
    ]
