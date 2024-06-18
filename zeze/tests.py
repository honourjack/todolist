# zeze/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Task, Tag

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user)
        self.tag1 = Tag.objects.create(name='Work')
        self.tag2 = Tag.objects.create(name='Personal')
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            due_date='2024-06-30',
            status=False,
            user=self.profile
        )
        self.task.tags.add(self.tag1)

    def test_task_creation(self):
        task_count = Task.objects.count()
        self.assertEqual(task_count, 1)

    def test_task_update(self):
        updated_task = Task.objects.get(title='Test Task')
        updated_task.title = 'Updated Task'
        updated_task.save()
        self.assertEqual(updated_task.title, 'Updated Task')

    def test_task_deletion(self):
        Task.objects.get(title='Test Task').delete()
        task_count = Task.objects.count()
        self.assertEqual(task_count, 0)

    def test_tag_assignment(self):
        tags_count = self.task.tags.count()
        self.assertEqual(tags_count, 1)

    def test_task_status_update(self):
        task = Task.objects.get(title='Test Task')
        task.status = True
        task.save()
        self.assertTrue(task.status)

    def test_task_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
