# Generated by Django 4.2.3 on 2023-07-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcadopara a página ser exibida publicamente.'),
        ),
    ]
