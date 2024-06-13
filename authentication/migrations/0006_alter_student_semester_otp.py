# Generated by Django 4.2 on 2024-06-12 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_student_semester_alter_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('1', '1th'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th')], max_length=50),
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]