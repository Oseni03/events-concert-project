from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Image(models.Model):
    fallback = models.BooleanField(default=False)
    image_url = models.URLField()


class Location(models.Model):
    country =  CountryField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return "{}, {}, {}".format(self.city, self.state, self.country)


class Venue(models.Model):
    discovery_id = models.CharField(max_length=50) 
    header_image = models.ForeignKey(Image, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    is_livenation_owned = models.BooleanField()
    slug = models.SlugField(null=True, blank=True)
    tm_id = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)


class Event(models.Model):
    class StatusChoice(models.TextChoices):
        ONSALE = "onsale", _("Onsale")
        OFFSALE = "offsale", _("Offsale")
        RESCHEDULED = "rescheduled", _("Rescheduled")
        CANCELLED = "cancelled", _("Cancelled")
        POSTPONED = "postponed", _("Postponed")
    
    class TypeChoice(models.TextChoices):
        FESTIVAL = "FESTIVAL", _("Festival")
        REGULAR = "REGULAR", _("Regular")
        
    discovery_id = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    status_code = models.CharField(max_length=25, choices=StatusChoice.choices)
    links = URLField(null=True, blank=True)
    name = models.CharField(max_length="255")
    sales_start_date_time = models.DateTimeField()
    similar_event_count = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)
    tm_id = models.CharField(max_length=50)
    type = models.CharField(max_length=100, choices=TypeChoice.choices)
    url = URLField(null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, related_name="events")
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ("-datetime",)


class UpSell(models.Model):
    classification_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    url = models.URLField()
    
    def __str__(self):
        return str(self.name)


class Genre(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)


class Artist(models.Model):
    discovery_id = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    
    def __str__(self):
        return str(self.name)
