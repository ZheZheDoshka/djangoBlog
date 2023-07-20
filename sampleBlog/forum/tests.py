from django.test import TestCase

from forum.models import *


class TopicTestCase(TestCase):
    def setUp(self):

        number_of_posts = 10
        Category.objects.create(category_name="test", category_description="test", slug="test")
        SubCategory.objects.create(subcategory_name="subtest", subcategory_description="subtest",
                                   slug = "subtest", category=Category.objects.get(category_name="test"))
        Topic.objects.create(title="test_topic", text="test_topic",
                             subcategory=SubCategory.objects.get(subcategory_name="subtest"),
                             user=None)
        Post.objects.bulk_create([Post(text=str(i), topic=Topic.objects.get(title="test_topic"), user=None) for i in range(number_of_posts)])

    def testLastPageNumber(self):
        number_of_posts = 10
        topic = Topic.objects.get(title="test_topic")
        self.assertEqual(number_of_posts, topic.get_post_number())

    """test for checking whether the link forms correctly"""
    def testUrl(self):
        topic = Topic.objects.get(title="test_topic")
        expected_url = "forum/test/subtest/1?page=1"
        self.assertEqual(expected_url, topic.get_url())


