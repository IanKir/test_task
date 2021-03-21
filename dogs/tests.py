from django.test import TestCase
from .models import Breed, Dog


class DogTestCase(TestCase):
    def setUp(self):
        beagle = Breed.objects.create(name='beagle', slug='beagle', description='some description')
        boxer = Breed.objects.create(name='boxer', slug='boxer', description='some description 2')
        Dog.objects.create(nickname='lion', slug='lion', breed=beagle)
        Dog.objects.create(nickname='sharik', slug='sharik', breed=boxer)

    def test_dogs_str_method(self):
        lion = Dog.objects.get(slug='lion')
        sharik = Dog.objects.get(slug='sharik')
        self.assertEqual(lion.nickname, 'lion')
        self.assertEqual(sharik.nickname, 'sharik')

    def test_breed_retrieval_from_dog(self):
        lion = Dog.objects.get(slug='lion')
        sharik = Dog.objects.get(slug='sharik')
        self.assertEqual(str(lion.breed), 'beagle')
        self.assertEqual(str(sharik.breed), 'boxer')


class BreedTestCase(TestCase):
    nicknames_for_beagle = ('lion', 'sharik', 'archi', 'vegas', 'kasper')
    nicknames_for_boxer = ('oskar', 'rex', 'teddy', 'cesar')

    def setUp(self):
        beagle = Breed.objects.create(name='beagle', slug='beagle', description='some description')
        boxer = Breed.objects.create(name='boxer', slug='boxer', description='some description 2')

        for nickname in self.nicknames_for_beagle:
            Dog.objects.create(nickname=nickname, slug=nickname, breed=beagle)

        for nickname in self.nicknames_for_boxer:
            Dog.objects.create(nickname=nickname, slug=nickname, breed=boxer)

    def test_multiple_dogs_retrieval(self):
        beagle = Breed.objects.get(slug='beagle')
        boxer = Breed.objects.get(slug='boxer')
        self.assertEqual(beagle.dog_set.count(), 5)
        self.assertEqual(boxer.dog_set.count(), 4)

