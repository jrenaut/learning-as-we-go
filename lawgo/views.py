from django.shortcuts import render, get_object_or_404
from podcast.models import Episode, Show

def episode_list(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    eps = Episode.objects.filter(show=show_id)
    return render(request, 'podcast/episode_list.html', {'show':show, 'eps':eps})
