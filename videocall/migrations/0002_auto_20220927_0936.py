# Generated by Django 2.2.28 on 2022-09-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videocall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommember',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
