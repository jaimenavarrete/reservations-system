# Generated by Django 4.1.3 on 2022-12-09 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationevent',
            old_name='display_current_spots_number',
            new_name='display_spots_number',
        ),
        migrations.RenameField(
            model_name='reservationevent',
            old_name='duration',
            new_name='duration_in_minutes',
        ),
        migrations.RemoveField(
            model_name='reservationevent',
            name='time_unit',
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='internal_note',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='modified_by',
            field=models.CharField(blank=True, max_length=36),
        ),
        migrations.AlterField(
            model_name='reservationevent',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='TimeUnit',
        ),
    ]
