from django.db import migrations


def owners_discription(apps, schema_editor):
    Owner = apps.get_model("property", "Owner")
    Flat = apps.get_model("property", "Flat")
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            full_name = flat.owner,
            owners_phonenumber = flat.owners_phonenumber,
            owner_pure_phone = flat.owner_pure_phone
        )
        

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20210327_1744'),
    ]

    operations = [
        migrations.RunPython(owners_discription)
    ]
