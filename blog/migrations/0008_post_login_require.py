# Generated by Django 4.2.14 on 2024-09-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_tag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
