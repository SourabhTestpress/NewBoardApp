from django.urls import resolve, reverse
from django.test import SimpleTestCase, TestCase, RequestFactory

from boards.views import board_list, topic_list, board_detail
from boards.models import Board


class BoardListViewTests(SimpleTestCase):
    """It tests list of Boards"""

    def test_home_url_is_referencing_to_correct_associated_function(self):
        view = resolve("/")
        self.assertEquals(view.func, board_list)


class BoardListViewTestsInvolvingDatabase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view_produces_status_code_200(self):
        request = self.factory.get("/")
        response = board_list(request)
        self.assertEquals(200, response.status_code)


class TopicListViewTests(SimpleTestCase):
    """It tests list of Topics"""

    def test_all_topics_url_is_referencing_to_correct_associated_function(self):
        view = resolve("/all-topics/")
        self.assertEquals(view.func, topic_list)


class TopicListViewTestsInvolvingDatabase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_topic_list_view_produces_status_code_200(self):
        request = self.factory.get(reverse("all_topics"))
        response = board_list(request)
        self.assertEquals(200, response.status_code)


class BoardDetailView(TestCase):
    """ It tests the views of BoardDetailView"""

    def setUp(self):
        self.board_obj = Board.objects.create(
            name="1st", slug="slug-of-board1", description="board_obj"
        )
        self.factory = RequestFactory()

    def test_board_detail_is_refrencing_to_correct_associated_function(self):
        view = resolve("/slug_of_board1/")
        self.assertEquals(view.func, board_detail)

    def test_board_detail_view_produces_status_code_200(self):
        response = self.client.get(reverse("detail", args=(self.board_obj.slug,)))
        self.assertEquals(200, response.status_code)
