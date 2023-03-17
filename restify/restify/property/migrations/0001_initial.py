# Generated by Django 4.1.7 on 2023-03-17 00:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('owner_first_name', models.CharField(max_length=255)),
                ('owner_last_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('guests', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('number_of_bedrooms', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('number_of_washrooms', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('contact_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('amenities', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
