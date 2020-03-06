## Just only order food
* greet
 - utter_can_i_help_you
* choose_food
 - action_choose_food
* say_thanks
 - utter_say_no_problem
* say_bye
 - utter_say_bye

## user say hungry
* say_hungry
 - utter_say_good_thing
> ask_user_choose_food

## user accept choose food
> ask_user_choose_food
* say_ok
 - utter_say_ok_choose_food
 - action_choose_food
* say_thanks
 - utter_say_no_problem
* say_bye
 - utter_say_bye

## user deny choose food
> ask_user_choose_food
* say_no_choose_food
 - utter_say_next
* say_no
 - utter_say_bye

## user greet + ask mission + name
* greet
 - utter_say_hi
* ask_mission
 - utter_say_answer_mission
* ask_name
 - utter_say_name
* say_bye
 - utter_say_bye
