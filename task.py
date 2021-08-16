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



if __name__ == '__main__':
    print(Task2().json_to_html())

