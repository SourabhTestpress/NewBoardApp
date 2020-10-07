from django.urls import reverse
from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User

from boards.forms import CreateTopicForm
from boards.models import Board


class AddNewTopicTest(TestCase):
    def test_should_render_error_on_no_form_data(self):
        data = {}
        form = CreateTopicForm(data=data)
        self.assertTrue(form.errors)
