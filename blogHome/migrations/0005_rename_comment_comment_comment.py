# Generated by Django 4.2.9 on 2024-01-05 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogHome', '0004_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]
