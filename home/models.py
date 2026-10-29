from django.db import models

from wagtail.admin.panels import FieldPanel #rend un champ visible dans l'admin
from wagtail.fields import RichTextField #champ de tecte avec mise en forme
from wagtail.models import Page


class HomePage(Page):
    accroche = models.CharField(max_length=255, blank=True) #une ligne de texte de 255 caractères max
    
    introduction = RichTextField(blank=True) #plusieurs paragraphes, avec mise en forme

    content_panels = Page.content_panels + [
        FieldPanel("accroche"),        #affiche accroche dans l'admin
        FieldPanel("introduction"),    #affiche introduction dans l'admin      
    ]


    
