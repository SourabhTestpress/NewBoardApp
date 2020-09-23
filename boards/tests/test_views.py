from django.urls import reverse
from django.urls import resolve
from django.test import TestCase

# imports from this folder
from ..views import board_list


class HomepageTests(TestCase):
    """It tests list of Boards"""

    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(
            response.status_code,
            200,
            "Expected Homepage View to have 200 got {}".format(response.status_code),
        )

    def test_correct_view_function_running(self):
        view = resolve("/")
        self.assertEquals(view.func, board_list)
