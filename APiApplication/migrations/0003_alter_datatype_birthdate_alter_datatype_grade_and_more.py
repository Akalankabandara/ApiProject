# Generated by Django 5.0.3 on 2024-03-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APiApplication', '0002_alter_datatype_birthdate_alter_datatype_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='birthdate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='grade',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='row_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='score',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
