# Generated by Django 3.1.2 on 2020-10-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_author_test_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
