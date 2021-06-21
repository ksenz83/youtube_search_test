from youtube_search_test.celery import app
from .services import get_video_list


@app.task()
def get_video_list_task():
    print('start task')
    get_video_list()
