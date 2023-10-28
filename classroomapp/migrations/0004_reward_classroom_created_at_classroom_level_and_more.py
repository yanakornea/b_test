# Generated by Django 4.1 on 2023-10-27 13:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("classroomapp", "0003_alter_classroom_class_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reward_name", models.CharField(max_length=256)),
                ("point_to_redeem", models.IntegerField()),
                ("available_reward", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("update_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name="classroom",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="classroom",
            name="level",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="classroom",
            name="update_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="mission",
            name="available_mission",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="mission",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="mission",
            name="mission_tag",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="mission",
            name="update_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="mission_log",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="mission_log",
            name="update_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="student",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="student",
            name="update_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="teacher",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="teacher",
            name="update_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="student",
            name="net_point",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="Reward_Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(max_length=125)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("update_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classroomapp.classroom",
                    ),
                ),
                (
                    "reward",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classroomapp.reward",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classroomapp.student",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classroomapp.teacher",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="reward",
            name="class_reward",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="classroomapp.classroom"
            ),
        ),
    ]
