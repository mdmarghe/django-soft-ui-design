# Generated by Django 4.2.4 on 2023-08-31 17:05

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='wines/')),
                ('production_house', models.CharField(max_length=100)),
                ('grape_variety', models.CharField(max_length=100)),
                ('denomination_of_origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedWine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.wine')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='wines',
            field=models.ManyToManyField(through='home.OrderedWine', to='home.wine'),
        ),
    ]
