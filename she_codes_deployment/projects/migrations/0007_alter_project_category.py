# Generated by Django 4.2.3 on 2023-09-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_idol_name_alter_project_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.category'),
        ),
    ]
