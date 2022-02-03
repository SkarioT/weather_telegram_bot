from django.db import models

# Create your models here.

class City_Geo (models.Model):
    geo_name =models.CharField(
        verbose_name="City Name",
        max_length=100
        )
    geo_lat=models.CharField(
        verbose_name="Geo lat",
        max_length=20
        )
    geo_lon=models.CharField(
        verbose_name="Geo lon",
        max_length=20
        )
    geo_description =models.CharField(
        verbose_name="Description",
        max_length=200
        )
    def __str__(self):
        return self.geo_name +" "+ self.geo_lat+' '+self.geo_lon+' '+self.geo_description

class City_weather(models.Model):
    # weather_cur_date,
    # weather_temp,
    # weather_azuzhenie,
    # weather_condition,
    # weather_wind_speed,
    # weather_wind_gust,
    # weather_wind_dir,
    # weather_pressure_mm,
    # weather_humidity
    city = models.ForeignKey(
        City_Geo,
        related_name='weather',
        on_delete=models.CASCADE
        )

    weather_cur_date=models.CharField(
        verbose_name="weather_cur_date",
        max_length=50
    )
    weather_temp=models.CharField(
        verbose_name="weather_temp",
        max_length=50
    )
    weather_azuzhenie=models.CharField(
        verbose_name="weather_azuzhenie",
        max_length=50
    )
    weather_condition=models.CharField(
        verbose_name="weather_condition",
        max_length=50
    )
    weather_wind_speed=models.CharField(
        verbose_name="weather_wind_speed",
        max_length=50
    )
    weather_wind_gust=models.CharField(
        verbose_name="weather_wind_gust",
        max_length=50
    )
    weather_wind_dir=models.CharField(
        verbose_name="weather_wind_dir",
        max_length=50
    )
    weather_pressure_mm=models.CharField(
        verbose_name="weather_pressure_mm",
        max_length=50
    )
    weather_humidity=models.CharField(
        verbose_name="weather_humidity",
        max_length=50
    )
    # description = models.TextField(
    #     verbose_name="Информация об атворе",
    #     null=True,
    #     blank=True,
    #     default='Информация об авторе скоро будет добавлена на сайт. Сделать ее более полной и интересной помогут объективные отзывы тех, кто хорошо знаком с творчеством и фактами биографии данного автора. Оставляйте свои комментарии, делитесь впечатлениями и вступайте в дискуссии — это поможет другим сделать выбор.'
    # )
    def __str__(self):
        return f"{self.city.geo_name} {self.weather_cur_date} {self.weather_temp}"
