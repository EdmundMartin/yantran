# yantran
## What is Yantran?
Yantran is a Python 3 wrapper for Yandex's translate API. Yantran sits on top of the Yandex API and makes the Yandex Translate API simpler to use. 
## Example Usage
### Indentify a Language
```python
from yantran import yantranslator

translator = yantranslator('SUPER_SECRET_API_KEY')
what_language = translator.indentify_language('Привет всем, меня зовут Эдмунд')
print(what_language)
>> ru
```
The Yandex Translate API allows users to indentify a language with users simply having to provide a piece of text for Yandex to check. The above example outputs the indentified langauge according to Yandex's API. 

It is also possible to provide Yandex with hints regarding the inputted language. Yantran supports this functionality and the example below outlines how this is done using Yantran.
```python
from yantran import yantranslator

translator = yantranslator('SUPER_SECRET_API_KEY')
what_language = translator.indentify_language('Привет всем, меня зовут Эдмунд','en,ru,uk,kz')
print(what_language)
>> ru
```
In the above example the user has included four 'hint languages'. Yantran returns the most likely language as a string.
### Translating a sentence
```python
from yantran import yantranslator

translator = yantranslator('SUPER_SECRET_API_KEY')
what_does_this_mean = translator.tran_sentence('ru','en','Почему ты смотришь на меня?')
print(what_does_this_mean)
>> Why are you looking at me?
```
The above example see's a user translating a sentence from a known language into another known language. Providing the source language 'ru' - Russian and the target language 'en' - English, plus the sentence to be translated. Yantran returns the result as a string.

Additionally, Yantran supports html input - allowing users to translate content contained within HTML. This is down by changing the optional argument to 'html' as outlined in the example below.
```python
from yantran import yantranslator

translator = yantranslator('SUPER_SECRET_API_KEY')
what_does_this_mean = translator.tran_sentence('ru','en','<h1>Почему ты смотришь на меня?</h1>','html')
print(what_does_this_mean)
>> <h1>Why are you looking at me?</h1>
```
### Automatic Translation of a sentence
```python
from yantran import yantranslator

translator = yantranslator('SUPER_SECRET_API_KEY')
what_does_this_mean = translator.auto_tran('en','Почему ты смотришь на меня?')
print(what_does_this_mean)
>> Why are you looking at me?
```
Yantran also supports automatic translation of sentences. The function takes target langauge and the sentence as required variables - and returns Yandex's translation of the given sentence. The arguement also takes the optional formatting argument - allowing you to specify whether the sentence is HTML or plain text.

### List of Supported Language Pairings
Yantran also allows users to check all the pairings which are currently supported by Yandex Translate. This function returns a list. An example usage can be found below.
```python
from yantran import yantranslator

translator = yantranslator('SUPER_SECRET_API_KEY')
what_can_this_translate = translator.supported_langs()
for language_pairing in what_can_this_translate:
    if 'ru' in language_pairing:
        print(language_pairing)
>> az-ru
>> be-ru
>> bg-ru
>> etc....
```

### Why Yandex?
Google charges people to use Translate API, it is increadibly cheap working out at about $0.05 per page of text. But what's better than very cheap - FREE. Yandex's Translation API is absolutely free to use, provided a link and statement saying that your product is powered by the Yandex Translate API. You can find out more and get your free Yandex API key [here](https://tech.yandex.com/translate/).

Additionally, the Yandex translate service is superior across a decent number of language pairs. Languages such as Russian, Ukrainian and Belarusian are much better supported by Yandex. 
