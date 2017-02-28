from django.shortcuts import render, get_object_or_404
from podcast.models import Episode, Show

def episode_list(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    eps = Episode.objects.filter(show=show_id)
    return render(request, 'podcast/episode_list.html', {'show':show, 'eps':eps})

def dl(request):
    episode = Episode.objects.get(pk=1)
    from django.contrib.sites.shortcuts import get_current_site
    from django.contrib.syndication.views import add_domain
    from urllib2 import urlopen
    from django.http import HttpResponse
    current_site = get_current_site(request)
    domain_url = add_domain(current_site.domain, episode.enclosure.file.url, False)
    response = HttpResponse(urlopen(domain_url), content_type=episode.enclosure.type)
    response['Content-Disposition'] = 'attachment; filename="%s.%s%s"' % (episode.show.slug, episode.slug, episode.enclosure.get_extension())
    return response
