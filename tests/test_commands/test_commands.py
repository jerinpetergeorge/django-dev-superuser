from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase

from django_su import conf


class TestCommands(TestCase):
    @property
    def user_model_cls(self):
        return get_user_model()

    def test_create_default(self):
        call_command("create_dev_su")
        user = self.user_model_cls.objects.first()
        self.assertEqual(user.username, conf.USERNAME)
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.check_password(conf.PASSWORD), True)
