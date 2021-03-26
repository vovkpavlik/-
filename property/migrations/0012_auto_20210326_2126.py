from django.db import migrations
import phonenumbers


def owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        pure_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(pure_number):
            flat.owner_pure_phone = pure_number
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_owner_pure_phone'),
    ]


    operations = [
        migrations.RunPython(owner_pure_phone)
    ]

