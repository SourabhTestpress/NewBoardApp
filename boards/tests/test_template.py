from django.test import TestCase
from django.urls import reverse

from boards.models import Board, Topic
from django.contrib.auth.models import User


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


class TopicListViewTests(TestCase):
    """It tests template list of Topics/url named all_topics"""

    def setUp(self):
        topic_objects_list = []
        board_associated_with_topic = Board.objects.create(
            name="board", slug="boardss", description="1"
        )
        user_associated_with_topic = User.objects.create_user(
            username="sourabh", email="so@dj.com", password="Somepassword"
        )

        for i in range(10):
            topic_objects_list.append(
                Topic(
                    board=board_associated_with_topic,
                    slug=str(i),
                    user=user_associated_with_topic,
                    subject=str(i),
                )
            )
        Topic.objects.bulk_create(objs=topic_objects_list)

    def tearDown(self):
        Topic.objects.all().delete()

    def test_rendering_of_all_topics_url_provides_correct_template(self):
        response = self.client.get(reverse("all_topics"))
        self.assertTemplateUsed(response, "boards/topic_list.html")

    def test_all_topics_url_response_contains_10_objects(self):
        response = self.client.get(reverse("all_topics"))
        self.assertEquals(10, len(response.context.get("topics")))

    def test_all_topics_url_with_empty_board_list(self):
        Topic.objects.all().delete()
        response = self.client.get(reverse("all_topics"))
        self.assertEquals(0, len(response.context.get("topics")))
