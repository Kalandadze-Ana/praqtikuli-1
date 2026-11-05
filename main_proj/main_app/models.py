from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    full_name = models.CharField(max_length=150)
    biography = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField()
    is_published = models.BooleanField(default=True)

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )

    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.OneToOneField(
        Movie,
        on_delete=models.CASCADE,
        related_name="rating"
    )
    score = models.FloatField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.score}"


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    author = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.movie.title}"
    