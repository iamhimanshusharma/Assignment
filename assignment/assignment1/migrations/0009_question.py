# Generated by Django 3.0.7 on 2021-08-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0008_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestionsText', models.CharField(max_length=100, null=True)),
                ('GradeId', models.CharField(max_length=100)),
                ('Grade', models.CharField(max_length=200, null=True)),
                ('SubjectID', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]