# Generated by Django 5.0.3 on 2024-04-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_blog_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]
