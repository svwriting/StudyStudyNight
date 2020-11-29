

# #  0. 當在colab上運作
# from google.colab import drive
# drive.mount('/content/drive')                   # 把資料路徑mapping到google drive
# !pip install line-bot-sdk flask flask-ngrok     # 需重新安裝套件


######################### import ##########################
#  1. 引用flask Web Server套件
from flask import Flask, request, abort, jsonify
#  1. 載入json處理套件
import json
#  1. 外部連結自動生成套件
from flask_ngrok import run_with_ngrok
#  1. 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 
from linebot import LineBotApi, WebhookHandler
#  1. 引用 InvalidSignatureError(無效簽章錯誤)
from linebot.exceptions import InvalidSignatureError
#  1. 引入Follow事件
from linebot.models.events import FollowEvent
#  1. 引入各式事件
from linebot.models import (
    MessageEvent, 
    PostbackEvent
)
#  1. 引入各種Message
from linebot.models import (
    # 傳入消息
    TextMessage, ImageMessage,
    # 送出消息
    TextSendMessage, ImageSendMessage, VideoMessage, AudioMessage,
    # 模板(送出)消息
    TemplateSendMessage 
)
#  1. 引入各種Action
from linebot.models import (
    # 傳入消息
    MessageAction, 
    PostbackAction,
    URIAction,
    DatetimePickerAction,
    LocationAction,
    CameraAction, 
    CameraRollAction, 
)
#  1. 引入其他訊息元件
from linebot.models import (
    # 快捷回應、快捷按鈕
    QuickReply, QuickReplyButton,
    # 將bubble類型的json 進行轉換變成 Python可理解之類型物件
    # 將該物件封裝進 Flex Message中
    FlexSendMessage,BubbleContainer
)
#  1. 引入按鍵模板
from linebot.models.template import ButtonsTemplate


######################### globals #########################
#  2. *是否在colab上運作
onColab=False
#  2. *app名
appname="TEST0"
#  2. *存放資訊的各檔名
userlog="app-users.log"     # 用戶資訊
eventlog="app-event.log"    # 事件資訊
#  2. *存放回傳檔案的各資料夾名
store_imgs="store_imgs"     # 回傳圖片資料夾
store_videos="store_videos" # 回傳影片資料夾
store_audios="store_audios" # 回傳音訊資料夾
#  2. *Channel驗證內容，請使用自己的Channel驗證內容
Channel_Access_token="VYe3OYn8SLzyehfhMDIIUv8G5RfxXK5OVug/fScOJpl5/cszSGLBV+zaq6vji6s+1KLsQO4ZVCCKNmxTfpls/o1qkrXjkw32fQNPseFD6OiS2E6T7Lfjc1L1nJTXcjA8x69mN1kBkLXdR52qP6qLBAdB04t89/1O/w1cDnyilFU="
Channel_Secret="5b6657d24bf11adfba3324ecff02eb29"
#-------------------------- path --------------------------
#  2. 在colabg上起始路徑就是Google Drive，不然就是空字串
startpath="/content/drive/MyDrive" if onColab else ""
#  3. app根路徑
apppath_root=f"{startpath}/forLineChatBot_{appname}"
#  4. app存放資訊路徑
apppath_userlog=f"{apppath_root}/{userlog}"
apppath_eventlog=f"{apppath_root}/{eventlog}"
#  4. app存檔資料夾路徑
apppath_imgs=f"{apppath_root}/{store_imgs}"
apppath_videos=f"{apppath_root}/{store_videos}"
apppath_audios=f"{apppath_root}/{store_audios}"
#------------------------ messages ------------------------
#  5. 範例-文字訊息：@123
specific_text_message=TextSendMessage(
    text="官方建議，用戶以文字消息觸發特殊功能的時候，要加上特殊符號")
#  5. 範例-圖片訊息：@分析的本質
analyze_truth_image_message=ImageSendMessage(
    original_content_url='https://i.imgur.com/M8jnn9B.png',
    preview_image_url='https://i.imgur.com/LtCtgg0.jpg'
)
#  5. 範例-模板按鍵訊息：@more
buttons_template_message = TemplateSendMessage(
    # alt_text: Line簡覽視窗所出現的說明文字
    # template: 所使用的模板
    # ButtonsTemplate: 按鍵模板
    #     thumbnail_image_url: 展示圖片
    #     title: 標題
    #     text: 說明文字
    #     actions: 模板行為所使用的行為
    #     data: 觸發postback後用戶回傳值，可以對其做商業邏輯處理
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='更多幫助',
        text='請點擊下方按鈕獲得更多幫助',
        actions=[
          {
            "type": "postback",
            "label": "企業，查找商業結合方案",
            "text": "[::text:]尋找BD",
            "data": "Data1"
          },
          {
            "type": "postback",
            "label": "開發者，尋求教學",
            "text": "[::text:]求助專家",
            "data": "Data2"
          }
        ],
  )
)
#  5. 範例-以json產出文字訊息：預設為文字訊息"哈囉"
def jsonTextSendMessage(json_=None):
    if json_==None:
        # 範例-以文字定義 的 json格式 textSendMessage：說"哈囉"
        json_ = """
            {
            "type": "text",
            "text": "Hello"
            }
        """
    text_send_message= TextSendMessage.new_from_json_dict(
        json.loads(
            json_
        )
    )
    return text_send_message
#------------------- QuickReplyButtons --------------------
# URI動作的戰略價值：
# https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#available-line-url-schemes
#  5. 範例-發送訊息快捷按鈕：以用戶身份發送文字消息
def QRB_Text(label_="發送文字消息",img_url=None,text_=""):
    textQuickReplyButton = QuickReplyButton(
        action=MessageAction(
            label=label_, 
            text=text_
        ),
        image_url=img_url
    )
    return textQuickReplyButton
#  5. 範例-時間選擇快捷按鈕：彈跳出選擇時間之視窗
def QRB_DatetimePicker(label_="時間選擇",img_url=None,mode_="date",data_="data_fromDatetimePicker"):
    dateQuickReplyButton = QuickReplyButton(
        action=DatetimePickerAction(
            label=label_,                      
            mode=mode_,
            data=data_
        ),
        image_url=img_url
    )
    return dateQuickReplyButton
#  5. 範例-開啟相機快捷按鈕：開啟相機
def QRB_Camera(label_="拍照",img_url=None):
    cameraQuickReplyButton = QuickReplyButton(
        action=CameraAction(label=label_),
        image_url=img_url
    )
    return cameraQuickReplyButton
#  5. 範例-相片選擇快捷按鈕：切換至照片相簿選擇
def QRB_PhotoChoose(label_="選擇照片",img_url=None):
    cameraRollQRB = QuickReplyButton(
        action=CameraRollAction(label=label_),
        image_url=img_url
    )
    return cameraRollQRB
#  5. 範例-地理位置快捷按鈕：跳出地理位置
def QRB_Location(label_="地理位置",img_url=None):
    locationQRB = QuickReplyButton(
        action=LocationAction(label=label_),
        image_url=img_url
    )
    return locationQRB
#  5. 範例-Postback快捷按鈕：以Postback事件回應Server 
def QRB_Postback(label_="我是PostbackEvent",img_url=None,data_=None):
    postbackQRB = QuickReplyButton(
        action=PostbackAction(
            label=label_, 
            data=data_
        ),
        image_url=img_url
    )
    return postbackQRB
#----------------------- QuickReply -----------------------
#  6. 範例-快捷回應：將QuickReplyButton(s)加入QuickReply的items
def produceQuickReplyItem(*QuickReplyButtons):
    if QuickReplyButtons==[]:
        QuickReplyButtons=[
            QRB_Text(), 
            QRB_DatetimePicker(), 
            QRB_Camera(), 
            QRB_PhotoChoose(), 
            QRB_Location(),
            QRB_Postback()
        ]
    quickReplyList = QuickReply(
        items = QuickReplyButtons
    )
    return quickReplyList
#  7. 範例-訊息with快捷回應：@reply，讓TextSendMessage伴隨QuickReply
tempQuickReply=produceQuickReplyItem()
quick_reply_text_send_message = TextSendMessage(
    text='發送問題給用戶，請用戶回答', 
    quick_reply=tempQuickReply)
#------------------- messages dict --------------------
#  8. 當用戶輸入相應文字消息，選擇訊息
template_message_dict = {
  "@123":specific_text_message,
  "@分析的本質": analyze_truth_image_message,
  "@more":buttons_template_message,
  "@reply":quick_reply_text_send_message,
}

######################### prepare #########################
#  9. 設定Server啟用細節
app = Flask(
    __name__,
    static_url_path = f"/{appname}" , 
    static_folder = f"./{appname}/"
)
run_with_ngrok(app)
#  9. 生成實體物件
line_bot_api = LineBotApi(Channel_Access_token)
handler = WebhookHandler(Channel_Secret)


######################## responses ########################
# 10. 入口訊息：This is "TEST0"
@app.route("/", methods=['GET'])
def welcome():
    return f" - This is \"{appname}\" - "
# 10. 計算機：v1+v2
@app.route("/calculate", methods=['GET'])
def calculate():
    first_parameter = int(request.args.get('v1'))
    second_parameter = int(request.args.get('v2'))
    return str(first_parameter+second_parameter)
# 10. 入口應答：使Line能丟消息進來
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    # 記錄用戶log
    f = open(apppath_eventlog, "a")
    f.write(body)
    f.close()
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


##################### events handler ######################
# 10. handler添加：如果收到FollowEvent，則記錄用戶資料
@handler.add(FollowEvent)
def reply_text_and_get_user_profile(event):
    # 取出消息內User的資料
    user_profile = line_bot_api.get_profile(event.source.user_id)   
     # 將用戶資訊存在檔案內
    with open(apppath_userlog, "a") as myfile:
        myfile.write(json.dumps(vars(user_profile),sort_keys=True))
        myfile.write('\n')
    # 回覆文字消息與圖片消息
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(f'{appname} 感謝您的關注')]
    )
# 10. handler添加：如果收到文字消息，根據條件內容回傳文字消息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if(event.message.text.find('@')!= -1) and (event.message.text in template_message_dict):
        line_bot_api.reply_message(
        event.reply_token,
        template_message_dict.get(event.message.text)
        )
    else:
        message_="字典內查無此字，請輸入"
        for key_ in template_message_dict:
            message_+=f" {key_} 或者"
        message_=message_[::-1].replace("或者"[::-1],"。",1)[::-1]
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="字典內查無此字")
        )
# 10. 10. handler添加：如果收到PostbackEvent，做出相應處理
@handler.add(PostbackEvent)
def handle_post_message(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    if (event.postback.data.find('Data1')== 0):
        with open("user_profile_business.txt", "a") as myfile:
            myfile.write(json.dumps(vars(user_profile),sort_keys=True))
            myfile.write('\n')
            line_bot_api.reply_message(
            event.reply_token,
                TextMessage(
                    text='請稍待，會有專人與您聯繫'
                )
            )
    elif (event.postback.data.find('Data2') == 0):
        with open("user_profile_tutorial.txt", "a") as myfile:
            myfile.write(json.dumps(vars(user_profile),sort_keys=True))
            myfile.write('\n')
            line_bot_api.reply_message(
            event.reply_token,
                TextMessage(
                    text='請稍待，我們會派專家與您聯繫'
                )
            )
    else:
        pass

    # 取出消息內User的資料
    user_profile = line_bot_api.get_profile(event.source.user_id)   
     # 將用戶資訊存在檔案內
    with open(f"{apppath_root}/{userlog}", "a") as myfile:
        myfile.write(json.dumps(vars(user_profile),sort_keys=True))
        myfile.write('\n')
    # 回覆文字消息與圖片消息
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(f'{appname} 感謝您的關注')]
    )
# 10. handler添加：如果收到圖片消息，回覆用戶文字消息並儲存照片
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Image has Upload'+ ' ' + event.message.id))
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(f"{apppath_imgs}/img_em{event.message.id}.jpg", 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
# 10. handler添加：如果收到影片消息，回覆用戶文字消息並儲存照片
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Video has Upload'+ ' ' + event.message.id))
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(f"{apppath_videos}/video_em{event.message.id}.mp4", 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
# 10. handler添加：如果收到音訊消息，回覆用戶文字消息並儲存照片
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Audio has Upload'+ ' ' + event.message.id))
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(f"{apppath_audios}/audio_em{event.message.id}.mp3", 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)


###################### notification #######################
# 10. 範例-指定推播：對user_id推播message_；
#                   預設為對user_id推播 "Hello World!"
def pushMessage_(user_id, message_="Hello World!"):
    line_bot_api.push_message(
        user_id, 
        TextSendMessage(
            text=message_
        )
    )
# 10. 範例-群體推播：對所有user_id_array裡user_id推播message_；
#                   預設為對所有userlog裡的用戶推播 "Hello World!"
def multicastMessage(user_id_array=[], message_="Hello World!"):
    if user_id_array==[]:
        json_object_strings = open(apppath_userlog,'r') 
        json_array = []
        for json_object_string in json_object_strings:
            json_object = json.loads(json_object_string)
            json_array.append(json_object)
        for user_record in json_array:
            user_id_array.append(user_record.get("user_id"))
    line_bot_api.multicast(
        user_id_array,
        TextSendMessage(
            text=message_
        )
    )
# 10. 懶得試-全體推播 broadcast     (推下去都是錢)
# 10. 懶得試-精準推播 narrowcast    (說明:https://engineering.linecorp.com/zh-hant/blog/narrowcast-api-on-line-chatbot/)


######################### run ############################
# 11. 啟動主程序
app.run()

