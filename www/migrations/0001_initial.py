# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Puheenjohtaja', 'Puheenjohtaja'), ('Varapuheenjohtaja', 'Varapuheenjohtaja'), ('Rahastonhoitaja', 'Rahastonhoitaja'), ('Sihteeri', 'Sihteeri'), ('Tiedotus- ja fuksivastaava', 'Tiedotus- ja fuksivastaava'), ('Liikunta- ja huvivastaava', 'Liikunta- ja huvivastaava'), ('Isäntä', 'Isäntä'), ('Emäntä', 'Emäntä'), ('Varajäsen', 'Varajäsen'), ('Toimari', 'Toimari'), ('Kooraaja', 'Kooraaja')], max_length=20)),
                ('view_order', models.IntegerField(choices=[(1, 'Puheenjohtaja'), (2, 'Varapuheenjohtaja'), (3, 'Rahastonhoitaja'), (4, 'Sihteeri'), (5, 'Tiedotus- ja fuksivastaava'), (6, 'Liikunta- ja huvivastaava'), (7, 'Isäntä'), (8, 'Emäntä'), (9, 'Varajäsen'), (10, 'Toimari'), (11, 'Kooraaja')])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(default='etu.suku@student.tut.fi', max_length=254)),
                ('ircnick', models.CharField(blank=True, max_length=15)),
                ('photo', models.URLField(blank=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boardmembers', to='www.Board')),
            ],
            options={
                'ordering': ['view_order'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'News',
            },
        ),
    ]
