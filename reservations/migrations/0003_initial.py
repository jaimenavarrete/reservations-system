# Generated by Django 4.1.3 on 2022-12-09 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0002_rename_display_current_spots_number_reservationevent_display_spots_number_and_more'),
        ('reservations', '0002_remove_reservationevent_event_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('extra_information', models.TextField(blank=True)),
                ('start_time', models.DateTimeField()),
                ('reservation_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.reservationevent')),
            ],
        ),
    ]