import requests#http请求
import json#json数据处理
import traceback#错误捕获
import urllib.request
import time#延时
import os#系统组件
import websocket#ws接口链接
import base64#请求体编码
import threading
import queue
import random
from pygments import highlight#高亮
from pygments.lexers import JsonLexer#高亮
from pygments.formatters import TerminalFormatter#高亮
from colorama import init, Fore, Back, Style#高亮
import urllib.request
import ssl
import psutil
import sys
import sentry_sdk
import threading
import openai

import ctypes

# 获取控制台窗口句柄
kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()


# 设置窗口标题
if hwnd != 0:
    kernel32.SetConsoleTitleW("ChatGPT公用终端进程-1")

openai.api_base = "https://free.gpt.ge/v1"
#openai.api_base = "https://openkey.cloud/v1"

messages = []
openai.api_key="sk-4kY0XJy60toUTzQMC26b5354C8C044C29b03FbDa56Cc7c9c"

sentry_sdk.init(
    dsn="https://a30ed1f97ae54e663e8cf7db6928b17d@o4506171336753152.ingest.sentry.io/4506176633896960",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

init(autoreset=True)  #初始化自动恢复颜色，多次执行会导致卡慢
b=0
lingpai='50357763a9034c07c3a6589d53cce2b0f8d65a523e16911c3319a7'
for s in range(30):
    try:
        zdsxw=10
        b+=1
        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({
        "chat_id":545093460387282944,
        "text":"ChatGPT服务启动[4.8]\n标识号:FREE1\n第"+str(s+1)+"次，共30次"
        })
        print(jsonfile)
        postreturn=requests.post(url,data=jsonfile,headers=headers)
        def get_audio_duration(url,msg):
            """
            try:
                # 要下载的文件的URL
                file_url = url

                # 从URL中提取文件名
                file_name = os.path.basename(file_url)

                # 构建文件的保存路径
                save_path = os.path.join(os.getcwd(), file_name)
                filename=file_name
                # 下载文件并保存到程序根目录
                urllib.request.urlretrieve(url, filename)
                print(f"文件已下载到：{filename}")
            except Exception as e:
                print(f"下载出错：{e}")
            # 获取音频文件的时长
            filepath = filename
            """
            # 获取到的时长单位为秒
            return len(msg) // 4
        '''
        url = "https://speech.ai.xiaomi.com/speech/1.0/tts_token?token=eyJ2IjoiVjAiLCJuIjoiU1oifQ.AAAXUkp9P1QAFgBdFAwbZ24VTkoaRRsPG2AFFhgAQgBIRyIvRw4PfR9GGBh0VUBPEQhHWxBrPkBITxBDEFhHb1RHT0FXEw0QY20QRU4AWgBZTTJVQQ4YTE9KEXF2AAkUSRNMGBh0XUdeQRtQQ31hahBOGRJPQwlGMwUXHBFdQV5ANmhBTk0UTkEPFW4BQXMUWUECR2A-QEtIEkJHXBM3VRtKFQsSAxpgYxceGBVFEBRPJgMAAAAKR0xLMD99FB8ATABeR2NVQBlHWw8KEjE7D0kaERcPAkBlBA8YR1tEDkBqbxQcQhNUDhhLN0QAFhNYGwkTY2IVSkMOVEdCUnQKExobXRACE2ZtGgA.EO5fMqpLGoC6LrZI3pQP5w"
        audio_duration = get_audio_duration(url)
        print(f"音频时长：{audio_duration} 秒")
        '''
        ms='0'
        lingpai='50357763a9034c07c3a67'
        sycyid=[]#使用成员id
        cysycs=[]#成员使用次数
        jgczsj=0#警告重置时间
        gjc=''#绘图关键词
        dycs=0#本次总调用次数
        fwqlb=[]#服务器列表
        fwqxz=[]#服务器选择角色
        fwqms=[]#服务器选择的模式
        efzdy=0#二分钟调用次数
        zdyzyxx=False#是否只打印重要信息，可能会影响性能
        mxlb=[]#模型列表
        hhxxlb=[]#绘画消息列表
        hhpdidlb=[]#频道id列表
        hhidlb=[]#绘画id列表
        xxjl=[]#消息记录
        xxfszid=[]#消息发送者列表
        xxfsz=[]#消息发送者用户名
        qgglb=['433204455396081664','619360459988258816']#去广告服务器id列表
        dljclb=[]#独立进程服务器id列表
        hfms=[]#回复模式
        xerror=False
        def addmsg(msg, color="white"):
            if color == "white":
                print(msg)
            elif color == "red":
                print("\033[31m" + msg + "\033[39m")
            elif color == "yellow":
                print("\033[33m" + msg + "\033[39m")
            elif color == "green":
                print("\033[32m" + msg + "\033[39m")
            elif color == "aqua":
                print("\033[36m" + msg + "\033[39m")

        def colorprint(smg2,pcolor):
            if pcolor=='red':
              print(Fore.RED + smg2)
            elif pcolor=='bandg':
              print(Back.GREEN + smg2)
            elif pcolor=='d':
              print(Style.DIM + smg2)
            # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
            #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True

        def colorize_json(smg2,pcolor=''):
            json_data=smg2
            try:
                try:
                    parsed_json = json.loads(json_data)  # 解析JSON数据
                except Exception as e:
                    parsed_json=json_data
                formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

                # 使用Pygments库进行语法高亮
                colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

                print(colored_json)
            except json.JSONDecodeError as e:
                print(json_data)
        def get_ad(adjl=10,fwqid=0):
            global qgglb
            fsad=random.randint(1,adjl)
            gg=''
            gglb=['[终止托管预警]\n9月后WDG团队下的bot将逐渐停止运行\n了解更多信息：https://in.fanbook.cn/LmgLJF3N \n请尽快考虑自行部署，存储库：https://github.com/fanbook-wangdage/Fanbook-ChatGPT-BOT-V4']
            if adjl==1 or adjl==2 or adjl==3:
                gg=gglb[random.randint(0,len(gglb)-1)]
                print(gg)
            if str(fwqid) in qgglb:
                return ''
            else:
                return gg
            
        def bot_send_message(token=lingpai,pdid=0,text=''):
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
            "chat_id":pdid,
            "text":text
            })
            print(jsonfile)
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        def pdxc(message=None):
            try:
                global ms
                global xz
                global sycyid,cysycs,jgczsj,dycs,hhxxlb,hhidlb,messages
                global gjc,fwqlb,fwqxz,fwqms,efzdy,mxlb,hhpdidlb,xxjl,xxfsz,xxfszid,xerror
                # 处理接收到的消息
                if zdyzyxx == False:
                    addmsg('收到消息',color='green')
                    colorize_json(message)
                message=json.loads(message)
                if message["action"] =="push":
                    if message["data"]["author"]["bot"] == false:
                        if str(message["data"]["guild_id"]) in dljclb:
                            pass
                        else: 
                            content = json.loads(message["data"]["content"])
                            userid=message["data"]["user_id"]
                            fwqid=message["data"]["guild_id"]
                            if "${@!469790724255502336}" in content['text']:
                                if zdyzyxx:
                                    addmsg('收到重要消息',color='green')
                                    colorize_json(message)
                                efzdy+=1
                                dycs+=1
                                if fwqid in fwqlb:
                                    print('服务器id:',fwqid,'已经记录过，不需要重新记录')
                                else:
                                    fwqlb.append(fwqid)
                                    fwqms.append("0")
                                    fwqxz.append('')
                                    mxlb.append('ChatGPT')
                                    messages.append([])
                                    hfms.append(0)
                                    print('服务器id:',fwqid,'已经成功被记录')
                                    print(fwqlb)
                                if userid in sycyid:
                                    sycy=sycyid.index(userid)
                                    cysycs[sycy]+=1
                                    print('用户id:',userid,'使用次数增加1,原本次数为：',cysycs[sycy])
                                else:
                                    sycyid.append(userid)
                                    cysycs.append(1)
                                    print('新使用用户：',userid)
                                    print(sycyid)
                                    print(cysycs)
                                if int(cysycs[sycyid.index(userid)]) == 15:
                                    print('用户：',userid,'第14次操作')
                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                    headers = {'content-type':"application/json;charset=utf-8"}
                                    jsonfile=json.dumps({
                                    "chat_id":int(message["data"]["channel_id"]),
                                    "text": '速率限制：\n你当前给机器人发送消息数超过每两分钟14次，请休息一下，2分钟后再来吧'+get_ad(adjl=2,fwqid=fwqid),
                                    "reply_to_message_id":int(message["data"]["message_id"])
                                    })
                                    print(jsonfile)
                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                elif int(cysycs[sycyid.index(userid)]) < 14:
                                    if '模式切换' in content['text']:
                                        if mxlb[fwqlb.index(fwqid)] == 'ChatGPT':
                                            if fwqms[fwqlb.index(fwqid)]=='0':
                                                fwqms[fwqlb.index(fwqid)]='1'
                                                fwqxz[fwqlb.index(fwqid)]=''
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": '回复模式已切换为语音回复模式(默认为派蒙[喵娘属性])\n可通过快捷指令[切换人物]切换'+get_ad(adjl=2,fwqid=fwqid),
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            else:
                                                fwqms[fwqlb.index(fwqid)]='0'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": '回复模式已切换为文本模式',
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                        else:
                                            fwqms[fwqlb.index(fwqid)]='0'
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": '抱歉，暂时只有ChatGPT支持模式切换，其他均为文本输出，请切换模型为ChatGPT再切换模式'+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif '可选人物' in content['text']:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text": "${@!"+message["data"]["user_id"]+"}"+'所有可选人物列表：空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然\n请使用切换人物指令切换，仅在语音回复模式生效'+get_ad(adjl=2,fwqid=fwqid),
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif '切换人物' in content['text']:
                                        fwqxz[fwqlb.index(fwqid)]=content['text'][31:-1]
                                        print(fwqxz[fwqlb.index(fwqid)])
                                        if str(fwqxz[fwqlb.index(fwqid)]) in allrw:
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": '人物已切换为:'+fwqxz[fwqlb.index(fwqid)],
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        else:
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": '找不到你选择的人物：'+fwqxz[fwqlb.index(fwqid)]+'\n请确认你输入的人物在可选人物列表中'+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif '运行节点信息' in content['text']:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text": "${@!"+message["data"]["user_id"]+"}"+'当前运行节点信息：\n运行节点名：云服务器1[公用]\nip:1.117.76.68\n参考位置：中国-上海市 腾讯云\n近期累计调用次数：'+str(dycs)+'次\n2分钟内调用次数：'+str(efzdy)+'次\n版本号：4.8\n新功能体验/反馈，欢迎前往：https://fanbook.mobi/LmgLJF3N \n体验高级功能，请查看：https://fanbook.mobi/sheet/300000000%24cFTvAWvRbvlJ'+get_ad(adjl=2,fwqid=fwqid),
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif 'AI绘图' in content['text']:
                                        gjc=content['text'][31:-1]
                                        print('关键词:',gjc)
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":"请稍等....\n正在努力生成图片，请在一分钟后再来查看此消息。\n你的关键词/表达式为："+gjc+get_ad(adjl=2,fwqid=fwqid),
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        htxxid=int(postreturn.json()['result']["message_id"])
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        try:
                                            url = "https://api.gptgod.online/v1/images/generations"
                                            payload = json.dumps({
                                            "model": "dall-e-3",
                                            "prompt": gjc,
                                            "n": 1,
                                            "size": "1024x1024"
                                            })
                                            headers = {
                                            'Authorization': 'Bearer sk-OsMMq65tXdfOIlTUYtocSL7NCsmA7CerN77OkEv29dODg1EA',
                                            'Content-Type': 'application/json'
                                            }
                                            response = requests.request("POST", url, headers=headers, data=payload)
                                            print(response.text)
                                            
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": "{\"type\":\"richText\",\"title\":\"图片生成完成\",\"document\":\"[{\\\"insert\\\":\\\"114514\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"图片链接："+json.loads(response.text)['data'][0]['url']+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+json.loads(response.text)['data'][0]['url']+"\\\",\\\"width\\\":1024.0,\\\"height\\\":1024.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                                            "message_id":htxxid,
                                            "parse_mode": "Fanbook"
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        except Exception as e:
                                            if xerror==True:
                                                err=traceback.format_exc()
                                            else:
                                                err=e
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": "图片生成失败，这是常见的，你可以多试几次\n提示：通过system_xerror命令设置失败时显示详细错误信息，复制给开发者以解决错误\n错误信息："+str(err)+"\napi:\n"+str(response.text),
                                            "message_id":htxxid,
                                            #"parse_mode": "Fanbook"
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            
                                    elif '获取绘图图片' in content['text']:
                                        pass
                                        """gjc=content['text'][33:-1]
                                        print('图片id:',gjc)
                                        htmessage=requests.get('https://api.lolimi.cn/api/ai/mj2?key=sWlckPY0hlgaDryj7hnLewOjTU&id='+str(gjc), stream=True)
                                        print(htmessage.text)
                                        htmessage=json.loads(htmessage.text)
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":"{\"type\":\"richText\",\"title\":\"图片获取成功\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"进度："+str(htmessage['data'])+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+str(htmessage["imageurl"])+"\\\",\\\"width\\\":1800.0,\\\"height\\\":2912.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                                        "parse_mode": "Fanbook",
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')"""
                                    elif '切换模型' in content['text']:
                                        if 'ChatGPT' in content['text']:
                                            mxlb[fwqlb.index(fwqid)] = 'ChatGPT'
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"模型已切换为ChatGPT"+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif '文心一言' in content['text']:
                                            mxlb[fwqlb.index(fwqid)] = '文心一言'
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"模型已切换为文心一言"+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif '星火大模型V2.0' in content['text']:
                                            mxlb[fwqlb.index(fwqid)] = '星火大模型V2.0'
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"模型已切换为星火大模型V2.0"+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        elif 'chatGPT3.5搜索' in content['text']:
                                            mxlb[fwqlb.index(fwqid)] = 'chatGPT3.5搜索'
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"模型已切换为chatGPT3.5搜索模型"+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        else:
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"找不到你选择的模型，请重新选择"+get_ad(adjl=2,fwqid=fwqid),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif 'system_message' in content['text']:
                                        print(content['text'][37:])
                                        system_message=content['text'][37:]
                                        messages[fwqlb.index(fwqid)].append({"role":"system","content":system_message})
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":'系统消息添加成功:'+content['text'][37:]+'\n当前上下文列表:\n'+str(messages[fwqlb.index(fwqid)])+'\n最大上下文长度:'+str(zdsxw),
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif '清除上下文' in content['text']:
                                        messages[fwqlb.index(fwqid)]=[]
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":"${@!"+message["data"]["user_id"]+"}"+'清除上下文成功\n最大上下文长度:'+str(zdsxw)+get_ad(adjl=2,fwqid=fwqid),
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif '切换回复模式' in content['text']:
                                        if hfms[fwqlb.index(fwqid)]==0:
                                            hfms[fwqlb.index(fwqid)]=1
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"${@!"+message["data"]["user_id"]+"}"+'回复模式已切换为流回复模式',
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        else:
                                            hfms[fwqlb.index(fwqid)]=0
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":"${@!"+message["data"]["user_id"]+"}"+'回复模式已切换为普通回复模式',
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif 'system_run_py' in content['text']:
                                        print(content['text'][36:])
                                        code=content['text'][36:]
                                        pdid=int(message["data"]["channel_id"])
                                        try:
                                            exec(code, globals())
                                        except Exception as e:
                                            error=traceback.format_exc()
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text":'执行失败，原因：\n'+error+'\ncode:\n'+code,
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":'执行完毕',
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    elif 'system_xerror' in content['text']:
                                        if xerror:
                                            xerror=False
                                            t='xerror->Flase'
                                        else:
                                            xerror=True
                                            t='xerror->True'
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":'完成'+t,
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                    else:
                                        try:
                                            if fwqms[fwqlb.index(fwqid)]=='0':
                                                #text=json.loads(content)
                                                print(mxlb[fwqlb.index(fwqid)]+'文本模式回复')
                                                print(content['text'])
                                                print(content['text'][23:])
                                                print(messages[fwqlb.index(fwqid)])
                                                if mxlb[fwqlb.index(fwqid)] == 'ChatGPT':
                                                    if len(messages[fwqlb.index(fwqid)]) > zdsxw:
                                                        sc=messages[fwqlb.index(fwqid)][0]
                                                        sc2=messages[fwqlb.index(fwqid)][1]
                                                        messages[fwqlb.index(fwqid)].pop(0)
                                                        messages[fwqlb.index(fwqid)].pop(1)
                                                        print('删除了上下文'+str(sc)+str(sc2)+'\n剩余长度'+str(len(messages[fwqlb.index(fwqid)])))
                                                    a=''
                                                    if hfms[fwqlb.index(fwqid)]==1:
                                                        messages[fwqlb.index(fwqid)].append({"role":"user","content": content['text'][23:]})
                                                        zt=0
                                                        for resp in openai.ChatCompletion.create(
                                                                                            model="gpt-3.5-turbo-0125",
                                                                                            messages=messages[fwqlb.index(fwqid)],
                                                                                            # 流式输出
                                                                                            stream = True):
                                                            if 'content' in resp.choices[0].delta:
                                                                if zt==0:
                                                                    zt=1
                                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                                    jsonfile=json.dumps({
                                                                    "chat_id":int(message["data"]["channel_id"]),
                                                                    "text": resp.choices[0].delta.content,
                                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                                    })
                                                                    print(jsonfile)
                                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                                    messageinfo=postreturn.text
                                                                    messageinfo=json.loads(messageinfo)
                                                                a+=resp.choices[0].delta.content
                                                                print(resp.choices[0].delta.content, end="", flush=True)
                                                                print(a)
                                                                if random.randint(0,100)<25:
                                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                                    jsonfile=json.dumps({
                                                                    "chat_id":int(message["data"]["channel_id"]),
                                                                    "message_id":messageinfo['result']['message_id'],
                                                                    "text": a,
                                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                                    })
                                                                    print(jsonfile)
                                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                                        headers = {'content-type':"application/json;charset=utf-8"}
                                                        jsonfile=json.dumps({
                                                        "chat_id":int(message["data"]["channel_id"]),
                                                        "message_id":messageinfo['result']['message_id'],
                                                        "text": a,
                                                        "reply_to_message_id":int(message["data"]["message_id"])
                                                        })
                                                        print(jsonfile)
                                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                                        reply = a
                                                        print(reply)
                                                        chatmessage=reply
                                                        messages[fwqlb.index(fwqid)].append({"role": "assistant", "content": chatmessage})
                                                    else:
                                                        messages[fwqlb.index(fwqid)].append({"role":"user","content": content['text'][23:]})
                                                        response=openai.ChatCompletion.create(
                                                        model="gpt-3.5-turbo-0125",
                                                        messages=messages[fwqlb.index(fwqid)]
                                                        )
                                                        
                                                        reply = response["choices"][0]["message"]["content"]
                                                        print(reply)
                                                        chatmessage=reply
                                                        messages[fwqlb.index(fwqid)].append({"role": "assistant", "content": chatmessage})
                                                        text=chatmessage.replace('', '')+get_ad(adjl=8)
                                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                        headers = {'content-type':"application/json;charset=utf-8"}
                                                        jsonfile=json.dumps({
                                                        "chat_id":int(message["data"]["channel_id"]),
                                                        "text": "${@!"+message["data"]["user_id"]+"}"+text+get_ad(adjl=8,fwqid=fwqid),
                                                        #"parse_mode":"Fanbook",
                                                        "reply_to_message_id":int(message["data"]["message_id"])
                                                        })
                                                        print(jsonfile)
                                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                                if mxlb[fwqlb.index(fwqid)] == 'chatGPT3.5搜索':
                                                    if len(messages[fwqlb.index(fwqid)]) > zdsxw:
                                                        sc=messages[fwqlb.index(fwqid)][0]
                                                        sc2=messages[fwqlb.index(fwqid)][1]
                                                        messages[fwqlb.index(fwqid)].pop(0)
                                                        messages[fwqlb.index(fwqid)].pop(1)
                                                        print('删除了上下文'+str(sc)+str(sc2)+'\n剩余长度'+str(len(messages[fwqlb.index(fwqid)])))
                                                    a=''
                                                    openai.api_key = "sk-4kY0XJy60toUTzQMC26b5354C8C044C29b03FbDa56Cc7c9c"
                                                    openai.api_base = "https://free.gpt.ge/v1"
                                                    if hfms[fwqlb.index(fwqid)]==1:
                                                        messages[fwqlb.index(fwqid)].append({"role":"user","content": content['text'][23:]})
                                                        zt=0
                                                        for resp in openai.ChatCompletion.create(
                                                                                            model="net-gpt-3.5-turbo",
                                                                                            messages=messages[fwqlb.index(fwqid)],
                                                                                            # 流式输出
                                                                                            stream = True):
                                                            if 'content' in resp.choices[0].delta:
                                                                if zt==0:
                                                                    zt=1
                                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                                    jsonfile=json.dumps({
                                                                    "chat_id":int(message["data"]["channel_id"]),
                                                                    "text": resp.choices[0].delta.content,
                                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                                    })
                                                                    print(jsonfile)
                                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                                    messageinfo=postreturn.text
                                                                    messageinfo=json.loads(messageinfo)
                                                                a+=resp.choices[0].delta.content
                                                                print(resp.choices[0].delta.content, end="", flush=True)
                                                                print(a)
                                                                if random.randint(0,100)<25:
                                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                                    jsonfile=json.dumps({
                                                                    "chat_id":int(message["data"]["channel_id"]),
                                                                    "message_id":messageinfo['result']['message_id'],
                                                                    "text": a,
                                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                                    })
                                                                    print(jsonfile)
                                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                                        headers = {'content-type':"application/json;charset=utf-8"}
                                                        jsonfile=json.dumps({
                                                        "chat_id":int(message["data"]["channel_id"]),
                                                        "message_id":messageinfo['result']['message_id'],
                                                        "text": a,
                                                        "reply_to_message_id":int(message["data"]["message_id"])
                                                        })
                                                        print(jsonfile)
                                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                                        reply = a
                                                        print(reply)
                                                        chatmessage=reply
                                                        messages[fwqlb.index(fwqid)].append({"role": "assistant", "content": chatmessage})
                                                    else:
                                                        messages[fwqlb.index(fwqid)].append({"role":"user","content": content['text'][23:]})
                                                        response=openai.ChatCompletion.create(
                                                        model="net-gpt-3.5-turbo",
                                                        messages=messages[fwqlb.index(fwqid)]
                                                        )
                                                        
                                                        reply = response["choices"][0]["message"]["content"]
                                                        print(reply)
                                                        chatmessage=reply
                                                        messages[fwqlb.index(fwqid)].append({"role": "assistant", "content": chatmessage})
                                                        text=chatmessage.replace('', '')+get_ad(adjl=8)
                                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                        headers = {'content-type':"application/json;charset=utf-8"}
                                                        jsonfile=json.dumps({
                                                        "chat_id":int(message["data"]["channel_id"]),
                                                        "text": "${@!"+message["data"]["user_id"]+"}"+text+get_ad(adjl=8,fwqid=fwqid),
                                                        #"parse_mode":"Fanbook",
                                                        "reply_to_message_id":int(message["data"]["message_id"])
                                                        })
                                                        print(jsonfile)
                                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                                    openai.api_base = "https://api.chatanywhere.com.cn/v1"
                                                    openai.api_key="sk-EoeISBCAJdJhi8xJgfCiC99AGdqyRWE9wXHanBhBDbDacJ2E"
                                                elif mxlb[fwqlb.index(fwqid)] == '文心一言':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/wx.php?type=json&format=0&msg='+content['text'][23:], stream=True)
                                                    chatmessage=json.loads(chatmessage.text)
                                                elif mxlb[fwqlb.index(fwqid)] == '星火大模型V2.0':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/xh.php?type=json&format=0&msg='+content['text'][23:]+'.', stream=True)
                                                    chatmessage=json.loads(chatmessage.text)
                                                print(chatmessage)
                                                n="""
            """
                                                if mxlb[fwqlb.index(fwqid)] == '星火大模型V2.0' or mxlb[fwqlb.index(fwqid)] == '文心一言':
                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                    jsonfile=json.dumps({
                                                    "chat_id":int(message["data"]["channel_id"]),
                                                    "text": chatmessage['data']['output'].replace('\n', n)+get_ad(adjl=8,fwqid=fwqid),
                                                    "reply_to_message_id":int(message["data"]["message_id"]),
                                                    })
                                                    print(jsonfile)
                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                '''
                                                else:
                                                    #chatmessage=chatmessage['data'].replace('\\\\', '\\')
                                                    chatmessage=chatmessage.replace('\\n', n)
                                                    text=chatmessage.replace('', '')+get_ad(adjl=8)
                                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                    headers = {'content-type':"application/json;charset=utf-8"}
                                                    jsonfile=json.dumps({
                                                    "chat_id":int(message["data"]["channel_id"]),
                                                    "text": "${@!"+message["data"]["user_id"]+"}"+text+get_ad(adjl=8,fwqid=fwqid),
                                                    #"parse_mode":"Fanbook",
                                                    "reply_to_message_id":int(message["data"]["message_id"])
                                                    })
                                                    print(jsonfile)
                                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                                '''
                                            elif fwqms[fwqlb.index(fwqid)]=='1':
                                                print('音频模式回复')
                                                print(content['text'])
                                                print(content['text'][23:])
                                                if fwqxz[fwqlb.index(fwqid)] == '':
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/ys3.5.php?msg=.'+content['text'][23:], stream=True)
                                                else:
                                                    chatmessage=requests.get('https://api.lolimi.cn/API/AI/ys3.5.php?msg=.'+content['text'][23:]+'&speaker='+xz, stream=True)
                                                chatmessage=json.loads(chatmessage.text)
                                                print(chatmessage)
                                                print(chatmessage['music'])
                                                url = chatmessage['music']
                                                audio_duration = get_audio_duration(str(url),msg=chatmessage['msg'])
                                                print(f"音频时长：{audio_duration} 秒")
                                                xx='{"type": "voice","url": "'+chatmessage['music']+'","second": '+str(int(audio_duration))+',"isRead": false}'
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": xx,
                                                "reply_to_message_id":int(message["data"]["message_id"])
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                            xxjl.append(mxlb[fwqlb.index(fwqid)]+'模式回复消息:'+content['text'][23:].replace('\n', '')+'，模型回复:'+str(chatmessage).replace('\n', ''))
                                            xxfsz.append('发送者:'+message["data"]["author"]["nickname"]+message["data"]["author"]["username"])
                                            xxfszid.append('userid:'+message['data']["user_id"]+" 服务器id:"+str(fwqid))
                                        except Exception as e:
                                            time.sleep(3)
                                            if xerror:
                                                error=traceback.format_exc()
                                            else:
                                                error=str(e)
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": "回复消息时出现错误\n你可以重试\n"+"信息："+str(error),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                else:
                                    print('用户：',userid,'已经操作过快，忽略输入')
                                    
                                
            except Exception as e:
                if 'KeyError' in traceback.format_exc():
                    pass
                else:
                    error=traceback.format_exc()
                    print(error)
                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({
                    "chat_id":545093460387282944,
                    "text":"发生错误:\n"+error
                    })
                    print(jsonfile)
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    colorize_json(smg2=postreturn.text,pcolor='d')
        allrw='空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然'
        allrw=allrw.split(', ')
        print(allrw)
        xz=''
        false=False
        data_queue = queue.Queue()
        def on_message(ws, message):
            n_pdxc = threading.Thread(target=pdxc,args=(message,))
            n_pdxc.start()
            # 在这里添加你希望执行的操作
        def on_error(ws, error):
            # 处理错误
            if 'KeyError' in traceback.format_exc():
                pass
            else:
                error=traceback.format_exc()
                addmsg("发生错误:"+str(error),color='red')
                print(error)
                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({
                "chat_id":545093460387282944,
                "text":"发生错误:\n"+error
                })
                print(jsonfile)
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                colorize_json(smg2=postreturn.text,pcolor='d')
        def on_close(ws):
            # 连接关闭时的操作
            addmsg("连接已关闭",color='red')
            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
            headers = {'content-type':"application/json;charset=utf-8"}
            jsonfile=json.dumps({
            "chat_id":545093460387282944,
            "text":"ws连接被关闭"
            })
            print(jsonfile)
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            colorize_json(smg2=postreturn.text,pcolor='d')
        def on_open(ws):
            # 连接建立时的操作
            addmsg("连接已建立",color='green')
            # 发送心跳包
            def send_ping():
                print('发送：{"type":"ping"}')
                ws.send('{"type":"ping"}')
            send_ping()  # 发送第一个心跳包
            # 定时发送心跳包
            def schedule_ping():
                send_ping()
                """
                # 每25秒发送一次心跳包
                websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                ws.send_ping()
                websocket._get_connection().sock.settimeout(70)
                ws.send('{"type":"ping"}')
                """
            #websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)
        # 替换成用户输入的BOT令牌
        lingpai = lingpai
        url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"
        # 发送HTTP请求获取基本信息
        response = requests.get(url)
        data = response.json()
        def send_data_thread():
            global sycyid,cysycs,jgczsj,efzdy,hhxxlb,hhidlb,hhpdidlb,xxfsz,xxjl,xxfszid
            while True:
                
                """
                for x in range(3):
                    cpu_res = psutil.cpu_percent(interval=1)
                     
                print(cpu_res/3)
                """
                # 在这里编写需要发送的数据
                time.sleep(17)
                with open('xxjl.txt', 'w',encoding="utf-8") as file:
                    for item in xxjl:
                        file.write(f"{item}\n")
                with open('xxfsz.txt', 'w',encoding="utf-8") as file:
                    for item in xxfsz:
                        file.write(f"{item}\n")
                with open('xxfszid.txt', 'w',encoding="utf-8") as file:
                    for item in xxfszid:
                        file.write(f"{item}\n")
                ws.send('{"type":"ping"}')
                addmsg('发送心跳包：{"type":"ping"}',color='green')
                requests.get(url='https://uptime.betterstack.com/api/v1/heartbeat/cjtmwjvkCypVZu3aSm5Uai3f')
                if len(xxjl) != len(xxfsz) or len(xxjl) != len(xxfszid) or len(xxjl) != len(xxfszid):
                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                    headers = {'content-type':"application/json;charset=utf-8"}
                    jsonfile=json.dumps({
                    "chat_id":545093460387282944,
                    "text":"[dev 1]\n[警告]\n[BUG]消息记录数据异常，已尝试清除"
                    })
                    print(jsonfile)
                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                    xxjl=[]
                    xxfsz=[]
                    xxfszid=[]
                jgczsj+=1
                for i in hhidlb:
                    z=hhpdidlb[hhidlb.index(i)]
                    sy=hhidlb.index(i)
                    try:
                        htmessage=requests.get('https://api.lolimi.cn/api/ai/mj2?key=sWlckPY0hlgaDryj7hnLewOjTU&id='+str(i), stream=True)
                        print(htmessage.text)
                        htmessage=json.loads(htmessage.text)
                        if str(htmessage['data']) != "100%":
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(z),
                            "text": "{\"type\":\"richText\",\"title\":\"图片正在生成，请稍等...\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"进度："+str(htmessage['data'])+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+str(htmessage["imageurl"])+"\\\",\\\"width\\\":1800.0,\\\"height\\\":2912.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                            "message_id":int(hhxxlb[hhidlb.index(i)]),
                            "parse_mode": "Fanbook"
                            })
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                        else:
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(z),
                            "text": "{\"type\":\"richText\",\"title\":\"图片生成完成\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"进度："+str(htmessage['data'])+"\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+str(htmessage["imageurl"])+"\\\",\\\"width\\\":1800.0,\\\"height\\\":2912.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                            "message_id":int(hhxxlb[hhidlb.index(i)]),
                            "parse_mode": "Fanbook"
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text,pcolor='d')
                            hhidlb.pop(sy)
                            hhpdidlb.pop(sy)
                            hhxxlb.pop(sy)
                    except Exception as e:
                        try:
                            if str(htmessage["pointout"]) == "请耐心等待出图":
                                pass
                            else:
                                hhidlb.pop(sy)
                                hhpdidlb.pop(sy)
                                hhxxlb.pop(sy)
                        #hhidlb.pop(sy)
                        #hhpdidlb.pop(sy)
                        #hhxxlb.pop(sy)
                        except Exception as e:
                            pass
                        pass
                print('当前警告重置时间：',str(jgczsj))
                if jgczsj >= 10:
                    print('警告重置')
                    jgczsj=0
                    efzdy=0
                    sycyid=[]#使用成员id
                    cysycs=[]#成员使用次数
                    #hhpdidlb.clear()
                    #hhidlb.clear()
                    #hhxxlb.clear()
        if response.ok and data.get("ok"):
            user_token = data["result"]["user_token"]
            device_id = "your_device_id"
            version_number = "1.6.60"
            super_str = base64.b64encode(json.dumps({
                "platform": "bot",
                "version": version_number,
                "channel": "office",
                "device_id": device_id,
                "build_number": "1"
            }).encode('utf-8')).decode('utf-8')
            ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
            threading.Thread(target=send_data_thread, daemon=True).start()
            # 建立WebSocket连接
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp(ws_url,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
            ws.on_open = on_open
            ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        else:
            addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
        '''
        xx='{"type": "voice","url": "https://speech.ai.xiaomi.com/speech/1.0/tts_token?token=eyJ2IjoiVjAiLCJuIjoiU1oifQ.AAAXUkp9P1QAFgBdFAwbZ24VTkoaRRsPG2AFFhgAQgBIRyIvRw4PfR9GGBh0VUBPEQhHWxBrPkBITxBDEFhHb1RHT0FXEw0QY20QRU4AWgBZTTJVQQ4YTE9KEXF2AAkUSRNMGBh0XUdeQRtQQ31hahBOGRJPQwlGMwUXHBFdQV5ANmhBTk0UTkEPFW4BQXMUWUECR2A-QEtIEkJHXBM3VRtKFQsSAxpgYxceGBVFEBRPJgMAAAAKR0xLMD99FB8ATABeR2NVQBlHWw8KEjE7D0kaERcPAkBlBA8YR1tEDkBqbxQcQhNUDhhLN0QAFhNYGwkTY2IVSkMOVEdCUnQKExobXRACE2ZtGgA.EO5fMqpLGoC6LrZI3pQP5w","second": '+str(int(audio_duration))+',"isRead": false}'

        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({
        "chat_id":int(pdid),
        "text": xx
        })
        postreturn=requests.post(url,data=jsonfile,headers=headers)
        colorize_json(smg2=postreturn.text,pcolor='d')
        '{\"type\":\"richText\",\"title\":\"\",\"document\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"111111111\\\\n测试\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\"https://fb-cdn.fanbook.mobi/fanbook/app/files/chatroom/unKnow/df8ce32b1e5e6990d4d958343a4b973d.png\\\",\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}","entities":[]}}'
        '''
    except Exception as e:
        print(f"出错：{e}")
        #global b
        lingpai='50357763a9034c07c3a6589d53cce2b59b8e16911c3319a7'
        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({
        "chat_id":545093460387282944,
        "text":"发生异常:\n"+str(traceback.format_exc())+"\n尝试次数:"+str(b)+"/30\n尝试重新启动..."
        })
        print(jsonfile)
        postreturn=requests.post(url,data=jsonfile,headers=headers)
        print(postreturn.text)
        continue
    