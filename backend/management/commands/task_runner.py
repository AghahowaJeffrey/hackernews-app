from django.core.management.base import BaseCommand
from backend.task import start_interval, start_task



class Command(BaseCommand):
    help = "Runs the Schedular task when server starts"
    
    def handle(self, *args, **options):
        start_task()
        start_interval()