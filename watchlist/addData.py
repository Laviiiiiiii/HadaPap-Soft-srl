from datetime import date
from models import Utilizatori, Filme, Rating_Filme, Vizionari_Filme, Comentarii_Filme


Utilizatori.objects.create(Nume_Utilizator='John Doe', Email='john.doe@example.com', Parola='parola1', Data_Inregistrare=date(2023, 1, 1))
Utilizatori.objects.create(ID_Utilizator=2, Nume_Utilizator='Jane Smith', Email='jane.smith@example.com', Parola='parola2', Data_Inregistrare=date(2023, 2, 5))
Utilizatori.objects.create(ID_Utilizator=3, Nume_Utilizator='Alex Johnson', Email='alex.johnson@example.com', Parola='parola3', Data_Inregistrare=date(2023, 3, 10))
Utilizatori.objects.create(ID_Utilizator=4, Nume_Utilizator='Emily Brown', Email='emily.brown@example.com', Parola='parola4', Data_Inregistrare=date(2023, 4, 15))
Utilizatori.objects.create(ID_Utilizator=5, Nume_Utilizator='Michael Wilson', Email='michael.wilson@example.com', Parola='parola5', Data_Inregistrare=date(2023, 5, 20))
Utilizatori.objects.create(ID_Utilizator=6, Nume_Utilizator='Sophia Davis', Email='sophia.davis@example.com', Parola='parola6', Data_Inregistrare=date(2023, 6, 25))
Utilizatori.objects.create(ID_Utilizator=7, Nume_Utilizator='William Miller', Email='william.miller@example.com', Parola='parola7', Data_Inregistrare=date(2023, 7, 30))
Utilizatori.objects.create(ID_Utilizator=8, Nume_Utilizator='Olivia Anderson', Email='olivia.anderson@example.com', Parola='parola8', Data_Inregistrare=date(2023, 8, 4))
Utilizatori.objects.create(ID_Utilizator=9, Nume_Utilizator='James Taylor', Email='james.taylor@example.com', Parola='parola9', Data_Inregistrare=date(2023, 9, 9))
Utilizatori.objects.create(ID_Utilizator=10, Nume_Utilizator='Emma Clark', Email='emma.clark@example.com', Parola='parola10', Data_Inregistrare=date(2023, 10, 14))


Filme.objects.create(ID_Film=1, Titlu='Inception', Regizor='Christopher Nolan', An_Lansare=2010, Gen='Thriller')
Filme.objects.create(ID_Film=2, Titlu='The Shawshank Redemption', Regizor='Frank Darabont', An_Lansare=1994, Gen='Drama')
Filme.objects.create(ID_Film=3, Titlu='Pulp Fiction', Regizor='Quentin Tarantino', An_Lansare=1994, Gen='Crime')
Filme.objects.create(ID_Film=4, Titlu='The Dark Knight', Regizor='Christopher Nolan', An_Lansare=2008, Gen='Action')
Filme.objects.create(ID_Film=5, Titlu='Fight Club', Regizor='David Fincher', An_Lansare=1999, Gen='Drama')
Filme.objects.create(ID_Film=6, Titlu='The Godfather', Regizor='Francis Ford Coppola', An_Lansare=1972, Gen='Crime')
Filme.objects.create(ID_Film=7, Titlu='The Matrix', Regizor='Lana Wachowski, Lilly Wachowski', An_Lansare=1999, Gen='Action')
Filme.objects.create(ID_Film=8, Titlu='Goodfellas', Regizor='Martin Scorsese', An_Lansare=1990, Gen='Crime')
Filme.objects.create(ID_Film=9, Titlu='Interstellar', Regizor='Christopher Nolan', An_Lansare=2014, Gen='Sci-Fi')
Filme.objects.create(ID_Film=10, Titlu='The Lord of the Rings: The Fellowship of the Ring', Regizor='Peter Jackson', An_Lansare=2001, Gen='Fantasy')




Rating_Filme.objects.create(ID_Rating=1, ID_Film=Filme.objects.get(pk=1), ID_Utilizator=Utilizatori.objects.get(pk=1), Rating=4.5, Data_Rating='2023-05-01')
Rating_Filme.objects.create(ID_Rating=2, ID_Film=Filme.objects.get(pk=2), ID_Utilizator=Utilizatori.objects.get(pk=1), Rating=3.8, Data_Rating='2023-05-02')
Rating_Filme.objects.create(ID_Rating=3, ID_Film=Filme.objects.get(pk=3), ID_Utilizator=Utilizatori.objects.get(pk=2), Rating=4.2, Data_Rating='2023-05-03')
Rating_Filme.objects.create(ID_Rating=4, ID_Film=Filme.objects.get(pk=4), ID_Utilizator=Utilizatori.objects.get(pk=2), Rating=3.5, Data_Rating='2023-05-04')
Rating_Filme.objects.create(ID_Rating=5, ID_Film=Filme.objects.get(pk=5), ID_Utilizator=Utilizatori.objects.get(pk=3), Rating=4.7, Data_Rating='2023-05-05')
Rating_Filme.objects.create(ID_Rating=6, ID_Film=Filme.objects.get(pk=6), ID_Utilizator=Utilizatori.objects.get(pk=3), Rating=4.1, Data_Rating='2023-05-06')
Rating_Filme.objects.create(ID_Rating=7, ID_Film=Filme.objects.get(pk=7), ID_Utilizator=Utilizatori.objects.get(pk=4), Rating=3.9, Data_Rating='2023-05-07')
Rating_Filme.objects.create(ID_Rating=8, ID_Film=Filme.objects.get(pk=8), ID_Utilizator=Utilizatori.objects.get(pk=4), Rating=4.3, Data_Rating='2023-05-08')
Rating_Filme.objects.create(ID_Rating=9, ID_Film=Filme.objects.get(pk=9), ID_Utilizator=Utilizatori.objects.get(pk=5), Rating=4.0, Data_Rating='2023-05-09')
Rating_Filme.objects.create(ID_Rating=10, ID_Film=Filme.objects.get(pk=10), ID_Utilizator=Utilizatori.objects.get(pk=6), Rating=3.6, Data_Rating='2023-05-10')



Vizionari_Filme.objects.create(ID_Vizionare=1, ID_Film=Filme.objects.get(pk=1), ID_Utilizator=Utilizatori.objects.get(pk=1), Data_Vizionare='2023-05-01', Durata=120)
Vizionari_Filme.objects.create(ID_Vizionare=2, ID_Film=Filme.objects.get(pk=2), ID_Utilizator=Utilizatori.objects.get(pk=1), Data_Vizionare='2023-05-02', Durata=105)
Vizionari_Filme.objects.create(ID_Vizionare=3, ID_Film=Filme.objects.get(pk=3), ID_Utilizator=Utilizatori.objects.get(pk=2), Data_Vizionare='2023-05-03', Durata=95)
Vizionari_Filme.objects.create(ID_Vizionare=4, ID_Film=Filme.objects.get(pk=4), ID_Utilizator=Utilizatori.objects.get(pk=2), Data_Vizionare='2023-05-04', Durata=110)
Vizionari_Filme.objects.create(ID_Vizionare=5, ID_Film=Filme.objects.get(pk=5), ID_Utilizator=Utilizatori.objects.get(pk=3), Data_Vizionare='2023-05-05', Durata=130)
Vizionari_Filme.objects.create(ID_Vizionare=6, ID_Film=Filme.objects.get(pk=6), ID_Utilizator=Utilizatori.objects.get(pk=3), Data_Vizionare='2023-05-06', Durata=115)
Vizionari_Filme.objects.create(ID_Vizionare=7, ID_Film=Filme.objects.get(pk=7), ID_Utilizator=Utilizatori.objects.get(pk=4), Data_Vizionare='2023-05-07', Durata=100)
Vizionari_Filme.objects.create(ID_Vizionare=8, ID_Film=Filme.objects.get(pk=8), ID_Utilizator=Utilizatori.objects.get(pk=4), Data_Vizionare='2023-05-08', Durata=125)
Vizionari_Filme.objects.create(ID_Vizionare=9, ID_Film=Filme.objects.get(pk=9), ID_Utilizator=Utilizatori.objects.get(pk=5), Data_Vizionare='2023-05-09', Durata=90)
Vizionari_Filme.objects.create(ID_Vizionare=10, ID_Film=Filme.objects.get(pk=10), ID_Utilizator=Utilizatori.objects.get(pk=6), Data_Vizionare='2023-05-10', Durata=105)



Comentarii_Filme.objects.create(ID_Comentariu=1, ID_Film=Filme.objects.get(pk=1), ID_Utilizator=Utilizatori.objects.get(pk=1), Comentariu='Foarte bun film!', Data_Comentariu='2023-05-01')
Comentarii_Filme.objects.create(ID_Comentariu=2, ID_Film=Filme.objects.get(pk=2), ID_Utilizator=Utilizatori.objects.get(pk=1), Comentariu='Interesantă poveste.', Data_Comentariu='2023-05-02')
Comentarii_Filme.objects.create(ID_Comentariu=3, ID_Film=Filme.objects.get(pk=3), ID_Utilizator=Utilizatori.objects.get(pk=2), Comentariu='M-a dezamăgit finalul.', Data_Comentariu='2023-05-03')
Comentarii_Filme.objects.create(ID_Comentariu=4, ID_Film=Filme.objects.get(pk=4), ID_Utilizator=Utilizatori.objects.get(pk=2), Comentariu='Recomand cu căldură!', Data_Comentariu='2023-05-04')
Comentarii_Filme.objects.create(ID_Comentariu=5, ID_Film=Filme.objects.get(pk=5), ID_Utilizator=Utilizatori.objects.get(pk=3), Comentariu='Nu mi-a plăcut deloc.', Data_Comentariu='2023-05-05')
Comentarii_Filme.objects.create(ID_Comentariu=6, ID_Film=Filme.objects.get(pk=6), ID_Utilizator=Utilizatori.objects.get(pk=3), Comentariu='Un film captivant.', Data_Comentariu='2023-05-06')
Comentarii_Filme.objects.create(ID_Comentariu=7, ID_Film=Filme.objects.get(pk=7), ID_Utilizator=Utilizatori.objects.get(pk=4), Comentariu='Personajele au fost foarte bine dezvoltate.', Data_Comentariu='2023-05-07')
Comentarii_Filme.objects.create(ID_Comentariu=8, ID_Film=Filme.objects.get(pk=8), ID_Utilizator=Utilizatori.objects.get(pk=4), Comentariu='Nu pot să-l uit!', Data_Comentariu='2023-05-08')
Comentarii_Filme.objects.create(ID_Comentariu=9, ID_Film=Filme.objects.get(pk=9), ID_Utilizator=Utilizatori.objects.get(pk=5), Comentariu='Mi-a plăcut coloana sonoră.', Data_Comentariu='2023-05-09')
Comentarii_Filme.objects.create(ID_Comentariu=10, ID_Film=Filme.objects.get(pk=10), ID_Utilizator=Utilizatori.objects.get(pk=6), Comentariu='Nu pot să-l recomand.', Data_Comentariu='2023-05-10')


