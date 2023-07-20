from django.test import TestCase

from forum.models import *


class TopicTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category_name="test", category_description="test", slug="test")
        SubCategory.objects.create(subcategory_name="subtest", subcategory_description="subtest",
                                   slug = "subtest", category=Category.objects.get(category_name="test"))
        Topic.objects.create(title="test_topic", text="test_topic",
                             subcategory=SubCategory.objects.get(subcategory_name="subtest"),
                             user=None)

    def testUrl(self):
        topic = Topic.objects.get(title="test_topic")
        expected_url = "forum/test/subtest/1?page=0"
        self.assertEqual(expected_url, topic.get_url())


