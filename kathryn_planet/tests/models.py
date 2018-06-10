from django.test import TestCase
from kathryn_planet.models import Post


class ModelTestCase(TestCase):
    """This class defines the test suite for the  model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.postTitle = "Write world class code"
        self.post = Post(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Post.objects.count()
        self.bucketlist.save()
        new_count = Post.objects.count()
        self.Post(old_count, new_count)