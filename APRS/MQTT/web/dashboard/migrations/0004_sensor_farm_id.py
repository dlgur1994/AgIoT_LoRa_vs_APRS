# Generated by Django 2.0.13 on 2019-12-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_farm_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='farm_id',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
