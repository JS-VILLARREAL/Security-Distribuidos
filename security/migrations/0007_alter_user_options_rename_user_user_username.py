# Generated by Django 4.2.6 on 2023-11-10 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_module_route_view_route'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='username',
        ),
    ]