from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 用到的端口 3306 mysql 3300 音乐接口 5000 网络交互 6666 udp服务

use_deepseek = os.getenv('USE_DEEPSEEK', 'True') == 'True'
sfapikey = os.getenv('SFAPIKEY', '')
deepseek_model = os.getenv('DEEPSEEK_MODEL', 'Pro/deepseek-ai/DeepSeek-V3')

use_openai = os.getenv('USE_OPENAI', 'False') == 'True'
openapikey = os.getenv('OPENAPIKEY', '')

use_spark = os.getenv('USE_SPARK', 'False') == 'True'
sparkapi_appid = os.getenv('SPARKAPI_APPID', '')
sparkapi_secret = os.getenv('SPARKAPI_SECRET', '')
sparkapi_key = os.getenv('SPARKAPI_KEY', '')

#####以上模型提供方三选一,True选择对应的模型,需要填写key######

chat_or_standard = os.getenv('CHAT_OR_STANDARD', 'True') == 'True' #采用聊天模式还是标准模式（家庭助手），True为聊天模式（采用流式），详见 prompt_and_deal.py
#切换模式后需删除 message.data文件（如有），否则会导致对话混乱

########语音服务(TTS and STT)##########
use_online_recognize = os.getenv('USE_ONLINE_RECOGNIZE', 'True') == 'True' #是否采用线上语音识别（效果好，针对优化）
azure_key = os.getenv('AZURE_KEY', '')   #使用线上语音识别需填写 Azrue key
speech_synthesis_voice_name = os.getenv('SPEECH_SYNTHESIS_VOICE_NAME', 'zh-CN-XiaoxiaoNeural')

#########语音唤醒模块(二选一)###########
snowboy_enable = os.getenv('SNOWBOY_ENABLE', 'False') == 'True' #是否加载snowboy模块，需提前安装好
snowboypath = os.getenv('SNOWBOYPATH', '/home/pi/xiaoxiao/snowboy') #snowboy位置（如果开启snowboy）

porcupine_enable = os.getenv('PORCUPINE_ENABLE', 'False') == 'True' #是否加载porcupine模块 (推荐，跨平台)
porcupine_key = os.getenv('PORCUPINE_KEY', 'xxxxxxxxxxxxxxxxx') #需要填写密钥
porcupinepath = os.getenv('PORCUPINEPATH', '/home/pi/xiaoxiao/Porcupine') #porcupine位置
porcupine_keyword_name = os.getenv('PORCUPINE_KEYWORD_NAME', 'happiness_en_raspberry-pi_v3_0_0.ppn') #唤醒词文件名

#注:唤醒功能默认关闭，运行时需要在ip:5000将wakebyhw手动勾选，开启唤醒功能
##############
wakebyhw = os.getenv('WAKEBYHW', 'False') == 'True' #是否开启唤醒功能

proxy = {
    'http': os.getenv('PROXY_HTTP', 'http://127.0.0.1:10810'),
    'https': os.getenv('PROXY_HTTPS', 'http://127.0.0.1:10810')
} #openai以及duckduckgo的代理

gpio_wake_enable = os.getenv('GPIO_WAKE_ENABLE', 'False') == 'True'  #按键唤醒，如果相应引脚接有外设的情况下开启
music_enable = os.getenv('MUSIC_ENABLE', 'False') == 'True'  #是否开启音乐功能(需要qq音乐的cookie,并启动QQMusicAPI服务)
qqmusicpath = os.getenv('QQMUSICPATH', '/home/pi/xiaoxiao/QQMusicApi') #MusicApi位置(如果开启音乐模块)
qqid = os.getenv('QQID', '')  #填写登录QQ音乐的QQ号(如果开启音乐模块,必填)
dev_enable = os.getenv('DEV_ENABLE', 'False') == 'True'  #是否开启外设控制功能(需要安装mosquito服务器，配置对应外设)
wlan_enable = os.getenv('WLAN_ENABLE', 'False') == 'True'  #是否开启广域网控制
schedule_enable = os.getenv('SCHEDULE_ENABLE', 'False') == 'True' #是否开启日程提醒功能(需要配置mysql)
udp_enable = os.getenv('UDP_ENABLE', 'False') == 'True' #是否开启无线模块外设唤醒(没有无线模块就不用打开)
hass_demo_enable=os.getenv('HASS_DEMO_ENABLE', 'False') == 'True' #用于演示HomeAssistant的交互，需要配置HomeAssistant。
UdpbroadcastAdd = os.getenv('UDP_BROADCAST_ADD', '192.168.31.255') #UDP广播地址，用于使用无线模块外设唤醒助手