# Generated by Django 2.2.6 on 2019-10-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='dishes.Ingredient'),
        ),
    ]
