# Generated by Django 5.0.4 on 2024-04-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oracles", "0007_alter_oracleanswer_roll_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="oraclequestion",
            name="die",
            field=models.CharField(default="d20", max_length=6),
        ),
    ]
