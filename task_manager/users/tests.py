from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()
        user_model.objects.create_user(username='user_test1',
                                                   password='ptesttest')
        user_model.objects.create_user(username='user_test2',
                                                   password='ptesttest')

    def test_users_view(self):
        response = self.client.get('/users/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        
        content = response.content.decode()
        self.assertIn('user_test1', content)
        self.assertIn('user_test2', content)


    def test_create_view(self):
        user_create_url = '/users/create/'
        response = self.client.get(user_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')
      
        response_redirect = self.client.post(user_create_url,
                                             {"username": "user_test3",
                                              "password1": "ptesttest",
                                              "password2": "ptesttest"})

        response = self.client.get('/login/')
        content = response.content.decode()
        self.assertIn('Регистрация прошла успешно', content)
        self.assertRedirects(response_redirect, '/login/')


    def test_error_create_user(self):
    
        response = self.client.post('/users/create/', {"username": "utest3",
                                                       "password1": "ptest",
                                                       "password2": "ptest"})
        content = response.content.decode()
        self.assertIn('Некорректные данные', content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')


    def test_update_user(self):
        self.client.login(username="user_test1", password="ptesttest")
        user_id = get_user_model().objects.get(username='user_test2').id
        response_redirect = self.client.get(f'/users/{user_id}/update/')

        response = self.client.get('/users/')
        content = response.content.decode()
        self.assertIn('Отсутствуют права доступа', content)
        self.assertRedirects(response_redirect, '/users/', 302, 200)

        user_id = get_user_model().objects.get(username='user_test1').id
        response = self.client.get(f'/users/{user_id}/update/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response_redirect = self.client.post(f'/users/{user_id}/update/',
                                             {"username": "user_test11",
                                              "password1": "ptesttest",
                                              "password2": "ptesttest"})
        response = self.client.get('/users/')
        content = response.content.decode()
        self.assertIn('Пользователь успешно изменен', content)
        self.assertIn('user_test11', content)
        self.assertIn('Вход', content)
        self.assertRedirects(response_redirect, '/users/', 302, 200)

        self.client.login(username="user_test11", password="ptesttest")
        response = self.client.get(f'/users/{user_id}/update/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_delete_user(self):

        self.client.login(username="user_test1", password="ptesttest")

        user_id = get_user_model().objects.get(username='user_test2').id
        response_redirect = self.client.get(f'/users/{user_id}/delete/')
        response = self.client.get('/users/')
        content = response.content.decode()
        self.assertIn('Отсутствуют права доступа', content)
        self.assertRedirects(response_redirect, '/users/', 302, 200)
  

        user_id = get_user_model().objects.get(username='user_test1').id
        response = self.client.get(f'/users/{user_id}/delete/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        self.assertIn('user_test1', content)

        response_redirect = self.client.post(f'/users/{user_id}/delete/')
        response = self.client.get('/users/')
        content = response.content.decode()
        self.assertIn('Пользователь успешно удален', content)
        self.assertNotIn('user_test1', content)
        self.assertIn('Вход', content)
        self.assertRedirects(response_redirect, '/users/', 302, 200)