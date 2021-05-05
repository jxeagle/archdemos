from flask import Flask, Response
import time, json
app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/takes_forever')
def takes_forever():
    def generate():
        for i in range(100):
            print('running')
            yield json.dumps({'data': i})
            time.sleep(2)
    return Response(generate(), mimetype='application/json')

if __name__ == '__main__':
    app.run()