'''

安裝套件

'''
!pip install line-bot-sdk flask flask-ngrok

'''
解壓縮模型
'''

from zipfile import ZipFile

with ZipFile('converted_savedmodel.zip', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall('converted_savedmodel')

'''
載入類別列表
'''
class_dict = {}
with open('converted_savedmodel/labels.txt') as f:
    for line in f:
       (key, val) = line.split()
       class_dict[int(key)] = val

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

from flask_ngrok import run_with_ngrok

# 設定Server啟用細節
app = Flask(__name__,static_url_path = "/material" , static_folder = "./material/")
run_with_ngrok(app)

line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('CHANNEL_SECRET')


@app.route("/", methods=['POST'])
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

'''

關注事件，功能說明

'''

# 引用套件
from linebot.models import (
    FollowEvent,TextSendMessage
)

# 關注事件處理
@handler.add(FollowEvent)
def process_follow_event(event):
    
    # 消息發送
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
        """這個教室裡面，我置入了兩個業配，當大家找到了業配，今天課程才算開始。請找到那個業配，拍下來並上傳。"""
        )
    )

'''

文字消息，功能說明

'''

# 引用套件
from linebot.models import (
    MessageEvent,TextMessage,TextSendMessage
)

# 關注事件處理
@handler.add(MessageEvent,message=TextMessage)
def process_text_message_event(event):
    
    # 消息發送
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
        """這個教室裡面，我置入了兩個業配，當大家找到了業配，今天課程才算開始。請找到那個業配，拍下來並上傳。"""
        )
    )

'''

圖片消息，解析圖片

'''

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# 引用套件
from linebot.models import (
    MessageEvent,ImageMessage,TextSendMessage
)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('converted_savedmodel/model.savedmodel')

import time

@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):

    print(time.asctime( time.localtime(time.time()) ))

    message_content = line_bot_api.get_message_content(event.message.id)
    file_name = event.message.id+'.jpg'
    with open(file_name, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    print(time.asctime( time.localtime(time.time()) ))

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(file_name)

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    print(time.asctime( time.localtime(time.time()) ))
    
    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0 - 1 )

    # Load the image into the array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0]= normalized_image_array[0:224,0:224,0:3]

    # run the inference
    prediction = model.predict(data)

    print(time.asctime( time.localtime(time.time()) ))

    max_probability_item_index = np.argmax(prediction[0])

    if prediction.max() > 0.6:
        line_bot_api.reply_message(
          event.reply_token,
          TextSendMessage(
          """這個物件極有可能是 %s ，其相似機率為 %s """ %(class_dict.get(max_probability_item_index), prediction[0][max_probability_item_index])
          )
        )
    else :
      line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
        """再混啊！亂拍照！！"""
        )
      )

if __name__ == "__main__":
    app.run()