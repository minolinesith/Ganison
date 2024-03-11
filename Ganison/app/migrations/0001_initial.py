# Generated by Django 5.0.3 on 2024-03-11 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answers', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assesment_Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assesment_areas', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sydney_participants', models.CharField(max_length=200)),
                ('sydney_percentile', models.CharField(max_length=200)),
                ('correct_answer_percentage_per_class', models.CharField(max_length=200)),
                ('participant', models.CharField(max_length=200)),
                ('correct_answers', models.CharField(max_length=200)),
                ('year_level', models.CharField(max_length=200)),
                ('average_score', models.CharField(max_length=200)),
            ],
        ),
    ]
