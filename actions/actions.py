# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from rasa_sdk.events import SlotSet
import random
#
class ActionGejala(Action):

    def name(self) -> Text:
        return "action_gejala"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        data_penyakit = pd.read_csv('Book1.csv', delimiter=';')
        penyakit = tracker.get_slot('penyakit')
        get_penyakit = data_penyakit[data_penyakit['penyakit']== penyakit]
        if len(get_penyakit) == 0:
            dispatcher.utter_message(text='penyakit {} belum terdaftar dalam pengetahuan kami'.format(penyakit))
        else:
            gejala = get_penyakit['gejala']
            dispatcher.utter_message(text='penyakit {} gejalanya adalah {}'.format(penyakit, gejala))

        return [SlotSet('gejala', gejala)]

class ActionFeedback(Action):

    def name(self) -> Text:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # if tracker.latest_message['intent'].get('name') == 'feedback' :
        feedback = tracker.latest_message.text
        csv_file = open("feedback.csv", "w")
        csv_file.write(feedback)
        csv_file.close()
        dispatcher.utter_message(text="Feedback telah tersimpan")

        return []

class ActionPenyakit(Action):

    def name(self) -> Text:
        return "action_penyakit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        data_penyakit = pd.read_csv('Book1.csv', delimiter=';')
        gejala = tracker.get_slot('gejala')

        for i in range(len(data_penyakit['gejala'])):
            if gejala in data_penyakit['gejala'][i]:
                penyakit = data_penyakit['penyakit'][i]
                break

        dispatcher.utter_message(text="anda kemungkinan terkena penyakit {}".format(penyakit))

        return [SlotSet('penyakit', penyakit)]

class ActionObatFromPenyakit(Action):

    def name(self) -> Text:
        return "action_obat_from_penyakit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        data_penyakit = pd.read_csv('Book1.csv' , delimiter=';')
        penyakit = tracker.get_slot('penyakit')
        if penyakit in data_penyakit['penyakit']:
            for i in range(len(data_penyakit['penyakit'])):
                if data_penyakit['penyakit'][i] == penyakit:
                    obat = data_penyakit['obat'][i]
            dispatcher.utter_message(text="penyakit {} dapat diobat dengan {}".format(penyakit, obat))
        else:
            dispatcher.utter_message(text="kami tidak memiliki pengetahuan tentang penyakit tersebut")

        return [SlotSet('pengobatan', obat)]

class ActionAdviceFromPenyakit(Action):

    def name(self) -> Text:
        return "action_advice_from_penyakit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        data_penyakit = pd.read_csv('Book1.csv' , delimiter=';')
        penyakit = tracker.get_slot('penyakit')
        if penyakit in data_penyakit['penyakit']:
            for i in range(len(data_penyakit['penyakit'])):
                if data_penyakit['penyakit'][i] == penyakit:
                    advice = data_penyakit['advice'][i]
            dispatcher.utter_message(text="bagi penderita {} disarankan untuk {}".format(penyakit, obat))
        else:
            dispatcher.utter_message(text="kami tidak memiliki pengetahuan tentang penyakit tersebut")
        return [SlotSet('advice', advice)]

class ActionHealDepresi(Action):

    def name(self) -> Text:
        return "action_heal_depresi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        data_depresi = pd.read_csv('actionDepression.csv')
        i_take = random.randint(len(data_depresi))
        
        dispatcher.utter_message(text=data_depresi['actionDepression'][i_take])
        return []

class ActionHealAnxiety(Action):

    def name(self) -> Text:
        return "action_heal_anxiety"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        data_anxiety = pd.read_csv('actionAnxiety.csv')
        i_take = random.randint(len(data_anxiety))
        
        dispatcher.utter_message(text=data_anxiety['actionAnxiey'][i_take])
        return []
        
class ActionHealParenting(Action):

    def name(self) -> Text:
        return "action_heal_parenting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        data_parenting = pd.read_csv('actionParenting.csv')
        i_take = random.randint(len(data_parenting))
        
        dispatcher.utter_message(text=data_parenting['actionParenting'][i_take])
        return []

class ActionHealRelationship(Action):

    def name(self) -> Text:
        return "action_heal_relationship"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        data_relation = pd.read_csv('actionRelationship.csv')
        i_take = random.randint(len(data_relation))
        
        dispatcher.utter_message(text=data_relation['actionRelationship'][i_take])
        return []
