# Generated by Django 5.0.3 on 2024-04-05 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_alter_blog_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category_name',
        ),
    ]
