# Generated by Django 4.1.1 on 2022-09-17 15:08

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_id', models.CharField(max_length=100, verbose_name='Quest ID')),
                ('user_id', models.CharField(max_length=50, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'QuestCounter',
                'verbose_name_plural': 'QuestCounter',
                'db_table': 'quest_counter',
                'ordering': ['quest_id', 'user_id'],
            },
        ),
        migrations.AddConstraint(
            model_name='questcounter',
            constraint=models.UniqueConstraint(fields=('quest_id', 'user_id'), name='unique_user_id_for_quest_id'),
        ),
        migrations.AddConstraint(
            model_name='questcounter',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('quest_id'), django.db.models.functions.text.Lower('user_id'), name='unique_user_id_quest_id_lower'),
        ),
        migrations.AlterUniqueTogether(
            name='questcounter',
            unique_together={('quest_id', 'user_id')},
        ),
    ]
