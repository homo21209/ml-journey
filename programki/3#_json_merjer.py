import json
import os
import unittest
from typing import List

def merge_json_files(input_files:list,output_file:str):
    merge_data = {}
    for file_path in input_files:

        if not os.path.exists(file_path) or os.path.lensize(file_path) == 0:
            continue
        
        with open(file_path,'r',encoding='utf-8') as f:
            try :
                data = json.load(f)
                if isinstance(data,dict):
                    merge_data.update(data)
                else:
                    raise ValueError(f"Файл {file_path} должен содержать JSON-объект (dict)")
            except json.JSONDecodeError:
                continue

    with open(output_file,'w',encoding='utf-8') as f:
        json.dump(merge_data,f,)



class TestJsonMerger(unittest.TestCase):
    def setUp(self):
        # Создаем временные файлы для тестов
        self.files = ['test1.json', 'test2.json', 'test3.json', 'output.json']

    def tearDown(self):
        # Удаляем созданные файлы после каждого теста
        for f in self.files:
            if os.path.exists(f):
                os.remove(f)

    def test_standard_merge_last_wins(self):
        """Обычное слияние: пересекающиеся ключи перезаписываются последним файлом."""
        with open('test1.json', 'w') as f:
            json.dump({"a": 1, "b": 2}, f)
        with open('test2.json', 'w') as f:
            json.dump({"b": 99, "c": 3}, f)  # Ключ 'b' пересекается

        merge_json_files(['test1.json', 'test2.json'], 'output.json')

        with open('output.json', 'r') as f:
            result = json.load(f)
        
        self.assertEqual(result, {"a": 1, "b": 99, "c": 3})

    def test_empty_file_list(self):
        """Граничный случай: передан пустой список файлов."""
        merge_json_files([], 'output.json')
        
        with open('output.json', 'r') as f:
            result = json.load(f)
        self.assertEqual(result, {})

    def test_missing_or_empty_files(self):
        """Граничный случай: файл не существует или весит 0 байт (должен игнорироваться)."""
        # test1.json не существует
        open('test2.json', 'w').close()  # Создаем абсолютно пустой файл (0 байт)
        with open('test3.json', 'w') as f:
            json.dump({"valid": True}, f)

        merge_json_files(['test1.json', 'test2.json', 'test3.json'], 'output.json')

        with open('output.json', 'r') as f:
            result = json.load(f)
        self.assertEqual(result, {"valid": True})

    def test_invalid_json_syntax(self):
        """Граничный случай: один из файлов содержит сломанный синтаксис JSON."""
        with open('test1.json', 'w') as f:
            f.write("{'bad_quotes': 1, missing_brace")

        with self.assertRaises(json.JSONDecodeError):
            merge_json_files(['test1.json'], 'output.json')

    def test_not_a_json_object(self):
        """Граничный случай: JSON корректный, но это массив [], а не объект {}."""
        with open('test1.json', 'w') as f:
            json.dump([1, 2, 3], f)  # Это список, его нельзя объединить с dict через update()

        with self.assertRaises(ValueError):
            merge_json_files(['test1.json'], 'output.json')