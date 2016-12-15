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
The above example see's a user translating a sentence
