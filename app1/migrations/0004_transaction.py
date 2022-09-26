# Generated by Django 4.0.5 on 2022-09-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_accounts_balfordisp_remove_accounts_productid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exac', models.CharField(blank=True, max_length=255)),
                ('vendor', models.CharField(blank=True, max_length=255)),
                ('tdate', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('tax', models.IntegerField(blank=True)),
                ('refenrence', models.CharField(blank=True, max_length=255)),
                ('customer', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
