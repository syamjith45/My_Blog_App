# Generated by Django 4.2.9 on 2024-01-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogHome', '0005_rename_comment_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
