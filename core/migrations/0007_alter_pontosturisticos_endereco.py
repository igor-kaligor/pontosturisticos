# Generated by Django 4.0.3 on 2022-03-09 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('core', '0006_remove_pontosturisticos_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturisticos',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
        ),
    ]
