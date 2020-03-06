import random
from typing import Text, List


def read_food_list(file_path: Text) -> List:
	with open(file_path, 'r') as f:
		raw_food_list = f.readlines()

	return list(map(_remove_newline_in_string, raw_food_list))


def choose_random_food(food_list: List) -> Text:
	choosed_food = random.choice(food_list)

	return choosed_food


def _remove_newline_in_string(string: Text) -> Text:
	string_container = list()
	for char in string:
		string_container.append(char)

	new_string_container = string_container[:-1]

	return ''.join(new_string_container)


if __name__ == '__main__':

	print("########### TESTING ##########")
	r = read_food_list('food_list.txt')

	import pdb; pdb.set_trace()
