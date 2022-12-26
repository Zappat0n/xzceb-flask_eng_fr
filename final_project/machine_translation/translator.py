'''This module contains the functions to translate text from English to French and vice versa.'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']
URL = os.environ['URL']

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator,
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''This function translates text from English to French.'''
    if english_text is None:
        return None

    french_text = language_translator.translate(
      text=english_text,
      model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''This function translates text from French to English.'''
    if french_text is None:
        return None

    english_text = language_translator.translate(
      text=french_text,
      model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
