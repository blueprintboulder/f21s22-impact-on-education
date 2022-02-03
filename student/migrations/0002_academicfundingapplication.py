# Generated by Django 3.2.11 on 2022-02-03 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_applicant', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicFundingApplication',
            fields=[
                ('application_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_applicant.application')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.TextField()),
                ('school', models.TextField()),
                ('role', models.BooleanField()),
                ('department', models.TextField()),
                ('needs_assistance', models.TextField()),
                ('funding_for', models.TextField()),
                ('funding_need', models.TextField()),
                ('funding_amount', models.TextField()),
                ('students_impacted', models.TextField()),
            ],
            bases=('base_applicant.application',),
        ),
    ]
