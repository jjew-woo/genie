# Generated by Django 2.2 on 2019-07-30 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodmenu', '0003_goodmenu_hit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodmenu',
            name='star',
        ),
    ]
