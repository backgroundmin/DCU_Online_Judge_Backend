# Generated by Django 2.1.7 on 2020-02-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0014_auto_20200222_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup_class',
            old_name='apply_user',
            new_name='isallow',
        ),
        migrations.AddField(
            model_name='lecture',
            name='isapply',
            field=models.BooleanField(default=False),
        ),
    ]
