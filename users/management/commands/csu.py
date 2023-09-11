from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='staff@sky.pro',
            first_name='Staff',
            last_name= 'Learning_platform',
            is_staff=True,
        )

        user.set_password('1234')
        user.save()
