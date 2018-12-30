from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError
# Create your tests here.




class ListAndItemModelTest(TestCase):
    ''' тест модели элементов списка '''

    def test_saving_and_retrieving_items(self):
        ''' тест сохранения и получения элементов списка '''

        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'The second  list item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEquals(saved_list, list_)

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(), 2)

        first_saved_item = saved_item[0]
        second_saved_item = saved_item[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'The second  list item')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_items(self):
        ''' тест: нельзя добавлять пустые элементы списка '''
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
    def test_get_absolute_url(self):
        ''' тест: получен абсолютный url '''
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')


