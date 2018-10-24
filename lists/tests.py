from django.test import TestCase
from lists.models import Item

# Create your tests here.


class HomePageTest(TestCase):

    '''тест домашней страницы'''

    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        ''' тест: переадресует после запроса '''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/only_one/')


class ItemModelTest(TestCase):
    ''' тест модели элементов списка '''

    def test_saving_and_retrieving_items(self):
        ''' тест сохранения и получения элементов списка '''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second  list item'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'The second  list item')


class ListViewTest(TestCase):
    ''' тест представления списка '''

    def test_uses_list_template(self):
        ''' тест: используется шаблон списка '''
        response = self.client.get('/lists/only_one/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        ''' тест : отображаются все элементы списка '''
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/only_one/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        ''' тест: можно сохранить post-запрос '''
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirect_after_POST(self):
        ''' тест: переадресует после POST- запроса '''
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/only_one/')

