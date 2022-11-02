from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from catatbund.models import CatatbundModel
import datetime

# Create your tests here.
class TestingViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="spongebob", email="sponge@dummy.com", password="patrickstar")
        group = Group.objects.create(name="bumil")
        self.user.groups.add(group)
        self.user.save()
        self.catatbund = CatatbundModel.objects.create(
            user = self.user,
            date = '2022-11-12',
            weight  = 22,
            height  = 1.2,
            bmi = 22 / (1.2*1.2)
        )
        self.client = Client()
        self.catatbund_html = reverse('catatbund:show_catatbund')
        self.catatbund_json = reverse('catatbund:show_json')

    def test_show_catatbund_html(self):
        self.client.login(username='spongebob', password='patrickstar')
        response = self.client.get(self.catatbund_html)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catatbund.html')

    def test_show_catatbund_json(self):
        response = self.client.get(self.catatbund_json)
        self.assertEqual(response.status_code, 200)