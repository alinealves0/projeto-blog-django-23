# Generated by Django 4.2.3 on 2023-07-14 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postattachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
    ]