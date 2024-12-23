# Generated by Django 5.1.4 on 2024-12-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminControl', '0002_trustedpartner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommercialServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('wattermarkIcon', models.ImageField(blank=True, null=True, upload_to='wattermarkIcon/')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
