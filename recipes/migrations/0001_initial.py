# Generated by Django 3.2.25 on 2025-04-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('calories', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('breakfast', 'Завтрак'), ('lunch', 'Обед'), ('dinner', 'Ужин')], max_length=10)),
            ],
        ),
    ]
