# Generated by Django 4.2.2 on 2023-06-12 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_dep_description_department_dept_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.CharField(max_length=100)),
                ('doc_img', models.ImageField(upload_to='doctors')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.department')),
            ],
        ),
    ]
