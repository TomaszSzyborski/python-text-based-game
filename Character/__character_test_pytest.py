#todo implement pytest tests
# import random
# import string
# import pytest
#
# from Character.character import Character
# from Constans.constans import *
#
#
# @pytest.fixture(scope="function", autouse=True)
#
# def random_name():
#     yield ''.join(random.choice(string.ascii_letters) for _ in range(10))
#
#
# @pytest.fixture(autouse=True)
# def attrs():
#     yield {
#         STRENGTH: random.randint(1, 21),
#         DEXTERITY: random.randint(1, 21),
#         VITALITY: random.randint(1, 21),
#         MAGIC: random.randint(1, 21),
#         PERCEPTION: random.randint(1, 21)
#     }
#
#
# #
# # def test_character_name_all_lower_case(self):
# #     lower_name = self.random_name.lower()
# #     character = Character(lower_name,
# #                           self.attrs, WARRIOR)
# #
# #     with self.assertRaises(AssertionError):
# #         self.assertEqual(character.name, lower_name)
# #
# # def test_character_name_all_upper_case(self):
# #     upper_name = self.random_name.upper()
# #     character = Character(upper_name,
# #                           self.attrs, WARRIOR)
# #
# #     with self.assertRaises(AssertionError):
# #         self.assertEqual(character.name, upper_name)
# #
# # def test_character_name_random_case(self):
# #     character = Character(self.random_name,
# #                           self.attrs, WARRIOR)
# #
# #     with self.assertRaises(AssertionError):
# #         self.assertEqual(character.name, self.random_name)
#
#
