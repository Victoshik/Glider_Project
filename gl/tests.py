from django.contrib.auth import get_user_model
from django.test import TestCase


from .models import *


class GliderTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.note = Notes.objects.create(
            title='Shopping',
            description='Shopping list',
            person=self.user,
        )

    def test_string_representation(self):
        note = Notes(title='A sample title')
        self.assertEqual(str(note), note.title)

    def test_note_content(self):
        self.assertEqual(f'{self.note.title}', 'title')
        self.assertEqual(f'{self.note.person}', 'testuser')
        self.assertEqual(f'{self.note.description}', 'description')

    def test_note_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'description')
        self.assertTemplateUsed(response, 'index.html')

    def test_note_create_view(self):
        response = self.client.post(reverse('add_note'), {
            'title': 'New title',
            'description': 'New description',
            'person': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New description')

    def test_note_update_view(self):
        response = self.client.post(reverse('edit_note', args='1'), {
            'title': 'Updated title',
            'description': 'Updated description',
        })
        self.assertEqual(response.status_code, 302)

    def test_note_delete_view(self):
        response = self.client.note(
            reverse('delete_note', args='1'))
        self.assertEqual(response.status_code, 302)