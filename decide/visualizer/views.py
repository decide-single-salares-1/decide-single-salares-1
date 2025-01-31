
import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404


import matplotlib.pyplot as plt

import aspose.words as aw
import telegram

#import aspose.words as aw


from base import mods

            
class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:

            bot_token = '5951418263:AAFhShQy3yYuk2SCjAF_E2YM6IO5XwYVqn4'
            chat_id = '-1001777911940'
            bot = telegram.Bot(token=bot_token)
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
            opci=[]
            votos=[]
            for v in r[0]["postproc"]:

                opci.append(v["option"]) 
                votos.append(v["votes"]) 
            fig, ax = plt.subplots()

            ax.set_ylabel('Votos')
       
            ax.set_title(r[0]["question"]["desc"])
  
            plt.bar(opci, votos)
            plt.savefig('barras_simple.png')
            
            fig, ax = plt.subplots()
            ax.pie(votos,labels=opci, autopct="%0.1f %%")
            plt.axis("equal")
            ax.set_title(r[0]["question"]["desc"])
            plt.savefig('pie_simple.png')

            doc = aw.Document()
          
            builder = aw.DocumentBuilder(doc)
           
    
            #Insertar imagen en el documento
           
            builder.insert_image("barras_simple.png")
            builder.insert_image("pie_simple.png")
            #Guardar como pdf
            doc.save("barras.pdf")
            with open('barras_simple.png', 'rb') as photo_file:
                           bot.sendPhoto(chat_id=chat_id,
                               photo=photo_file,
                               caption='Aqui esta una grafica de barras de la votacion')

            with open('pie_simple.png', 'rb') as photo_file:
                           bot.sendPhoto(chat_id=chat_id,
                               photo=photo_file,
                               caption='Aqui esta una grafica de pastel de la votacion')

            with open('barras.pdf', 'rb') as InputFile:
                           bot.sendDocument(chat_id=chat_id,
                               document=InputFile,
                               caption='Aqui esta una grafica de pastel de la votacion')
        except:
            raise Http404

        return context

class VisualizerViewENG(TemplateView):
    template_name = 'visualizer/visualizereng.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        return context


class VisualizerViewALE(TemplateView):
    template_name = 'visualizer/visualizerale.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        return context