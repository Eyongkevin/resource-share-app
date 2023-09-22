from django.test import TestCase

from apps.user.templatetags import custom_filter


class TestCustomFilterTemplateTags(TestCase):
    def test_cap_all_but_upper_first_admin_value_all_upper(self):
        value = "admin"

        result = custom_filter.cap_all_but_upper_first(value)

        self.assertEqual(result, "ADMIN")

    def test_cap_all_but_upper_first_any_other_value_capitalize(self):
        value = "kevin"

        result = custom_filter.cap_all_but_upper_first(value)

        self.assertEqual(result, "Kevin")
