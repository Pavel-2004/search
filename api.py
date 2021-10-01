from flask import *
import json, time
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'error': 'no data'}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/url/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('url'))
    print(user_query)
    url = requests.get("https://www.zedge.net/ringtone/790049b8-71e5-3b05-b1e2-381e00911a3f")
    htmltext = url.text

    x = htmltext.find("previewUrl") + 14
    final = "h"
    for i in range(x, len(htmltext)):
        if htmltext[i] == '"':
            break
        else:
            final += htmltext[i]
    data_set = {'url': final}
    json_dump = json.dumps(data_set)
    return json_dump



if __name__ == '__main__':
    app.run(port=7777)