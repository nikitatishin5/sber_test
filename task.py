import json
class BaseTask():
    def __init__(self):
        self.input_file = open('source.json', 'r')
        self.output_file = open('index.html', 'w')
    def __del__(self):
        self.input_file.close()
        self.output_file.close()
class Task1(BaseTask):
    def data_prep(self,info:dict):
        string_to_return = ''
        for key in info:
            if key == 'title':
                string_to_return += f'<h1>{info[key]}</h1>'
            elif key == 'body':
                string_to_return += f'<p>{info[key]}</p>'
        return string_to_return
    def json_to_html(self):
        self.output_file.write(''.join(list(map(self.data_prep, json.load(self.input_file)))))
class Task2(Task1):
    def data_prep(self, info: dict):
        string_to_return = ''
        for key in info:
            string_to_return += f'<{key}>{info[key]}</{key}>'
        return string_to_return
class Task3(Task2):
    def json_to_html(self):
        self.output_file.write('<ul>'+''.join(list(map(self.data_prep, json.load(self.input_file))))+'</ul>')
    def data_prep(self, info: dict):
        string_to_return = ''
        for key in info:
            string_to_return += f'<{key}>{info[key]}</{key}>'
        return '<li>'+string_to_return+'</li>'
class Task4(Task3):
    def json_to_html(self,if_req = None):
        # print(list(map(print,json.load(self.input_file))))
        if if_req:
            return '<ul>'+''.join(list(map(self.data_prep, if_req)))+'</ul>'
        else:
            self.output_file.write('<ul>'+''.join(list(map(self.data_prep, json.load(self.input_file))))+'</ul>')
    def data_prep(self, info: dict):
        string_to_return = ''
        for key in info:
            if isinstance(info[key],list):
                string_to_return += f'<{key}>{self.json_to_html(info[key])}</{key}>'
            else:
                string_to_return += f'<{key}>{info[key]}</{key}>'
        return '<li>'+string_to_return+'</li>'

class Task5(Task4):
    def parse_body(self,body:str):
        my_dict = {'<': '&lt;','>':'&gt;'}

        for key in my_dict:
            while body.find(key) != -1:
                body = body.replace(key,my_dict[key])
        return body

    def parse_tags(self,tag_aka_key:str):
        class_list = []
        id_list = []
        key_only = tag_aka_key[:tag_aka_key.index('.')]
        key_body = tag_aka_key[tag_aka_key.index('.')+1:]
        if '#' in key_body:
            key_body = [key_body[:key_body.index('#')],key_body[key_body.index('#')+1:]]
            class_list = key_body[0].split('.')
            id_list = key_body[1].split('.')
        else:
            if 'class' in key_body: class_list = key_body.split('.')
            elif 'id' in key_body : id_list = key_body.split('.')
        return key_only,' '.join(class_list), ' '.join(id_list)


    def json_to_html(self,if_req = None):

        if if_req:
            return '<ul>'+''.join(list(map(self.data_prep, if_req)))+'</ul>'
        else:
            self.output_file.write('<ul>'+''.join(list(map(self.data_prep, json.load(self.input_file))))+'</ul>')

    def data_prep(self, info: dict):
        string_to_return = ''
        for key in info:
            k,classes, ids = self.parse_tags(key)
            tmp_str = f'<{k} '
            if ids: tmp_str += f'id="{ids}" '
            if classes: tmp_str += f'class="{classes}" '
            tmp_str+='>'
            body = info[key]
            if not isinstance(info[key],list)  :
                body = self.parse_body(info[key])
            if isinstance(info[key],list):
                string_to_return += f'{tmp_str}{self.json_to_html(body)}</{k}>'
            else:
                string_to_return += f'{tmp_str}{body}</{k}>'
        return '<li>'+string_to_return+'</li>'



if __name__ == '__main__':
    print(Task5().json_to_html())

