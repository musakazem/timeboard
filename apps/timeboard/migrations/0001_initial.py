# Generated by Django 5.2 on 2025-04-05 16:53

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductivityDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='score')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Productivity Daily',
                'verbose_name_plural': 'Productivity Daily',
            },
        ),
        migrations.CreateModel(
            name='ProductivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('productivity_factor', models.PositiveSmallIntegerField(default=0, verbose_name='productivity factor')),
            ],
            options={
                'verbose_name': 'Productivity Type',
                'verbose_name_plural': 'Productivity Types',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('hours', models.PositiveSmallIntegerField(default=0, verbose_name='hours')),
                ('productivity_daily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_activities', to='timeboard.productivitydaily', verbose_name='productivity details')),
                ('productivity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_types', to='timeboard.productivitytype', verbose_name='productivity type')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
