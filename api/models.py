from .abstract import TimestampAbstractModel
from django.utils.translation import gettext as _
from django.db import models


class Movie(TimestampAbstractModel):
    """
    Holds Movie objects with all fields available
    at OMDB, for simpler **kwargs later on nulls
    everywhere as I'm not 100% sure if each feed has
    all data
    """
    title = models.TextField(_('Title'),
                             help_text=_('Title of the movie'),
                             max_length=256
                             )
    year = models.CharField(_('Year'),
                            help_text=_('Year of release'),
                            blank=True, null=True,
                            max_length=10
                            )
    rated = models.CharField(_('Rated'),
                             help_text=_('PG rating'),
                             max_length=50,
                             blank=True, null=True
                             )
    released = models.CharField(_('Released'),
                                help_text=_('Date of release'),
                                max_length=30,
                                blank=True, null=True
                                )
    runtime = models.TextField(_('Runtime'),
                               help_text=_('Length of movie (mins)'),
                               blank=True, null=True
                               )
    genre = models.TextField(_('Genre'),
                             max_length=200,
                             blank=True, null=True
                             )
    director = models.TextField(_('Director'),
                                max_length=200,
                                blank=True, null=True
                                )
    writer = models.TextField(_('Writer'),
                              max_length=1000,
                              blank=True, null=True
                              )
    actors = models.TextField(_('Actors'),
                              max_length=2000,
                              blank=True, null=True
                              )
    plot = models.TextField(_('Plot'),
                            max_length=3000,
                            blank=True, null=True
                            )
    language = models.CharField(_('Language'),
                                max_length=50,
                                blank=True, null=True
                                )
    country = models.CharField(_('Country'),
                               max_length=100,
                               blank=True, null=True
                               )
    awards = models.TextField(_('Awards'),
                              max_length=1000,
                              blank=True, null=True
                              )

    poster = models.CharField(_('Poster'),
                              max_length=2000,
                              blank=True, null=True
                             )

    metascore = models.CharField(_('Metascore'),
                                 blank=True, null=True,
                                 max_length=10
                                 )

    imdbrating = models.CharField(_('IMDB Rating'),
                                  max_length=30,
                                  blank=True, null=True
                                  )

    imdbvotes = models.CharField(_('IMDB votes'),
                                 max_length=30,
                                 blank=True, null=True
                                 )

    imdbid = models.CharField(_('IMDB ID'),
                              max_length=50,
                              blank=True, null=True
                              )
    type = models.CharField(_('Type'),
                            max_length=100,
                            blank=True, null=True
                            )
    dvd = models.CharField(_('DVD release date'),
                           blank=True, null=True,
                           max_length=30
                           )

    boxoffice = models.CharField(_('Box Office'),
                                 max_length=100,
                                 blank=True, null=True,
                                 )

    production = models.CharField(_('Production'),
                                  max_length=500,
                                  blank=True, null=True,
                                  )
    website = models.CharField(_('Website'),
                               max_length=2000,
                               blank=True, null=True
                               )
    # imagine this is big. Recalculating entire database of comments
    # every time to show how many of these are already present will
    # be painful
    comments_count = models.PositiveIntegerField(_('Comments count'),
                                                 blank=True, default=0
                                                 )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-comments_count']


class Comment(TimestampAbstractModel):
    """
    Holds comment content, FKs to Movie
    """
    movie = models.ForeignKey(Movie,
                              related_name='comments',
                              on_delete=models.CASCADE,
                              )
    content = models.TextField(_('Comment content'),
                               max_length=2000
                               )

    def __str__(self):
        return self.movie.title
