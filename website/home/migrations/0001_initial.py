# Generated by Django 3.0 on 2021-05-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('published', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]