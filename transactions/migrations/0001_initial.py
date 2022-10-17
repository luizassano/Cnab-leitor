from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stores", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("type", models.CharField(max_length=1)),
                ("date", models.DateField()),
                ("value", models.FloatField()),
                ("hour", models.TimeField()),
                ("card", models.CharField(max_length=12)),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="stores.store",
                    ),
                ),
            ],
        ),
    ]