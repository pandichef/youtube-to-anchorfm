import os
from django.shortcuts import render
from django.http import HttpResponse


def save_id_to_episode_json(youtube_id):
    string_to_write = "{" + f' "id": "{youtube_id}" ' + "}\n"
    with open('episode.json', 'w') as f:
        f.write(string_to_write)


def push_new_episode_json_to_github(youtube_id):
    os.system('git add episode.json')
    os.system(f'git commit -m "Push {youtube_id} to Anchor"')
    os.system('git push origin main')


def index(request):
    youtube_id = request.GET['id']
    save_id_to_episode_json(youtube_id)
    push_new_episode_json_to_github(youtube_id)
    return HttpResponse(
        f"Done.  YouTube video {youtube_id} should appear on Anchor in a few minutes."
    )
