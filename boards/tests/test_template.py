from django.test import TestCase
from django.urls import reverse

from boards.models import Board


class BoardListViewTests(TestCase):
    """It tests template list of Boards/url named home"""

    def setUp(self):
        board_objects_list = []
        for i in range(10):
            board_objects_list.append(
                Board(name=i, slug=i, description="unique objects")
            )
        Board.objects.bulk_create(objs=board_objects_list)

    def tearDown(self):
        Board.objects.all().delete()

    def test_rendering_of_home_url_provides_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "boards/list.html")

    def test_home_url_response_contains_10_objects(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(10, len(response.context.get("boards")))

    def test_home_url_with_empty_board_list(self):
        Board.objects.all().delete()
        response = self.client.get(reverse("home"))
        self.assertEquals(0, len(response.context.get("boards")))
