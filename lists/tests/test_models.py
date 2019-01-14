from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError
# Create your tests here.

class ItemModelTest(TestCase):
    ''' тест модели элементов списка '''

    def test_cannot_save_empty_items(self):
        ''' тест: нельзя добавлять пустые элементы списка '''
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_duplicate_items_are_invalid(self):
        '''тест: повторы элементов недопустимы '''
        list_ =  List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()
            #item.save()

    def tetst_CAN_save_same_item_to_different_lists(self):
        list1 = List.object.create()
        list2 = List.object.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean() #не должен поднять исключение
    
    def test_list_ordering(self):
        ''' тест упорядочения списка '''
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
                list(Item.objects.all()),
                [item1, item2, item3]
                )
            
    def test_string_representation(self):
        ''' тест строкового представления '''
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')

    def test_default_text(self):
        '''тест заданного по умолчанию текста '''
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        '''тест: элемент связан со списком '''
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())


class ListModelTest(TestCase):
    ''' тест модели списка '''
    
    def test_get_absolute_url(self):
        ''' тест: получен абсолютный url '''
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')


