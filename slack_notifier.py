import json
import requests


class SlackNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def notify(self, date, name):
        message = "{date} {name}さんが入室しました。".format(date=date.strftime("%H:%M"), name=name)
        requests.post(self.webhook_url, data=json.dumps({
            "text": message, "link_names": 1}))

    def send(self, message):
        requests.post(self.webhook_url, data=json.dumps({
            "text": message, "link_names": 1}))
