# Generated by Django 5.0 on 2023-12-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Parker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.IntegerField(default=0),
        ),
    ]