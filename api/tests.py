from django.test import TestCase
from django.urls import reverse
from unittest import mock

from rest_framework.test import APIClient

from api.models import Movie, Comment


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(title="TestTitle")

    def _mock_response(self):
        json_data = {
            "title": "Guardians of the Galaxy Vol. 2",
            "year": "2017",
            "rated": "PG-13",
            "released": "05 May 2017",
            "runtime": "136 min",
            "genre": "Action, Adventure, Comedy, Sci-Fi",
            "director": "James Gunn",
            "writer": "James Gunn, Dan Abnett "
                      "(based on the Marvel comics by), "
                      "Andy Lanning (based on the Marvel "
                      "comics by), Steve Englehart "
                      "(Star-Lord created by), Steve Gan "
                      "(Star-Lord created by), "
                      "Jim Starlin (Gamora and Drax created by),"
                      " Stan Lee (Groot created by),"
                      " Larry Lieber (Groot created by), "
                      "Jack Kirby (Groot created by), "
                      "Bill Mantlo (Rocket Raccoon created by),"
                      " Keith Giffen "
                      "(Rocket Raccoon created by), Steve Gerber"
                      " (Howard the Duck created by), "
                      "Val Mayerik (Howard the Duck created by)",
            "actors": "Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel",
            "plot": "The Guardians struggle to keep "
                    "together as a team "
                    "while dealing with their personal "
                    "family issues, "
                    "notably Star-Lord's encounter with "
                    "his father the ambitious celestial being Ego.",
            "language": "English",
            "country": "USA",
            "awards": "Nominated for 1 Oscar. Another "
                      "12 wins & 42 nominations.",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SX300.jpg",  # noqa
            "ratings": [
                {
                    "source": "Internet Movie Database",
                    "value": "7.7/10"
                },
                {
                    "source": "Rotten Tomatoes",
                    "value": "84%"
                },
                {
                    "source": "Metacritic",
                    "value": "67/100"
                }
            ],
            "metascore": "67",
            "imdbRating": "7.7",
            "imdbVotes": "471,312",
            "imdbID": "tt3896198",
            "type": "movie",
            "dvd": "22 Aug 2017",
            "boxoffice": "$389,804,217",
            "production": "Walt Disney Pictures",
            "website": "https://marvel.com/guardians",
            "response": "True"
        }

        mock_resp = mock.Mock()
        mock_resp.status_code = 200
        mock_resp.json = mock.Mock(return_value=json_data)
        return mock_resp

    def test_movies_list_endpoint(self):
        r = self.client.get(reverse('movies-list'))
        self.assertEqual(r.status_code, 200)

    def test_movies_detail_endpoint(self):
        r = self.client.get(reverse('movies-detail', kwargs={'pk': self.movie.pk}))
        self.assertEqual(r.status_code, 200)

    def test_movies_update_endpoint(self):
        r = self.client.put(reverse('movies-detail', kwargs={'pk': self.movie.pk}),
                            {'title': 'namechanged'})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Movie.objects.first().title, 'namechanged')

    def test_movies_delete_endpoint(self):
        r = self.client.delete(reverse('movies-detail', kwargs={'pk': self.movie.pk}))
        self.assertEqual(Movie.objects.count(), 0)
        self.assertEqual(r.status_code, 204)

    def test_comments_endpoint_get(self):
        r = self.client.get(reverse('comments'))
        self.assertEqual(r.status_code, 200)

    def test_top_endpoint(self):
        r = self.client.get(reverse('top'))
        self.assertEqual(r.status_code, 200)

    @mock.patch('requests.get')
    def test_movies_create_endpoint(self, mock_get):
        mock_resp = self._mock_response()
        mock_get.return_value = mock_resp
        movies_count = Movie.objects.count()
        r = self.client.post(reverse('movies-list'), {"title": "Test"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Movie.objects.count(), movies_count + 1)

    def test_comment_create_endpoint(self):
        comments_count = Comment.objects.count()
        r = self.client.post(reverse('comments'),
                             {"movie": self.movie.pk, "content": "test"})
        self.assertEqual(Movie.objects.count(), comments_count + 1)
        self.assertEqual(Comment.objects.last().movie.comments_count, 1)
        self.assertEqual(r.status_code, 201)

    def test_top_list_endpoint(self):
        r = self.client.get(reverse('top'))
        self.assertEqual(r.status_code, 200)
