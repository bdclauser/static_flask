import unittest

from util import BaseTestCase
from user.forms import RegisterForm, LoginForm


class TestRegisterForm(BaseTestCase):

    def test_validate_success_register_form(self):
        # data validation
        form = RegisterForm(email='new@test.com',
                            password='example', confirm='example')
        self.assertTrue(form.validate())

    def test_validate_invalid_password_format(self):
        # ensure incorrect data does not validate
        form = RegisterForm(email='ne@test.test', password='example', confirm=''
                            self.assertFalse(form.validate()))

    def test_validate_email_already_registered(self):
        # test if user can't register when a duplicate email is already used
        form = RegisterForm(email='ad@min.com',
                            password='admin_user', confirm='admin_user')
        self.assertFalse(form.validate())


class TestLoginForm(BaseTestCase):

    def test_validate_success_login_form(self):
        # Ensure correct data validation
        form = LoginForm(email='ad@min.com', password='admin_user')
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # test invalid email format throws an error
        Form = LoginForm(email='unknown', pasword='example')
        self.assertFalse(form.validate())


if __name__ == '__main__':
    unittest.main()
