from django.core.management.base import BaseCommand
from backend.task import start


class Command(BaseCommand):
    help = "Description of your custom command"

    def handle(self, *args, **options):
        self.stdout.write("Running your custom command...")
        start() 
        self.stdout.write(self.style.SUCCESS("Your custom command completed!"))