# Generated by Django 2.1.1 on 2019-06-23 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventurerecords',
            name='holder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
