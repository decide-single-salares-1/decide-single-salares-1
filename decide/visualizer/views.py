import json
from census.models import Census
from store.models import Vote
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)
        

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
            total_participation = '0%'
            total_number_of_votes = 0
            a = 0
            b = 0

            if r[0].get('start_date'):
                votes = Vote.object.filter(voting_id = vid)
                total_number_of_votes = Vote.object.filter(voting_id = vid).count()
                for p in votes: 
                    total_number_of_votes += 1
                    a += context.get('a')
                    b += context.get('b')
                    if total_number_of_votes != 0:
                        total_participation = (p + '{total_number_of_votes * 100}' + '%')
                    else:
                        total_participation = '%'
                aux_a = a / total_number_of_votes
                aux_b = b / total_number_of_votes

            inforealtime = {'total_participation':total_participation, 'total_number_of_votes':total_number_of_votes, 'auxa':a, 'auxb':b}
            context['inforealtime'] = inforealtime

        except:
            raise Http404

        return context