# Generated by Django 2.0.1 on 2018-03-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scc_kanban', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('launched', 'Launched'), ('headspace', 'In Headspace'), ('desk', 'On Desk'), ('monitor', 'Monitor'), ('board', 'On the Board'), ('icebox', 'In the Icebox'), ('graveyard', 'Graveyard')], max_length=32),
        ),
    ]
