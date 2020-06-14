from django.db import models
import django
# Create your models here.
class AwAboutAromaWines(models.Model):
    Title = models.CharField(max_length=120)
    description = models.TextField()
    Create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Title)
    class Meta:
        verbose_name_plural = "Aw About Aroma Wines"