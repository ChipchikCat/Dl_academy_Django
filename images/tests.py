from django.test import TestCase
from django.core.files import File
from .models import Image


# Create your tests here.

class ImagesModelTest(TestCase):

    def test_images_save_and_retrive(self):
        image1 = Image(
            title="image 1",
            image = File(open("images/test_images/test1.png", "rb")),
        )
        image1.save()

        image2 = Image(
            title="image 2",
            image = File(open("images/test_images/test2.png", "rb")),
        )
        image2.save()

        all_images = Image.objects.all()

        self.assertEqual(len(all_images), 2)

        self.assertEqual(all_images[0].title, image1.title)

        self.assertEqual(all_images[0].image, image1.image)

        self.assertEqual(all_images[1].title, image2.title)

        self.assertEqual(all_images[1].image, image2.image)