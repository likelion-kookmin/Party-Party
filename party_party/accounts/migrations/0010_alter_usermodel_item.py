# Generated by Django 3.2.4 on 2021-08-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_usermodel_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='item',
            field=models.CharField(choices=[('etc', '그외'), ('character', '캐릭터'), ('people', '실존인물'), ('2D', '2D')], max_length=80),
        ),
    ]