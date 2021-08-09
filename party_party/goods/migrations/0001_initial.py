# Generated by Django 3.2.3 on 2021-08-09 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SemiGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('product_image', models.ImageField(upload_to='')),
                ('semi_price', models.IntegerField()),
                ('semi_count', models.IntegerField()),
                ('item', models.CharField(choices=[('character', '캐릭터'), ('2D', '2D'), ('etc', '그외'), ('people', '실존인물')], max_length=80)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('twitter', models.CharField(max_length=20)),
                ('information_needs', models.CharField(max_length=500)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semiregist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('product_image', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('item', models.CharField(choices=[('character', '캐릭터'), ('2D', '2D'), ('etc', '그외'), ('people', '실존인물')], max_length=80)),
                ('end_date', models.DateField(db_column='End Date')),
                ('term_needs', models.DateField()),
                ('term_deposit', models.IntegerField()),
                ('information_needs', models.CharField(max_length=500)),
                ('information_deposit', models.CharField(max_length=500)),
                ('account_deposit', models.CharField(max_length=50)),
                ('count_needs', models.IntegerField()),
                ('count_deposit', models.IntegerField()),
                ('howto_delivery', models.CharField(max_length=10)),
                ('location1', models.CharField(max_length=20)),
                ('location2', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
