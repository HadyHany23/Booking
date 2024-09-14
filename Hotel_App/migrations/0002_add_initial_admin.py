from django.db import migrations
from django.contrib.auth.models import User

def create_admin(apps, schema_editor):
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpassword',
        id=0,
    )

class Migration(migrations.Migration):

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
