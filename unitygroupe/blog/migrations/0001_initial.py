# Generated by Django 2.2.6 on 2019-10-03 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('image', models.ImageField(upload_to='blog/image')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/category')),
                ('titre', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categorie',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('message', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='blog/comment')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='blog.Article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/image')),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('date_upd', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_article', to='blog.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_article', to='blog.Categorie'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]