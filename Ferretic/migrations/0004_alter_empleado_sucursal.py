# Generated by Django 4.1.3 on 2022-11-01 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ferretic', '0003_alter_empleado_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='Ferretic.sucursal'),
        ),
    ]