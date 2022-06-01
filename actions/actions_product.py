from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.api.product_price import get_product_price


class ActionProductDefinition(Action):

    def name(self) -> Text:
        return "action_product_define"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            name = tracker.get_slot("product")
            print(name)

            if name is not None:
                print(get_product_price(
                    name, "definition"))
                dispatcher.utter_message(
                    text=get_product_price(name, "definition"))
            else:
                dispatcher.utter_message(
                     text="Xin lỗi tôi không hiểu, {call_name} muốn hỏi thông tin về loại mặt hàng nào?")
        except Exception as e:
            print(str(e))
        return []


class ActionPrice(Action):

    def name(self) -> Text:
        return "action_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            name = tracker.get_slot("product")
            print(name)
            if name is not None:
                print(get_product_price(
                    name, "price"))
                dispatcher.utter_message(
                    text=get_product_price(name, "price"))
            else:
                
                dispatcher.utter_message(
                    text="Xin lỗi tôi không hiểu, {call_name} muốn hỏi giá vận chuyển mặt hàng nào?")
        except Exception as e:
            print(str(e))
        return []
