# Generated by Django 4.0.5 on 2022-09-29 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_vendor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='detype',
        ),
    ]