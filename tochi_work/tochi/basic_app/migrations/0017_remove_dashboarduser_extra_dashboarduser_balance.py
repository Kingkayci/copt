# Generated by Django 4.1 on 2023-10-20 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0016_dashboarduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboarduser',
            name='extra',
        ),
        migrations.AddField(
            model_name='dashboarduser',
            name='balance',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
