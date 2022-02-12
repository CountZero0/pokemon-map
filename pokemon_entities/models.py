from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='Имя (RU)', max_length=200)
    title_en = models.CharField(verbose_name='Имя (EN)', max_length=200, blank=True)
    title_jp = models.CharField(verbose_name='Имя (JP)', max_length=200, blank=True)
    description = models.TextField(verbose_name='Описание', default='', blank=True)
    image = models.ImageField(verbose_name='Изображение', blank=True)
    evolution_from = models.ForeignKey('self',
                                       related_name='next_evolutions',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       verbose_name='Эволюционирует из')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                related_name='pokemons',
                                null=True,
                                verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', null=True, blank=True)
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Сила', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon.title} по координатам: {self.lat, self.lon}"
