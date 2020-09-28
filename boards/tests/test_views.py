from django.urls import resolve
from django.test import SimpleTestCase, TestCase, RequestFactory

from boards.views import board_list


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
