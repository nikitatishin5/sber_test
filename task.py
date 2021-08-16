import json
def json_to_html(info:dict):
    string_to_return = ''
    for key in info:
        if key == 'title':
            string_to_return += f'<h1>{info[key]}</h1>'
        elif key == 'body':
            string_to_return += f'<p>{info[key]}</p>'
    return string_to_return
with open('source.json', 'r') as json_file:
    request = json.load(json_file)
    json_file.close()
final_string = ''.join(list(map(json_to_html,request)))
print(final_string)
with open('index.html', 'w') as html_file:
    html_file.write(final_string)
    html_file.close()

