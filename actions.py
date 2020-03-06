# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from chef_utils.utils import read_food_list, choose_random_food


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionChooseFood(Action):
	
	def name(self) -> Text:
		return "action_choose_food"

	def run(self,
			dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		food_list_path = "chef_utils/food_list.txt" # Need fix
		food_list = read_food_list(food_list_path)
		choosed_food = choose_random_food(food_list)

		dispatcher.utter_message(text=f'Món ăn hôm nay là: {choosed_food} ạ')

		return []
