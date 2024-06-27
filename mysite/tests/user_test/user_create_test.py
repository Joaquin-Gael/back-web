from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from users.models import TypeUser, Visit, WeeklyVisit

class UserModelTestCase(TestCase):
    def setUp(self):
        self.type_user = TypeUser.objects.create(type_user='admin')
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            type_user=self.type_user
        )
        self.visit = Visit.objects.create(
            ip_addres='127.0.0.1',
            user_agent='Mozilla/5.0',
        )
        self.weekly_visit = WeeklyVisit.objects.create(
            week_start=timezone.now().date(),
            week_end=timezone.now().date(),
            visit_count=10
        )

    def test_user_creation(self):
        user_count = get_user_model().objects.count()
        self.assertEqual(user_count, 1)

    def test_visit_creation(self):
        visit_count = Visit.objects.count()
        self.assertEqual(visit_count, 1)

    def test_weekly_visit_creation(self):
        weekly_visit_count = WeeklyVisit.objects.count()
        self.assertEqual(weekly_visit_count, 1)

    def test_user_type(self):
        self.assertEqual(self.user.type_user.type_user, 'admin')

    def test_user_string_representation(self):
        expected_str = f'''
            {self.user.username},
            {self.user.email},
            {self.user.is_active},
            {self.user.date_joined},
            {self.user.last_login},
            {self.user.last_logout},
            {self.user.type_user}
        '''
        self.assertEqual(str(self.user), expected_str)



