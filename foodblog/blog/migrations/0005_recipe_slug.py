# Generated by Django 4.1.1 on 2022-10-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_catagory_image_alter_recipe_cover_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default='slug', max_length=150),
            preserve_default=False,
        ),
    ]