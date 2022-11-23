import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

import matplotlib
import matplotlib.pyplot as plt
import numpy as np



from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
    
        
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            
            V=json.dumps(r[0])
            context['voting'] = json.dumps(r[0])
            opci=[]
            votos=[]
            for v in r[0]["postproc"]: 
                opci.append(v["option"]) 
                votos.append(v["votes"]) 
            fig, ax = plt.subplots()
            #Colocamos una etiqueta en el eje Y
            ax.set_ylabel('Votos')
            #Colocamos una etiqueta en el eje X
            ax.set_title('Cantidad de Votos por opcion')
            #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
            plt.bar(opci, votos)
            plt.savefig('barras_simple.png')

            
            
        
        
        except:
            raise Http404

        return context
