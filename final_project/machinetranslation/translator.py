import json
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

def englishToFrench(englishText):
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return englishToFrench.get("tranlation"[0].get("tranlation"))



def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='fr-en').get_result()
    return englishToFrench.get("tranlation"[0].get("tranlation"))

