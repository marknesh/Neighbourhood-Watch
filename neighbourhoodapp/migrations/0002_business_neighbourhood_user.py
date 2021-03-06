# Generated by Django 3.0.4 on 2020-03-25 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhoodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('occupants', models.CharField(max_length=60)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=60)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.Neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.Neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.User')),
            ],
        ),
    ]
