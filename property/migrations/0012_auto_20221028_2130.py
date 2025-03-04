# Generated by Django 2.2.24 on 2022-10-28 18:30
from django.db import migrations


def copy_all_owner_to_new_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flat_set = Flat.objects.all()
    for flat in flat_set.iterator():
        full_name = flat.owners
        owner_pure_phone = flat.owner_pure_phone
        owners_phonenumber = flat.owners_phonenumber
        owners = Owner.objects.get_or_create(owner=full_name, phone_number=owners_phonenumber,
                                     pure_phone=owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20221028_2121'),
    ]

    operations = [
        migrations.RunPython(copy_all_owner_to_new_model),
    ]
