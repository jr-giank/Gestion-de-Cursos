# Generated by Django 4.0.1 on 2022-01-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_cursos_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='costo',
            field=models.DecimalField(decimal_places=8, max_digits=10, null=True),
        ),
    ]
