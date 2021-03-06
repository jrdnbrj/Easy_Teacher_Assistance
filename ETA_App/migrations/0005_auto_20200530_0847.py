# Generated by Django 3.0.6 on 2020-05-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ETA_App', '0004_alumno_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('string', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='alumno',
            name='calificacion',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Calificación'),
        ),
    ]
