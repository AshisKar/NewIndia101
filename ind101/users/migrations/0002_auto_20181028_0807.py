# Generated by Django 2.0.8 on 2018-10-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Age',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Sex',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=6),
        ),
    ]