# Generated by Django 2.2.4 on 2019-08-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20190819_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]