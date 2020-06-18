import json
from channels.generic.websocket import WebsocketConsumer

class MarketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({"message from server": "hello"}))

    def disconnect(self):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        #message = text_data_json['message]

        #self.send(text_data=json.dumps({
        # 'message': message
        # }))

