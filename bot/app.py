from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from flask_ngrok import run_with_ngrok
from settings import *
from temp import *

app = Flask(__name__)
run_with_ngrok(app)

line_bot_api = LineBotApi(CHANNEL_ACCSESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

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

@handler.add(MessageEvent, message= TextMessage)
def handler_message(event):
    msg = event.message.text
    if '!beta' in msg:
        line_bot_api.reply_message(event.reply_token,TemplateSendMessage(
            alt_text="您有一則新訊息",
            template=ButtonsTemplate(
                thumbnail_image_url='https://images.chinatimes.com/newsphoto/2021-07-09/1024/20210709001635.jpg',
                title='凱基卷商買超',
                text="請選擇",
                actions=[
                    MessageTemplateAction(label='點下方安扭查看', text='Hello'),
                    URITemplateAction(label='凱基台北', uri ="https://5850web.moneydj.com/z/zg/zgb/zgb0.djhtm?a=9200&b=9268&c=E&e=2022-6-14&f=2022-6-14"),
                ]
            )
        ))
if __name__ == "__main__":
    app.run()