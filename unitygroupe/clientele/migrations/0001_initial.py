# Generated by Django 2.2.6 on 2019-10-03 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=250)),
                ('titre', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='img')),
                ('descriptions', models.TextField()),
                ('status', models.BooleanField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteurTest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
