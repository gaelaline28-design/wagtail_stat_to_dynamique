from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images.models import Image #Importer le modèle d'image de Wagtail

from wagtail.models import Page

class PrestationsPage(Page):

    # nouveau champ texte riche
    introduction = RichTextField(blank=True) 

    # rend le champ visible dans l'admin
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),  
    ]

class EquipePage(Page):
    #rendre image dinamique
    image_dynamique = models.ForeignKey(
        'wagtailimages.Image',  # Lien vers la bibliothèque d'images Wagtail
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image de la section L'équipe"
    )
    content_panels = Page.content_panels + [
            # Ajoutez le champ dans l'interface d'administration
            FieldPanel('image_dynamique'),
    ]


class ContactPage(Page):
    pass
