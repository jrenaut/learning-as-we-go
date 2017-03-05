from django.shortcuts import render, get_object_or_404
from podcast.models import Episode, Show
from .models import Bio

def episode_list(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    eps = Episode.objects.filter(show=show_id)
    return render(request, 'podcast/episode_list.html', {'show':show, 'eps':eps})

def meet_the_kids(request):
    bios = Bio.objects.all()
    return render(request, 'meet_the_kids.html', {'bios':bios})
    
def show_bio(request, bio_id):
    b = Bio.objects.get(pk=bio_id)
    return render(request, 'bio.html', {'bio': b})
