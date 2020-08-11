from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('4a7W0DseVYZy/O1WTkiIYuDNUHnmpwRQoOfeBie9UiNhDTyZf5fvnxNgHsS51epkbZxBse4dGth9JP5K+7+QAqmd3vMOkyUMCXnQPEQyeGTljVQ6HPAU9vnM8I0wPrx6msqHswb4UHsvccitDG7q1QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c52ed9412ddbc815a6f5ff5af98dd727')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "I don't understand"
    if msg == 'hi':
        r = "hello"
    elif msg == "Did you sleep well?"
        r = "Nooooooooooooo"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()