from django.db import models


class Feed(models.Model):
    url = models.URLField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'URLs'

    def __str__(self):
        return self.url

    def __repr__(self):
        return "<Feed '{}'>".format(self.url)
