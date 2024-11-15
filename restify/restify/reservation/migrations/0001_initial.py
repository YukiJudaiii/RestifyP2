# Generated by Django 4.1.7 on 2023-03-18 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('state', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied'), ('Canceled', 'Canceled'), ('Terminated', 'Terminated'), ('Completed', 'Completed'), ('Expired', 'Expired'), ('Pending Cancel', 'Pending Cancel')], default='Pending', max_length=14)),
                ('action', models.CharField(blank=True, choices=[('approve', 'Approve'), ('deny', 'Deny'), ('approve_cancel', 'Approve Cancel'), ('deny_cancel', 'Deny Cancel')], max_length=15, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
