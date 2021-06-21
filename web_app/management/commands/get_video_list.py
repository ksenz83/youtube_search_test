from django.core.management.base import BaseCommand, CommandError
from web_app.services import get_video_list


class Command(BaseCommand):
    help='Get video list for test'

    def handle(self, *args, **options):
        get_video_list()
