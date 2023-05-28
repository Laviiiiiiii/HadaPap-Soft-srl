from django.db import models


class Utilizatori(models.Model):
    ID_Utilizator = models.IntegerField(primary_key=True)
    Nume_Utilizator = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=100, null=True)
    Parola = models.CharField(max_length=50, null=True)
    Data_Inregistrare = models.DateField(null=True)
    Durata_Totala_Vizionari = models.IntegerField(null=True)


class Filme(models.Model):
    ID_Film = models.IntegerField(primary_key=True)
    Titlu = models.CharField(max_length=100, null=True)
    Regizor = models.CharField(max_length=100, null=True)
    An_Lansare = models.IntegerField(null=True)
    Gen = models.CharField(max_length=50, null=True)
    Rating_Mediu = models.DecimalField(max_digits=3, decimal_places=1, null=True)


class Rating_Filme(models.Model):
    ID_Rating = models.IntegerField(primary_key=True)
    ID_Film = models.ForeignKey(Filme, on_delete=models.CASCADE, null=True)
    ID_Utilizator = models.ForeignKey(Utilizatori, on_delete=models.CASCADE, null=True)
    Rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    Data_Rating = models.DateField(null=True)


class Vizionari_Filme(models.Model):
    ID_Vizionare = models.IntegerField(primary_key=True)
    ID_Film = models.ForeignKey(Filme, on_delete=models.CASCADE, null=True)
    ID_Utilizator = models.ForeignKey(Utilizatori, on_delete=models.CASCADE, null=True)
    Data_Vizionare = models.DateField(null=True)
    Durata = models.IntegerField(null=True)


class Comentarii_Filme(models.Model):
    ID_Comentariu = models.IntegerField(primary_key=True)
    ID_Film = models.ForeignKey(Filme, on_delete=models.CASCADE, null=True)
    ID_Utilizator = models.ForeignKey(Utilizatori, on_delete=models.CASCADE, null=True)
    Comentariu = models.TextField(null=True)
    Data_Comentariu = models.DateField(null=True)


class CalculeazaDurataTotalaVizionari(models.Model):
    class Meta:
        managed = False  # This model is a database view or a custom SQL query

    id = models.IntegerField(primary_key=True)  # Primary key column is required for Django models
    durataTotala = models.IntegerField()


class CalculeazaMediaRatingFilm(models.Model):
    class Meta:
        managed = False  # This model is a database view or a custom SQL query

    id = models.IntegerField(primary_key=True)  # Primary key column is required for Django models
    media = models.DecimalField(max_digits=3, decimal_places=1)


class CalculeazaSumaRatingFilm(models.Model):
    class Meta:
        managed = False  # This model is a database view or a custom SQL query

    id = models.IntegerField(primary_key=True)  # Primary key column is required for Django models
    sumaRating = models.DecimalField(max_digits=5, decimal_places=2)


class VerificaVizionareFilm(models.Model):
    class Meta:
        managed = False  # This model is a database view or a custom SQL query

    id = models.IntegerField(primary_key=True)  # Primary key column is required for Django models
    exista = models.BooleanField()
