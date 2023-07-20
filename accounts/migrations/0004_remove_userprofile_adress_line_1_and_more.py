# Generated by Django 4.2.3 on 2023-07-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='adress_line_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='adress_line_2',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'Customer')], null=True),
        ),
    ]