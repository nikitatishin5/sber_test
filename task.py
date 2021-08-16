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



if __name__ == '__main__':
    print(Task4().json_to_html())

