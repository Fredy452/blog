"""Blog model"""
# Django
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Base model.
    BaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class Category(BaseModel):
    """Category model."""
    name = models.CharField('nombre', max_length=50, unique=True)
    slug = models.SlugField('slug', unique=True, help_text='Una URL-amigable representación del nombre')
    description = models.TextField('descripción', blank=True, null=True)

    class Meta:
        """Meta options."""
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        """Return name."""
        return self.name

    def get_absolute_url(self):
        return f'hotel/blog/category/{self.slug}/'


class Tag(BaseModel):
    """Tag model."""
    name = models.CharField('nombre', max_length=50, unique=True)
    slug = models.SlugField('slug', unique=True, help_text='Una URL-amigable representación del nombre')
    description = models.TextField('descripción', blank=True, null=True)

    class Meta:
        """Meta options."""
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        """Return name."""
        return self.name

    def get_absolute_url(self):
        return f'hotel/blog/tag/{self.slug}/'


class Post(BaseModel):
    """Post model."""
    title = models.CharField('titulo', max_length=200)
    slug = models.SlugField('slug', unique=True, help_text='Una URL-amigable representación del titulo')
    content = models.TextField('contenido')
    image = models.ImageField('imagen', upload_to='blog/', blank=True, null=True)
    published = models.BooleanField('publicado', default=False)
    author = models.ForeignKey('auth.User', verbose_name='autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField('blogs.Category', verbose_name='categorias', related_name='get_posts')
    tags = models.ManyToManyField('blogs.Tag', verbose_name='etiquetas', related_name='get_posts')

    class Meta:
        """Meta options."""
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        """Return title."""
        return self.title

    def get_absolute_url(self):
        return f'hotel/blog/{self.slug}/'
