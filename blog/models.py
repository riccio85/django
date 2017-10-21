from django.db import models
from django.utils import timezone

"""
    per importare
 # import nome modulo
 # from django.db import models la differenza l'aias come chimarlo si puo dare ex. import napi ad np

 tutto quello dentro cuna class è variabile di istanza
 se uno vuole far diversamente bisogna unsare la funzione init
 Post(models.Model) == Post extends models.Model
 self== this
 __str__ == toString()
 quando uno definisce una funzione def publish(self) usa self -- publish viene chiamato senza paramentero
 senza self diventa come se fosse un metodo statico

"""

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
