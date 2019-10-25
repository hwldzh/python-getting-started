# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError
import requests
import re
import json #引用json模块

engine = Engine()

@engine.define
def test():
	regex = r"defjson:(.*})"
	html=requests.get('http://data.eastmoney.com/xg/kzz/default.html')
	matches = re.finditer(regex, html.text)
	for matchNum, match in enumerate(matches, start=1):
    		return match.group()

@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
