from django.db import models


class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    link = models.URLField()
    # date_created = models.DateTimeField(null=True)
    # visits = models.IntegerField(null=True)

    def __str__(self):
        return f"ID: {self.url_id} , main URL {self.link}"





