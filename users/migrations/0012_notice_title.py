# Generated by Django 2.1.15 on 2020-12-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_notice_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
