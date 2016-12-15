import requests
import json

class yantranslator(object):

    def __init__(self,api_key):
        self.api_key = api_key

    def supported_langs(self,ui_lang='en'):
        url = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs?key='
        user_lang = ui_lang
        r = requests.get('{}{}&'.format(url,self.api_key,user_lang))
        data = json.loads(r.text)
        lang_pairs = data['dirs'][0:]
        return lang_pairs

    def indentify_language(self,text,hint=''):
        url = 'https://translate.yandex.net/api/v1.5/tr.json/detect?key='
        text = '&text={}'.format(text)
        if hint == '':
            r = requests.get('{}{}{}'.format(url,self.api_key,text))
            data = json.loads(r.text)
            language = data['lang'][0:]
            return language
        else:
            hint = '&hint={}'.format(hint)
            r = requests.get('{}{}{}{}'.format(url,self.api_key,text,hint))
            data = json.loads(r.text)
            language = data['lang'][0:]
            return language

    def tran_sentence(self,from_lang,to_lang,sentence,formatting='plain'):
        language_pairing = '&lang={}-{}'.format(from_lang,to_lang)
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='
        text = '&text={}'.format(sentence)
        formatting = '&fomat={}'.format(formatting)
        r = requests.get('{}{}{}{}{}'.format(url,self.api_key,language_pairing,text,formatting))
        data = json.loads(r.text)
        result = data['text'][0:]
        result = ''.join(result)
        return result

    def auto_tran(self,to_lang,sentence,formatting='plain'):
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='
        language = '&lang={}'.format(to_lang)
        options = '&option=1'
        text = '&text={}'.format(sentence)
        r = requests.get('{}{}{}{}{}'.format(url,self.api_key,text,language,options))
        data = json.loads(r.text)
        result = data['text'][0:]
        result = ''.join(result)
        return result
