from io import StringIO
from unittest.mock import call, patch

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase

from django_su import conf


class TestCreateDevSu(TestCase):
    @property
    def User(self):
        return get_user_model()

    def test_creates_superuser(self):
        call_command("create_dev_su")
        user = self.User.objects.get(**{conf.USERNAME_FIELD: conf.USERNAME})
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.check_password(conf.PASSWORD))

    def test_idempotent(self):
        # Running the command twice must not create a second user.
        call_command("create_dev_su")
        call_command("create_dev_su")
        self.assertEqual(self.User.objects.count(), 1)

    def test_success_output(self):
        out = StringIO()
        call_command("create_dev_su", stdout=out)
        output = out.getvalue()
        self.assertIn(conf.USERNAME, output)
        self.assertIn(conf.PASSWORD, output)

    def test_duplicate_prints_warning(self):
        call_command("create_dev_su")
        out = StringIO()
        call_command("create_dev_su", stdout=out)
        self.assertIn("already exists", out.getvalue())

    def test_case_insensitive_duplicate_check(self):
        # The duplicate filter uses __iexact, so an existing user whose
        # username differs only in case should still block creation.
        self.User.objects.create_superuser(conf.USERNAME.upper(), password="test")
        out = StringIO()
        call_command("create_dev_su", stdout=out)
        self.assertIn("already exists", out.getvalue())
        self.assertEqual(self.User.objects.count(), 1)

    @patch.object(conf, "USERNAME", "customuser")
    @patch.object(conf, "PASSWORD", "custompass")
    def test_custom_config(self):
        call_command("create_dev_su")
        user = self.User.objects.get(**{conf.USERNAME_FIELD: "customuser"})
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password("custompass"))


class TestUtilRestore(TestCase):
    def test_calls_commands_in_order(self):
        with patch(
            "django_su.management.commands.util_restore.call_command",
        ) as mock_cc:
            call_command("util_restore")
            self.assertEqual(
                mock_cc.call_args_list,
                [
                    call("reset_db", "--noinput"),
                    call("migrate"),
                    call("create_dev_su"),
                ],
            )

    def test_success_output(self):
        with patch("django_su.management.commands.util_restore.call_command"):
            out = StringIO()
            call_command("util_restore", stdout=out)
            self.assertIn("Restore Completed", out.getvalue())
