# Generated by Django 3.2.4 on 2021-08-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_usermodel_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='item',
            field=models.CharField(choices=[('2D', '2D'), ('character', '캐릭터'), ('etc', '그외'), ('people', '실존인물')], max_length=80),
        ),
    ]
