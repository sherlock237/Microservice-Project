# Generated by Django 3.2.8 on 2023-10-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInteraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('content_id', models.IntegerField()),
                ('interaction_type', models.CharField(choices=[('LIKE', 'Like'), ('READ', 'Read')], max_length=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
