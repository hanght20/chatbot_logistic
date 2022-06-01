from typing import Any, Text, Dict, List

from rasa_sdk.executor import CollectingDispatcher
import re
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict


class ValidateCustomerForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_customer_form"

    def validate_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `phone` value."""
        value = tracker.get_slot("phone")
        print(f"Phone number = {slot_value} length = {len(slot_value)}")
        if re.search(r"(^(84|0[3|5|7|8|9])+([0-9]{8})\b)", slot_value):
            if len(value) < 10 or len(value) > 10:
                dispatcher.utter_message(text="valid")
                return{"phone": value}
            else:
                print("nfhhf")
        else:
            dispatcher.utter_message(
                text=f"Số điện thoại không đúng! Mời bạn nhập lại!")
            return {"phone": None}

        return {"phone": slot_value}

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `email` value."""
        value = tracker.get_slot("email")
        if re.search(r"(^[a-z][a-z0-9_\.]+@[a-z0-9]+(\.[a-z0-9]{2,4}){1,2}$)", value):
            print("print id")
            return{"email": value}
        else:
            dispatcher.utter_message(
                text="Email không đúng. Mời bạn nhập lại!")
            return {"email": None}
