import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import telegram

import aspose.words as aw
from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
    
        bot_token = '5951418263:AAFhShQy3yYuk2SCjAF_E2YM6IO5XwYVqn4'
        chat_id = '-1001777911940'
        bot = telegram.Bot(token=bot_token)
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)
        print(vid)
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
            with open('barras_simple.png', 'rb') as photo_file:
                            bot.sendPhoto(chat_id=chat_id,
                                photo=photo_file,
                                caption='Aqui esta una grafica de la votacion')
            
            # Crear un nuevo documento
            doc = aw.Document()
            # Crear un generador de documentos
            builder = aw.DocumentBuilder(doc)
            # Insertar imagen en el documento
            builder.insert_image("barras_simple.png")

            # Guardar como pdf
            doc.save("barras.pdf")
            
        
        
        except:
            raise Http404

        return context
