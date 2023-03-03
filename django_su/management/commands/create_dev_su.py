from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()

DJANGO_SU_USERNAME_FIELD = getattr(
    settings,
    "DJANGO_SU_USERNAME_FIELD",
    User.USERNAME_FIELD,
)
DJANGO_SU_USERNAME = getattr(settings, "DJANGO_SU_USERNAME", "admin")
DJANGO_SU_PASSWORD = getattr(settings, "DJANGO_SU_PASSWORD", "admin")
DJANGO_SU_EXTRA_ARGS = getattr(settings, "DJANGO_SU_EXTRA_ARGS", {})


class Command(BaseCommand):
    help = "Create a SuperUser"

    def create_superuser(self):
        User.objects.create_superuser(
            DJANGO_SU_USERNAME,
            password=DJANGO_SU_PASSWORD,
            **DJANGO_SU_EXTRA_ARGS,
        )

    def handle(self, *args, **options):
        filter_args = {
            f"{DJANGO_SU_USERNAME_FIELD}__iexact": DJANGO_SU_USERNAME.lower(),
        }
        exists = User.objects.filter(**filter_args).exists()
        if not exists:
            self.create_superuser()
            self.stdout.write(
                self.style.SUCCESS(
                    f"SuperUser created with \n"
                    f"\t{DJANGO_SU_USERNAME_FIELD}: {DJANGO_SU_USERNAME}\n"
                    f"\tPassword: {DJANGO_SU_PASSWORD}",
                ),
            )
