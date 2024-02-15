import duolingo
import inspect
from googletrans import Translator

translator = Translator()

source = inspect.getsource(duolingo)
new_source = source.replace('jwt=None', 'jwt')
new_source = source.replace('self.jwt = None', ' ')
exec(new_source, duolingo.__dict__)

lingo  = duolingo.Duolingo('lingualinkios', jwt='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMzgxMjg1NzA3fQ.y-NV-wMihp2xs4vm535XRQgQT8pFVBZhNDhJ6B6zPgY')

vocab_list = lingo.get_vocabulary("hi")['vocab_overview']

filtered_vocab_list = {}

for item in vocab_list:
    skill = item['skill']
    word = translator.translate(text=item['word_string'], src="hi", dest="en")
    if skill in filtered_vocab_list.keys():
        filtered_vocab_list[skill].append(word.text)
    else:
        filtered_vocab_list[skill] = [word.text]

print(filtered_vocab_list)