# Generated by Django 5.0 on 2024-06-27 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestap', models.DateTimeField(auto_now_add=True)),
                ('ip_addres', models.GenericIPAddressField()),
                ('user_agent', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Visit',
                'verbose_name_plural': 'Visits',
                'db_table': 'visits',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WeeklyVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField()),
                ('week_end', models.DateField()),
                ('visit_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'WeeklyVisit',
                'verbose_name_plural': 'WeeklyVisits',
                'db_table': 'weekly_visits',
                'ordering': ['id'],
            },
        ),
    ]
