# Generated by Django 3.2 on 2021-08-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usermodel_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='item',
            field=models.CharField(choices=[('character', '캐릭터'), ('2D', '2D'), ('etc', '그외'), ('people', '실존인물')], max_length=80),
        ),
    ]