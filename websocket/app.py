from flask import Flask, Response
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time, json

pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-a7723895-60dc-4568-acde-3aa1f87d5f34"
pnconfig.subscribe_key = "sub-c-aa129212-ad1d-11eb-8759-1eedd707a532"
pnconfig.uuid = "serverUUID-PUB"
pubnub = PubNub(pnconfig)


app = Flask(__name__,
            static_url_path='',
            static_folder='static')


@app.route('/takes_forever')
def hello():
    print('1'*100)
    for i in range(100):
        message = {"entry": 'data', "update": i}
        envelope = pubnub.publish().channel('the_guide').message(message).sync()
        time.sleep(2)
    print('2'*100)
    return "Hello World!"


if __name__ == '__main__':
    app.run()
