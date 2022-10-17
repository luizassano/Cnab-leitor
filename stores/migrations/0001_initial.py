from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("store_owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
                ("cpf", models.CharField(max_length=11)),
            ],
        ),
    ]