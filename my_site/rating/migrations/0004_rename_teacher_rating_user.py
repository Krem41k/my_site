# Generated by Django 4.0.1 on 2022-03-07 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_rename_company_rating_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='teacher',
            new_name='user',
        ),
    ]
