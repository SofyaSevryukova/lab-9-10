# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tasks', to='todolist.TaskType'),
        ),
    ]