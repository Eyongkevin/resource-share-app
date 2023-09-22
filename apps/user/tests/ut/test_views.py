from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from apps.user import views
from apps.user import models


class TestUserView(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        # TODO: CREATE A USER
        self.user = models.User.objects.create_user(
            username="kenz",
            password="test@2023password",
            first_name="tony",
            last_name="ralph",
            email="tonyralph@gmail.com",
            bio="Good at anything Python",
            title="Python Developer",
        )

    def test_profile_redirect_for_non_auth_user(self):
        url = reverse("profile")
        request = self.factory.get(url)
        request.user = AnonymousUser()  # non-authenticated user

        response = views.profile(request)

        self.assertEqual(response.status_code, 302)

    def test_profile_ok_for_auth_user(self):
        url = reverse("profile")
        request = self.factory.get(url)
        request.user = self.user

        response = views.profile(request)

        self.assertEqual(response.status_code, 200)
