import os
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required


def save_id_to_episode_json(youtube_id):
    string_to_write = "{" + f' "id": "{youtube_id}" ' + "}\n"
    with open('episode.json', 'w') as f:
        f.write(string_to_write)


def push_new_episode_json_to_github(youtube_id):
    # Note: git commands can be run from Django subdirectory
    # They don't need to run from git top level directory
    # django_directory = os.getcwd()
    # os.chdir('..')  # github repo is here
    os.system('git add episode.json')
    os.system(f'git commit -m "Push {youtube_id} to Anchor"')
    os.system('git push origin main')
    # os.chdir(django_directory)


@login_required(login_url='/admin/login/')
def index(request):
    try:
        youtube_id = request.GET['id']
    except MultiValueDictKeyError:
        return HttpResponse(
            'Error.  You must pass a YouTube video ID as GET key "id".')
    save_id_to_episode_json(youtube_id)
    push_new_episode_json_to_github(youtube_id)
    return HttpResponse(
        f"Done.  YouTube video {youtube_id} should appear on Anchor in a few minutes."
    )
