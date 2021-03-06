# Generated by Django 3.2 on 2022-06-07 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coxit_staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=50)),
                ('deadline_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'academy_assignments',
            },
        ),
        migrations.CreateModel(
            name='AcademyStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('birthday', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='coxit_staff.coxitworker')),
            ],
            options={
                'db_table': 'academy_students',
            },
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=30)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coxit_academy.academyassignment')),
                ('revisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coxit_staff.coxitworker')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coxit_academy.academystudent')),
            ],
            options={
                'db_table': 'academy_assignment_submissions',
            },
        ),
        migrations.CreateModel(
            name='AcademyLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date', models.DateField(null=True)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coxit_staff.coxitworker')),
            ],
            options={
                'db_table': 'academy_lectures',
            },
        ),
        migrations.AddField(
            model_name='academyassignment',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coxit_academy.academylecture'),
        ),
    ]
