# Generated by Django 2.1.5 on 2019-03-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('available_on', models.DateField(verbose_name='availability date')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='meals',
            field=models.ManyToManyField(to='main_app.Meal'),
        ),
    ]
