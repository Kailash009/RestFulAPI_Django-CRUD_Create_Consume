# Generated by Django 5.0.3 on 2024-05-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('mobileno', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]
