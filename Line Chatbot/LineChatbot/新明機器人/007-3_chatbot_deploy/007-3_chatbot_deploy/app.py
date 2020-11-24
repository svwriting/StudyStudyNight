'''

對話機器人主結構，任何用戶發的話，必然經過此方法

用戶發的任何Event，都存成Log

'''

# 引用Web Server套件
from flask import Flask, request, abort
import os

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)

# 載入json處理套件
import json
# from flask_ngrok import run_with_ngrok

# 設定Server啟用細節
app = Flask(__name__,static_url_path = "/material" , static_folder = "./material/")
# run_with_ngrok(app)

import os
# 生成實體物件
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

# 引用套件
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# from google.colab import auth
# from oauth2client.client import GoogleCredentials
import gspread



# 啟動server對外接口，使Line能丟消息進來
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 驗證準備
    gauth = GoogleAuth()

    # 載入本地端的設定檔
    gauth.LoadCredentialsFile("mycreds.txt")

    # 若裡面沒有設定檔，則用Colab常使用的驗證方式取得設定檔
    if gauth.access_token_expired:
      gauth.Refresh()
    else:
      gauth.Authorize()

    global drive
    drive = GoogleDrive(gauth)

    # 將新生成的設定檔儲存起來
    gauth.SaveCredentialsFile("mycreds.txt")

    # 事前必須準備好一個 檔名為chatbot-event-log的google sheet
    global gc
    gc = gspread.authorize( gauth.credentials )
    worksheet = gc.open('chatbot-event-log').sheet1
    worksheet.append_row([body])


    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


'''

讓開發者可把資料放在material資料夾內，開發者透過裡面的Json設定檔，將消息發給用戶

'''

# 引用會用到的套件
from linebot.models import (
    ImagemapSendMessage, TextSendMessage, ImageSendMessage, LocationSendMessage, FlexSendMessage, VideoSendMessage,StickerSendMessage,AudioSendMessage
)

from linebot.models.template import (
    ButtonsTemplate, CarouselTemplate, ConfirmTemplate, ImageCarouselTemplate

)

from linebot.models.template import *


def detect_json_array_to_new_message_array(fileName):
    # 開啟檔案，轉成json
    root_folder = drive.ListFile({'q': "title='material' "}).GetList()

    file_content = ''
    for root_object in root_folder:
        if root_object['mimeType'] == 'application/vnd.google-apps.folder':

            # print(anything)
            material_folder = drive.ListFile(
                {'q': " '{}' in parents and trashed=false".format(root_object['id'])}).GetList()
            # print(fileList2)
            for anything_in_material_folder in material_folder:
                # print(replyJson)
                if anything_in_material_folder['title'] == fileName:
                    # print(anything_in_reply_folder)
                    target_folder = drive.ListFile(
                        {'q': " '{}' in parents and trashed=false".format(anything_in_material_folder['id'])}).GetList()
                    for reply_json in target_folder:
                        # print(target)
                        if reply_json['title'] == 'reply.json':
                            file_content = reply_json.GetContentString()
                            break
    jsonArray = json.loads(file_content)

    # 解析json
    returnArray = []
    for jsonObject in jsonArray:

        # 讀取其用來判斷的元件
        message_type = jsonObject.get('type')

        # 轉換
        if message_type == 'text':
            returnArray.append(TextSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'imagemap':
            returnArray.append(ImagemapSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'template':
            returnArray.append(TemplateSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'image':
            returnArray.append(ImageSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'sticker':
            returnArray.append(StickerSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'audio':
            returnArray.append(AudioSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'location':
            returnArray.append(LocationSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'flex':
            returnArray.append(FlexSendMessage.new_from_json_dict(jsonObject))
        elif message_type == 'video':
            returnArray.append(VideoSendMessage.new_from_json_dict(jsonObject))

            # 回傳
    return returnArray


'''

用戶關注時，取得個資，並綁定選單，並偵測關注資料夾，並存成User的相關Log

'''

# 引用套件
from linebot.models import (
    FollowEvent
)


# 關注事件處理
@handler.add(FollowEvent)
def process_follow_event(event):
    # 讀取並轉換
    result_message_array = []
    replyJsonPath = "關注"
    result_message_array = detect_json_array_to_new_message_array(replyJsonPath)

    # 消息發送
    line_bot_api.reply_message(
        event.reply_token,
        result_message_array
    )

    # 取個資
    user_profile = line_bot_api.get_profile(event.source.user_id)
    profile_worksheet = gc.open('chatbot-profile-log').sheet1
    profile_worksheet.append_row([json.dumps(vars(user_profile), sort_keys=True)])


'''

用戶發文字訊息時，會從material資料夾內的指定資料夾取回reply.json

'''


# 引用套件
from linebot.models import (
    MessageEvent, TextMessage
)

# 文字消息處理
@handler.add(MessageEvent,message=TextMessage)
def process_text_message(event):

    # 讀取本地檔案，並轉譯成消息
    result_message_array =[]
    replyJsonPath = event.message.text
    result_message_array = detect_json_array_to_new_message_array(replyJsonPath)

    # 發送
    line_bot_api.reply_message(
        event.reply_token,
        result_message_array
    )

'''

用戶發圖片/影片/檔案訊息/發音訊檔案，都取回放入LineBot的資料夾內

'''

# 引用套件
from linebot.models import (
    MessageEvent, ImageMessage
)

# 圖片消息處理
@handler.add(MessageEvent,message=ImageMessage)
def process_image_message(event):

        # 發送
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(event.message.id + ' has upload.' )
    )

    # 讀取本地檔案，並轉譯成消息
    message_content = line_bot_api.get_message_content(event.message.id)
    image_file_name= event.message.id+'.jpg'
    with open(image_file_name, 'wb') as fd:
      for chunk in message_content.iter_content():
          fd.write(chunk)

    folderName="images"
    folders = drive.ListFile({'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
      if folder['title'] == folderName:
        file2 = drive.CreateFile({'title':event.message.id+'.jpg','parents': [{'id': folder['id']}]})
        file2.SetContentFile(image_file_name)
        file2.Upload()

'''

用戶發圖片/影片/檔案訊息/發音訊檔案，都取回放入LineBot的資料夾內

'''

# 引用套件
from linebot.models import (
    MessageEvent, VideoMessage
)

# 影片消息處理
@handler.add(MessageEvent,message=VideoMessage)
def process_video_message(event):

        # 發送
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(event.message.id + ' has upload.' )
    )

    # 讀取本地檔案，並轉譯成消息
    message_content = line_bot_api.get_message_content(event.message.id)
    image_file_name= event.message.id+'.mp4'
    with open(image_file_name, 'wb') as fd:
      for chunk in message_content.iter_content():
          fd.write(chunk)

    folderName="images"
    folders = drive.ListFile({'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
      if folder['title'] == folderName:
        file2 = drive.CreateFile({'title':event.message.id+'.mp4','parents': [{'id': folder['id']}]})
        file2.SetContentFile(image_file_name)
        file2.Upload()

'''

用戶發圖片/影片/檔案訊息/發音訊檔案，都取回放入LineBot的資料夾內

'''

# 引用套件
from linebot.models import (
    MessageEvent, AudioMessage
)

# 影片消息處理
@handler.add(MessageEvent,message=AudioMessage)
def process_audio_message(event):

        # 發送
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(event.message.id + ' has upload.' )
    )

    # 讀取本地檔案，並轉譯成消息
    message_content = line_bot_api.get_message_content(event.message.id)
    image_file_name= event.message.id+'.mp3'
    with open(image_file_name, 'wb') as fd:
      for chunk in message_content.iter_content():
          fd.write(chunk)

    folderName="images"
    folders = drive.ListFile({'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
      if folder['title'] == folderName:
        file2 = drive.CreateFile({'title':event.message.id+'.mp3','parents': [{'id': folder['id']}]})
        file2.SetContentFile(image_file_name)
        file2.Upload()


'''

用戶發PostbackEvent時，若指定menu=xxx，則可更換menu

若menu欄位有值，則
    讀取其rich_menu_id，並取得用戶id，將用戶與選單綁定
    讀取其reply.json，轉譯成消息，並發送


'''

from linebot.models import (
    PostbackEvent
)

from urllib.parse import parse_qs


@handler.add(PostbackEvent)
def process_postback_event(event):
    query_string_dict = parse_qs(event.postback.data)

    print(query_string_dict)

    if 'menu' in query_string_dict:
        replyJsonPath = query_string_dict.get('menu')[0]


        # 開啟檔案，轉成json
        root_folder = drive.ListFile({'q': "title='material' "}).GetList()

        linkRichMenuId = query_string_dict.get('menu')[0]
        for root_object in root_folder:
            if root_object['mimeType'] == 'application/vnd.google-apps.folder':

                # print(anything)
                material_folder = drive.ListFile(
                    {'q': " '{}' in parents and trashed=false".format(root_object['id'])}).GetList()
                # print(fileList2)
                for anything_in_material_folder in material_folder:
                    # print(replyJson)
                    if anything_in_material_folder['title'] == linkRichMenuId:
                        # print(anything_in_reply_folder)
                        target_folder = drive.ListFile(
                            {'q': " '{}' in parents and trashed=false".format(anything_in_material_folder['id'])}).GetList()
                        for reply_json in target_folder:
                            # print(target)
                            if reply_json['title'] == 'rich_menu_id':
                                linkRichMenuId = reply_json.GetContentString()
                                break

        # 綁定圖文選單
        line_bot_api.link_rich_menu_to_user(event.source.user_id, linkRichMenuId)

        result_message_array = detect_json_array_to_new_message_array(replyJsonPath)
        line_bot_api.reply_message(
            event.reply_token,
            result_message_array
        )




'''

伺服器運行

'''

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
    # app.run()
