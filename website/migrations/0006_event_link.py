# Generated by Django 4.0.1 on 2022-01-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_blog_slug_event_slug_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
