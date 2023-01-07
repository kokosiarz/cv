# coding=UTF8
import json
from jinja2 import Template

with open('data.json',encoding='utf8') as data_file:
    with open('cv.html',encoding='utf8') as templatef:
        temp = templatef.readlines()
        print(temp)
        template = Template(temp)
        data = json.load(data_file)
        template.render(data=data, getid = lambda x : "skill_level_"+str(id(x)))
