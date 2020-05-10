from django.test import TestCase
from django.urls import reverse
from home.models import Contact



class HomePageTests(TestCase):

    def test_home_get(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)

class AboutPageTests(TestCase):

    def test_about_get(self):
        response = self.client.get(reverse("about"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<form")

    def test_contact_form_valid(self):
        response = self.client.post(reverse("about"), {
            "name": "TestName",
            "email": "test@email.com",
            "message": "Test message"
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "SENT :)")

        self.assertEqual(Contact.objects.count(), 1)

    def test_email_invalid(self):
        response = self.client.post(reverse("about"), {
            "name": "TestName",
            "email": "bademail",
            "message": "Test message"
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")

        self.assertEqual(Contact.objects.count(), 0)


    def test_email_empty(self):
        response = self.client.post(reverse("about"), {
            "name": "TestName",
            "email": "",
            "message": "Test message"
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertEqual(Contact.objects.count(), 0)


    def test_name_empty(self):
        response = self.client.post(reverse("about"), {
            "name": "",
            "email": "test@email.com",
            "message": "Test message"
        })
        self.assertEquals(response.status_code, 200)
        # self.assertContains(response, "This field is required.")
        self.assertEqual(Contact.objects.count(), 0)


    def test_message_empty(self):
        response = self.client.post(reverse("about"), {
            "name": "TestName",
            "email": "test@email.com",
            "message": ""
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertEqual(Contact.objects.count(), 0)




