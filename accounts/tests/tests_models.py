from django.test import TestCase
from accounts.models import User

class TestModelsAccount(TestCase):    

    def test_create_user(self):
        user = User.objects.create(username='ruan', email='ruan@gmail.com',
        phone='99999999999'
        )
        self.assertEqual(user.username, 'ruan')
        self.assertEqual(user.email, 'ruan@gmail.com')
        self.assertEqual(user.phone, '99999999999')
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)
        self.assert_( not user.is_superuser)

    def test_super_user(self):
        super_user = User.objects.create_superuser(username='admin', email='admin@gmail.com',
        phone='99999999999'
        )

        self.assertEqual(super_user.username, 'admin')
        self.assertEqual(super_user.email, 'admin@gmail.com')
        self.assertEqual(super_user.phone, '99999999999')
        self.assertEqual(super_user.is_staff, True)
        self.assertEqual(super_user.is_active, True)
        self.assert_(super_user.is_superuser)


