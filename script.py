import duolingo
import inspect

source = inspect.getsource(duolingo)
new_source = source.replace('jwt=None', 'jwt')
new_source = source.replace('self.jwt = None', ' ')
exec(new_source, duolingo.__dict__)

lingo  = duolingo.Duolingo('lingualinkios', jwt='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMzgxMjg1NzA3fQ.y-NV-wMihp2xs4vm535XRQgQT8pFVBZhNDhJ6B6zPgY')

print(lingo.get_known_words("hi"))