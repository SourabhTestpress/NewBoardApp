from django.urls import resolve, reverse
from django.test import SimpleTestCase, TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User

from boards.views import board_list, topic_list, board_detail, CreateTopicView
from boards.models import Board, Topic, Post


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
        request = self.factory.get(reverse("detail", args=(self.board_obj.slug,)))
        response = board_detail(request, self.board_obj.slug)
        self.assertEquals(200, response.status_code)


class AddNewTopicTest(TestCase):
    def setUp(self):
        self.board_obj = Board.objects.create(
            name="board", slug="boarddslug", description="1"
        )
        self.user = User.objects.create_user(
            username="sourabh", email="so@dj.com", password="Somepassword"
        )
        self.factory = RequestFactory()

    def test_csrf_token_is_present_in_get_request_to_create_topic_view(self):
        kwargs = {"slug": self.board_obj.slug}
        request = self.factory.get(reverse("new_topic", args=(self.board_obj.slug,)))
        request.user = self.user
        response = CreateTopicView.as_view()(request, **kwargs)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_create_topic_view_redirects_on_valid_post_data(self):
        kwargs = {"slug": self.board_obj.slug}
        url = reverse("new_topic", args=(self.board_obj.slug,))
        data = {
            "subject": "Test title",
            "message": "Lorem ipsum dolor sit amet",
            "board": self.board_obj.id,
            "user": self.user.id,
        }
        request = self.factory.post(url, data)
        request.user = self.user
        response = CreateTopicView.as_view()(request, **kwargs)
        self.assertEquals(302, response.status_code)

    def test_should_create_topic_with_valid_post_data(self):
        kwargs = {"slug": self.board_obj.slug}
        url = reverse("new_topic", args=(self.board_obj.slug,))
        data = {
            "subject": "Test title",
            "message": "Lorem ipsum dolor sit amet",
            "board": self.board_obj.id,
            "user": self.user.id,
        }
        request = self.factory.post(url, data)
        request.user = self.user
        response = CreateTopicView.as_view()(request, **kwargs)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())
