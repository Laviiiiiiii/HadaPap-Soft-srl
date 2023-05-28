from django.contrib import admin
from .models import Filme, Utilizatori, Rating_Filme, Vizionari_Filme, Comentarii_Filme
admin.site.register(Filme)
admin.site.register(Utilizatori)
admin.site.register(Rating_Filme)
admin.site.register(Vizionari_Filme)
admin.site.register(Comentarii_Filme)
# Register your models here.
