# Generated by Django 3.2.4 on 2023-05-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinarblog', '0006_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]