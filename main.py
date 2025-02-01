import logging
import coloredlogs
# 创建日志记录器
logger = logging.getLogger(__name__)

# 配置 coloredlogs
coloredlogs.install(level='DEBUG', logger=logger)
logger.info("开始加载库")
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
init(autoreset=True)  #初始化自动恢复颜色，多次执行会导致卡慢
import urllib.request
import ssl
import psutil
import sys
import sentry_sdk
import threading
import openai
import fanbookbotapi
import ctypes
import re
from g4f.client import Client
logger.info("加载完成，开始初始化")

def is_string_in_another_string(str1, str2):
    # 使用search()函数
    if re.search(str1, str2):
        return True
    else:
        return False

# 获取控制台窗口句柄
kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()

# 设置窗口标题
if hwnd != 0:
    kernel32.SetConsoleTitleW("ChatGPT公用终端进程-1")

openai.api_base = "https://api.chatanywhere.tech/v1"
#openai.api_base = "https://openkey.cloud/v1"

messages = []
openai.api_key="sk-EoeISBCAJdJhi8xJgfCiC99AGdqyRWE9wXHanBhBDbDacJ2E"

sentry_sdk.init(
    dsn="https://cc747dea8f773476ede3e713f99b3593@o4507525750521856.ingest.us.sentry.io/4507706575421440",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

b=0
lingpai=''

def sentrytool(tags,key,v=1):
    # Increment a counter by one for each button click.
    sentry_sdk.metrics.incr(
        key=key,
        value=v,
        tags=tags
    )
logger.info("初始化完成，开始运行")
for s in range(30):
    try:
        zdsxw=10
        b+=1
        print(fanbookbotapi.sendmessage(lingpai,chatid=545093460387282944,text="ChatGPT服务启动[5.2]\n标识号:FREE1\n第"+str(s+1)+"次，共30次",type='text').text)
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
        ms='0'
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
        qgglb=[]#去广告服务器id列表
        dljclb=[]#独立进程服务器id列表
        hfms=[]#回复模式
        tsc=[]#提示词
        kimi_Id=[]#kimi的上下文id
        glm_id=[]#智谱清言 ChatGLM4的上下文id
        glm4_token=''
        kimi_token=''
        black_list=[]
        black_msg=[]
        sycs1=0
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
            gglb=['']
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
                global gjc,fwqlb,fwqxz,fwqms,efzdy,mxlb,hhpdidlb,xxjl,xxfsz,xxfszid,xerror,sycs1,kimi_Id,glm_id
                # 处理接收到的消息
                if zdyzyxx == False:
                    logger.info('收到消息')
                    colorize_json(message)
                message=json.loads(message)
                if message["action"] =="push":
                    if message["data"]["author"]["bot"] == false:
                        fwqid=message["data"]["guild_id"]
                        if str(message["data"]["guild_id"]) in dljclb:
                            pass
                        else: 
                            content = json.loads(message["data"]["content"])
                            userid=message["data"]["user_id"]
                            fwqid=message["data"]["guild_id"]
                            if "${@!469790724255502336}" in content['text']:#注意这里的botid
                                if zdyzyxx:
                                    logger.info('收到重要消息')
                                    colorize_json(message)
                                efzdy+=1
                                dycs+=1
                                if fwqid in fwqlb:
                                    logger.info('服务器id:'+str(fwqid)+'已经记录过，不需要重新记录')
                                else:
                                    fwqlb.append(fwqid)
                                    fwqms.append("0")
                                    fwqxz.append('')
                                    mxlb.append('ChatGPT')
                                    messages.append([])
                                    hfms.append(0)
                                    tsc.append('')
                                    kimi_Id.append('none')
                                    glm_id.append('none')
                                    logger.info('服务器id:'+str(fwqid)+'已经成功被记录')
                                    print(fwqlb)
                                    sentrytool({"fwqid":fwqid},"newFwq")
                                if userid in sycyid:
                                    sycy=sycyid.index(userid)
                                    cysycs[sycy]+=1
                                    logger.info('用户id:'+str(userid)+'使用次数增加1,原本次数为：'+str(cysycs[sycy]))
                                    sentrytool({"userid":userid,"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":messages[fwqlb.index(fwqid)],"pdid":str(message["data"]["channel_id"])},"yhsy")
                                else:
                                    sycyid.append(userid)
                                    cysycs.append(1)
                                    logger.info('新使用用户，id:'+str(userid))
                                    print(sycyid)
                                    print(cysycs)
                                    sentrytool({"fwqid":fwqid,"userid":userid},"newUser")
                                    sentrytool({"fwqid":fwqid,"userid":userid,"pdid":str(message["data"]["channel_id"])},"yhsy")
                                if int(cysycs[sycyid.index(userid)]) == 15:
                                    logger.warning('用户：'+str(userid)+'第15次操作')
                                    postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="你当前给机器人发送消息数超过每两分钟14次，请休息一下，2分钟后再来吧",biaoti='速率限制',type='card')
                                    colorize_json(smg2=postreturn.text,pcolor='d')
                                    sentrytool({"userid":userid},"sulvxianzhi")
                                    
                                elif int(cysycs[sycyid.index(userid)]) < 14:
                                    logger.debug('开始处理消息')
                                    if str(fwqid) in black_list:
                                        fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text=f'抱歉，用于以下原因暂时无法回复该服务器的消息：\n{black_msg[black_list.index(fwqid)]}')
                                        raise Exception("服务器已被屏蔽")
                                    if '运行节点信息' in content['text']:
                                        postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="${@!"+message["data"]["user_id"]+"}"+'当前运行节点信息：\n运行节点名：云服务器1[公用]\nip:124.221.67.43\n参考位置：中国-上海市 腾讯云\n近期累计调用次数：'+str(dycs)+'次\n2分钟内调用次数：'+str(efzdy)+'次\n版本号：5.2\n新功能体验/反馈，欢迎前往：https://fanbook.mobi/LmgLJF3N',type='text')
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"])},"yxjdxx")
                                    elif 'AI绘图' in content['text']:
                                        gjc=content['text'][31:-1]
                                        print('关键词:',gjc)
                                        url = "https://dalle.feiyuyu.net/requests"#获取使用量

                                        payload = ""
                                        headers = {
                                        'Authorization': 'Bearer 516344f7-434c',
                                        'Content-Type': 'application/json'
                                        }
                                        response = requests.request("POST", url, headers=headers, data=payload)

                                        print(response.text)
                                        
                                        r=response.json()
                                        if r["left_times"]<1:
                                            fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text='使用量超过限制，等一会再用吧\n不要着急，'+str(r["reset_mins"])+'分钟以后就能用了',ik=[[]])
                                            sentrytool({"userid":userid,"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":messages[fwqlb.index(fwqid)],"pdid":str(message["data"]["channel_id"]),"gjc":gjc,"sycs":str(sycs1),"fwqid":str(fwqid)},"aihuituxianzhi")
                                            return None
                                        
                                        sycs1=r["left_times"]
                                        
                                        postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="请稍等....\n正在努力生成图片，请在一分钟后再来查看此消息。\n你的关键词/表达式为："+gjc,type='text')
                                        htxxid=int(postreturn.json()['result']["message_id"])
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        try:
                                            url = "https://dalle.feiyuyu.net/v1/images/generations"

                                            payload = json.dumps({
                                            "model": "dall-e-3",
                                            "prompt": gjc,
                                            "n": 1,
                                            "size": "1024x1024"
                                            })
                                            headers = {
                                            'Authorization': 'Bearer 516344f7-434c',
                                            'Content-Type': 'application/json'
                                            }

                                            response = requests.request("POST", url, headers=headers, data=payload)

                                            print(response.text)

                                            if not is_string_in_another_string('github',json.loads(response.text)['data'][0]['url']):
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": "{\"type\":\"richText\",\"title\":\"图片生成完成\",\"document\":\"[{\\\"insert\\\":\\\"114514\\\\n测试\\\\n\\\\n[图片]\\\\n\\\"}]\",\"v2\":\"[{\\\"insert\\\":\\\"图片链接："+json.loads(response.text)['data'][0]['url']+"\\\\n你这一会还可以使用"+str(sycs1-1)+"次\\\\n\\\\n\\\\n\\\"},{\\\"insert\\\":{\\\"name\\\":\\\"paste_image_1693622751346.png\\\",\\\"source\\\":\\\""+json.loads(response.text)['data'][0]['url']+"\\\",\\\"width\\\":1024.0,\\\"height\\\":1024.0,\\\"checkPath\\\":null,\\\"_type\\\":\\\"image\\\",\\\"_inline\\\":false}},{\\\"insert\\\":\\\"\\\\n\\\\n\\\"}]\",\"v\":2}",
                                                "message_id":htxxid,
                                                "parse_mode": "Fanbook"
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                                sentrytool({"userid":userid,"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":messages[fwqlb.index(fwqid)],"pdid":str(message["data"]["channel_id"]),"gjc":gjc,"url":json.loads(response.text)['data'][0]['url'],"sycs":str(sycs1),"fwqid":str(fwqid)},"aihuitu")
                                            else:
                                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/editMessageText'
                                                headers = {'content-type':"application/json;charset=utf-8"}
                                                jsonfile=json.dumps({
                                                "chat_id":int(message["data"]["channel_id"]),
                                                "text": "图片生成失败，可能是因为你的关键词不准确，ai不知道这是什么意思\n你的生成句子应该是这样的：一只猫，而不是：帮我画一只猫，你可以切换模型为GLM4，然后和ai说要画什么",
                                                "message_id":htxxid,
                                                #"parse_mode": "Fanbook"
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text,pcolor='d')
                                                sentrytool({"userid":userid,"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":messages[fwqlb.index(fwqid)],"pdid":str(message["data"]["channel_id"]),"gjc":gjc,"err":str(traceback.format_exc()),"sycs":str(sycs1),"fwqid":str(fwqid)},"aihuituerr")
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
                                            sentrytool({"userid":userid,"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":messages[fwqlb.index(fwqid)],"pdid":str(message["data"]["channel_id"]),"gjc":gjc,"err":str(traceback.format_exc()),"sycs":str(sycs1),"fwqid":str(fwqid)},"aihuituerr")
                                            
                                    elif '切换模型' in content['text']:
                                        if 'ChatGPT' in content['text']:
                                            messages[fwqlb.index(fwqid)]=[]
                                            mxlb[fwqlb.index(fwqid)] = 'ChatGPT'
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="模型已切换为ChatGPT",type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)]},"xzmx")
                                        elif '文心一言' in content['text']:
                                            fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text='该模型暂时下线，敬请期待',ik=[[]])
                                            return None
                                            mxlb[fwqlb.index(fwqid)] = '文心一言'
                                        elif '星火大模型V2.0' in content['text']:
                                            fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text='该模型暂时下线，敬请期待',ik=[[]])
                                            return None
                                            mxlb[fwqlb.index(fwqid)] = '星火大模型V2.0'
                                        elif 'chatGPT3.5搜索' in content['text']:
                                            messages[fwqlb.index(fwqid)]=[]
                                            mxlb[fwqlb.index(fwqid)] = 'chatGPT3.5搜索'
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="模型已切换为chatGPT3.5搜索（联网）模型",type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)]},"xzmx")
                                        elif 'KimiAI' in content['text']:
                                            messages[fwqlb.index(fwqid)]=[]
                                            kimi_Id[fwqlb.index(fwqid)]='none'
                                            mxlb[fwqlb.index(fwqid)] = 'KimiAI'
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="模型已切换为KimiAI模型",type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)]},"xzmx")
                                        elif 'GLM4' in content['text']:
                                            messages[fwqlb.index(fwqid)]=[]
                                            glm_id[fwqlb.index(fwqid)]='none'
                                            mxlb[fwqlb.index(fwqid)] = 'GLM4'
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="模型已切换为GLM4模型",type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)]},"xzmx")
                                        else:
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="找不到你选择的模型，请重新选择",type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            
                                    elif 'system_message' in content['text']:
                                        print(content['text'][37:])
                                        system_message=content['text'][37:]
                                        messages[fwqlb.index(fwqid)].append({"role":"system","content":system_message})
                                        postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text='系统消息添加成功:'+content['text'][37:]+'\n当前上下文列表:\n'+str(messages[fwqlb.index(fwqid)])+'\n最大上下文长度:'+str(zdsxw),type='text')
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"syssmg":system_message},"systemmessage")
                                    elif '清除上下文' in content['text']:
                                        messages[fwqlb.index(fwqid)]=[]
                                        kimi_Id[fwqlb.index(fwqid)]="none"
                                        glm_id[fwqlb.index(fwqid)]="none"
                                        postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="${@!"+message["data"]["user_id"]+"}"+'清除上下文成功\n最大上下文长度:'+str(zdsxw)+get_ad(adjl=2,fwqid=fwqid),type='text')
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)]},"qcsxw")
                                        if tsc[fwqlb.index(fwqid)]!='':
                                            if tsc[fwqlb.index(fwqid)]!=[]:
                                                messages[fwqlb.index(fwqid)].append({"role": "system", "content": tsc[fwqlb.index(fwqid)]})
                                                logger.debug('重新添加提示词')
                                            
                                    elif '切换回复模式' in content['text']:
                                        if hfms[fwqlb.index(fwqid)]==0:
                                            hfms[fwqlb.index(fwqid)]=1
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="${@!"+message["data"]["user_id"]+"}"+'回复模式已切换为流回复模式',type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        else:
                                            hfms[fwqlb.index(fwqid)]=0
                                            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text="${@!"+message["data"]["user_id"]+"}"+'回复模式已切换为普通回复模式',type='text')
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                        sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)]},"qhhfms")
                                    # elif 'system_run_py' in content['text']:
                                    #     print(content['text'][36:])
                                    #     code=content['text'][36:]
                                    #     pdid=int(message["data"]["channel_id"])
                                    #     try:
                                    #         exec(code, globals())
                                    #     except Exception as e:
                                    #         error=traceback.format_exc()
                                    #         url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                    #         headers = {'content-type':"application/json;charset=utf-8"}
                                    #         jsonfile=json.dumps({
                                    #         "chat_id":int(message["data"]["channel_id"]),
                                    #         "text":'执行失败，原因：\n'+error+'\ncode:\n'+code,
                                    #         "reply_to_message_id":int(message["data"]["message_id"])
                                    #         })
                                    #         print(jsonfile)
                                    #         postreturn=requests.post(url,data=jsonfile,headers=headers)
                                    #         colorize_json(smg2=postreturn.text,pcolor='d')
                                    #     url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                    #     headers = {'content-type':"application/json;charset=utf-8"}
                                    #     jsonfile=json.dumps({
                                    #     "chat_id":int(message["data"]["channel_id"]),
                                    #     "text":'执行完毕',
                                    #     "reply_to_message_id":int(message["data"]["message_id"])
                                    #     })
                                    #     print(jsonfile)
                                    #     postreturn=requests.post(url,data=jsonfile,headers=headers)
                                    #     colorize_json(smg2=postreturn.text,pcolor='d')
                                    #     sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"code":code},"runcode")
                                    elif 'system_xerror' in content['text']:
                                        if xerror:
                                            xerror=False
                                            t='xerror->Flase'
                                        else:
                                            xerror=True
                                            t='xerror->True'
                                        postreturn=fanbookbotapi.sendmessage(lingpai,chatid=int(message["data"]["channel_id"]),text='完成'+t,type='text')
                                        colorize_json(smg2=postreturn.text,pcolor='d')
                                        sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"x":str(xerror)},"systemXerror")
                                    elif '设置提示词' in content['text']:
                                        tsc[fwqlb.index(fwqid)]=content['text'][32:-1]
                                        fwqms[fwqlb.index(fwqid)]=='0'
                                        if tsc[fwqlb.index(fwqid)]=='0':
                                            tsc[fwqlb.index(fwqid)]=''
                                            mxlb[fwqlb.index(fwqid)] = 'ChatGPT'
                                            messages[fwqlb.index(fwqid)]=[]
                                            fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text=f'提示词已成功取消',ik=[[]])
                                            return None
                                
                                        print(tsc[fwqlb.index(fwqid)])
                                        r=json.loads(requests.get(f'https://124.221.67.43/webapi/web/getdataforid?id={tsc[fwqlb.index(fwqid)]}').text)
                                        if r['code']==200:
                                            messages[fwqlb.index(fwqid)]=[]
                                            mxlb[fwqlb.index(fwqid)] = 'ChatGPT'
                                            tsc[fwqlb.index(fwqid)]=r['data'][0]['tsc']
                                            messages[fwqlb.index(fwqid)]=[]
                                            text=f'已成功设置提示词\n提示词名称：{r['data'][0]['name']}\n简介：{r['data'][0]['introduce']}\n创建日期：{r['data'][0]['date']}\n创建者：$'
                                            text+='{@!'+r['data'][0]['uid']+'}'+'\n设置提示词id为0即可取消'
                                            messages[fwqlb.index(fwqid)].append({"role": "system", "content": tsc[fwqlb.index(fwqid)]})
                                            openai.api_key = "sk-EoeISBCAJdJhi8xJgfCiC99AGdqyRWE9wXHanBhBDbDacJ2E"
                                            openai.api_base = "https://api.chatanywhere.tech/v1"
                                            fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text=text,ik=[[]])
                                            return None
                                        
                                        else:
                                            tsc[fwqlb.index(fwqid)]=''
                                            fanbookbotapi.sendmessage(token=lingpai,chatid=int(message["data"]["channel_id"]),type='text',text=f'选择失败\n{r['code']} {r['msg']}\n可能是该提示词正在审核、被删除或者id无效，前往https://124.221.67.43/aibot/ 寻找新的提示词',ik=[[]])
                                        messages[fwqlb.index(fwqid)]=[]
                                        sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)]},"sztsc")
                                        
                                    else:
                                        openai.api_key = "sk-EoeISBCAJdJhi8xJgfCiC99AGdqyRWE9wXHanBhBDbDacJ2E"
                                        openai.api_base = "https://api.chatanywhere.tech/v1"
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
                                                        del messages[fwqlb.index(fwqid)][0]
                                                        del messages[fwqlb.index(fwqid)][1]
                                                        print('删除了上下文'+str(sc)+str(sc2)+'\n剩余长度'+str(len(messages[fwqlb.index(fwqid)])))
                                                        if tsc[fwqlb.index(fwqid)]!='':
                                                            del messages[fwqlb.index(fwqid)][0]
                                                            messages[fwqlb.index(fwqid)].append({"role": "system", "content": tsc[fwqlb.index(fwqid)]})
                                                        
                                                    a=''
                                                    if hfms[fwqlb.index(fwqid)]==1:
                                                        messages[fwqlb.index(fwqid)].append({"role":"user","content": content['text'][23:]})
                                                        zt=0
                                                        try:
                                                            for resp in openai.ChatCompletion.create(
                                                                                                model="gpt-3.5-turbo",
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
                                                                    api2=0
                                                        except Exception as e:
                                                            api2=1
                                                            error=traceback.format_exc()
                                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)]),"text":content['text'][23:],"err":str(error).replace('\n', '')},"api1err")
                                                            client = Client()
                                                            response = client.chat.completions.create(
                                                                model="gpt-3.5-turbo",
                                                                messages=messages[fwqlb.index(fwqid)]
                                                            )
                                                            print(response.choices[0].message.content)
                                                            a=response.choices[0].message.content
                                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)]),"text":content['text'][23:]},"api2ok")
                                                        if api2==0:
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
                                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                                            headers = {'content-type':"application/json;charset=utf-8"}
                                                            jsonfile=json.dumps({
                                                            "chat_id":int(message["data"]["channel_id"]),
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
                                                        try:
                                                            response=openai.ChatCompletion.create(
                                                            model="gpt-3.5-turbo",
                                                            messages=messages[fwqlb.index(fwqid)]
                                                            )
                                                            
                                                            reply = response["choices"][0]["message"]["content"]
                                                            if len(reply)>2:
                                                                print(reply)
                                                                chatmessage=reply
                                                            else:
                                                                sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)]),"text":content['text'][23:],"err":"apiNoContent"},"api1err")
                                                                client = Client()
                                                                response = client.chat.completions.create(
                                                                    model="gpt-3.5-turbo",
                                                                    messages=messages[fwqlb.index(fwqid)]
                                                                )
                                                                print(response.choices[0].message.content)
                                                                chatmessage=response.choices[0].message.content
                                                                sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)])},"api2ok")
                                                        except Exception as e:
                                                            error=traceback.format_exc()
                                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)]),"text":content['text'][23:],"err":str(error).replace('\n', '')},"api1err")
                                                            client = Client()
                                                            response = client.chat.completions.create(
                                                                model="gpt-3.5-turbo",
                                                                messages=messages[fwqlb.index(fwqid)]
                                                            )
                                                            print(response.choices[0].message.content)
                                                            chatmessage=response.choices[0].message.content
                                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)])},"api2ok")
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
                                                    sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)]),"text":content['text'][23:],"chatmessage":chatmessage},"yhsychatgpt")
                                                if mxlb[fwqlb.index(fwqid)] == 'chatGPT3.5搜索':
                                                    if len(messages[fwqlb.index(fwqid)]) > zdsxw:
                                                        sc=messages[fwqlb.index(fwqid)][0]
                                                        sc2=messages[fwqlb.index(fwqid)][1]
                                                        messages[fwqlb.index(fwqid)].pop(0)
                                                        messages[fwqlb.index(fwqid)].pop(1)
                                                        print('删除了上下文'+str(sc)+str(sc2)+'\n剩余长度'+str(len(messages[fwqlb.index(fwqid)])))
                                                    a=''
                                                    openai.api_key = "sk-xEfyaZvkrqeC9iyO05124411B99e48379b588123F2EdFaE1"
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
                                
                                                    sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)])},"yhsychatgptss")
                                                    openai.api_base = "https://api.chatanywhere.com.cn/v1"
                                                    openai.api_key="sk-EoeISBCAJdJhi8xJgfCiC99AGdqyRWE9wXHanBhBDbDacJ2E"
                                                elif mxlb[fwqlb.index(fwqid)] == 'KimiAI':
                                                    ok=0
                                                    #检测引用消息
                                                    try:
                                                        if message["data"]["quote_l1"]!=None:
                                                            url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMessage"
                                                            payload = json.dumps({
                                                            "chat_id": int(message["data"]["channel_id"]),
                                                            "message_id": int(message["data"]["quote_l1"])
                                                            })
                                                            headers = {
                                                            'Content-Type': 'application/json'
                                                            }

                                                            response = requests.request("POST", url, headers=headers, data=payload)

                                                            print(response.text)
                                                            msg=json.loads(json.loads(response.text)["result"]["text"])
                                                            if msg["type"]=="image":
                                                                url = "http://124.221.67.43/v1/chat/completions"
                                                                payload = json.dumps({
                                                                    "conversation_id": kimi_Id[fwqlb.index(fwqid)],
                                                                    "model": "kimi",
                                                                    "messages": [
                                                                        {
                                                                            "role": "user",
                                                                            "content": [
                                                                                {
                                                                                    "type": "image_url",
                                                                                    "image_url": {
                                                                                        "url": msg["url"]
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": content['text'][23:]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ],
                                                                    "use_search": false
                                                                })
                                                                headers = {
                                                                'Authorization': 'Bearer '+kimi_token,
                                                                'Content-Type': 'application/json'
                                                                }

                                                                response = requests.request("POST", url, headers=headers, data=payload)
                                                                postreturn=response
                                                                text=json.loads(postreturn.text)["choices"][0]["message"]["content"]
                                                                chatmessage=text
                                                                kimi_Id[fwqlb.index(fwqid)]=json.loads(postreturn.text)["id"]
                                                                ok=1
                                                            if msg["type"]=="file":
                                                                url = "http://124.221.67.43/v1/chat/completions"
                                                                payload = json.dumps({
                                                                    "conversation_id": kimi_Id[fwqlb.index(fwqid)],
                                                                    "model": "kimi",
                                                                    "messages": [
                                                                        {
                                                                            "role": "user",
                                                                            "content": [
                                                                                {
                                                                                    "type": "file",
                                                                                    "file_url": {
                                                                                        "url": msg["file_url"]
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": content['text'][23:]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ],
                                                                    "use_search": false
                                                                })
                                                                headers = {
                                                                'Authorization': 'Bearer '+kimi_token,
                                                                'Content-Type': 'application/json'
                                                                }

                                                                response = requests.request("POST", url, headers=headers, data=payload)
                                                                postreturn=response
                                                                text=json.loads(postreturn.text)["choices"][0]["message"]["content"]
                                                                chatmessage=text
                                                                kimi_Id[fwqlb.index(fwqid)]=json.loads(postreturn.text)["id"]
                                                                ok=1
                                                            else:
                                                                #引发异常已便跳出
                                                                raise Exception("未找到引用文件")
                                                        else:
                                                            #引发异常已便跳出
                                                            raise Exception("未找到引用文件")
                                                    except:
                                                        if ok==0:
                                                            logger.info("引用消息解析失败")
                                                            url = "http://124.221.67.43/v1/chat/completions"
                                                            payload = json.dumps({
                                                            "conversation_id": kimi_Id[fwqlb.index(fwqid)],
                                                            "model": "kimi",
                                                            "messages": [
                                                                {
                                                                    "role": "user",
                                                                    "content": content['text'][23:]
                                                                }
                                                            ],
                                                            "use_search": True,
                                                            "stream": False
                                                            })
                                                            headers = {
                                                            'Authorization': 'Bearer '+kimi_token,
                                                            'Content-Type': 'application/json'
                                                            }

                                                            response = requests.request("POST", url, headers=headers, data=payload)

                                                            print(response.text)
                                                            postreturn=response
                                                            text=json.loads(postreturn.text)["choices"][0]["message"]["content"]
                                                            chatmessage=text
                                                            kimi_Id[fwqlb.index(fwqid)]=json.loads(postreturn.text)["id"]
                                                        
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
                                                    sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)])},"Kimi")
                                                    print(response.text)
                                                    
                                                elif mxlb[fwqlb.index(fwqid)] == 'GLM4':
                                                    ok=0
                                                    #检测引用消息
                                                    try:
                                                        if message["data"]["quote_l1"]!=None:
                                                            url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMessage"
                                                            payload = json.dumps({
                                                            "chat_id": int(message["data"]["channel_id"]),
                                                            "message_id": int(message["data"]["quote_l1"])
                                                            })
                                                            headers = {
                                                            'Content-Type': 'application/json'
                                                            }

                                                            response = requests.request("POST", url, headers=headers, data=payload)

                                                            print(response.text)
                                                            msg=json.loads(json.loads(response.text)["result"]["text"])
                                                            if msg["type"]=="image":
                                                                url = "http://124.221.67.43/glm/v1/chat/completions"
                                                                payload = json.dumps({
                                                                    "id": glm_id[fwqlb.index(fwqid)],
                                                                    "model": "glm4",
                                                                    "messages": [
                                                                        {
                                                                            "role": "user",
                                                                            "content": [
                                                                                {
                                                                                    "type": "image_url",
                                                                                    "image_url": {
                                                                                        "url": msg["url"]
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": content['text'][23:]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ],
                                                                })
                                                                headers = {
                                                                'Authorization': 'Bearer '+glm4_token,
                                                                'Content-Type': 'application/json'
                                                                }

                                                                response = requests.request("POST", url, headers=headers, data=payload)
                                                                postreturn=response
                                                                text=json.loads(postreturn.text)["choices"][0]["message"]["content"]
                                                                chatmessage=text
                                                                glm_id[fwqlb.index(fwqid)]=json.loads(postreturn.text)["id"]
                                                                ok=1
                                                            if msg["type"]=="file":
                                                                url = "http://124.221.67.43/glm/v1/chat/completions"
                                                                payload = json.dumps({
                                                                    "id": glm_id[fwqlb.index(fwqid)],
                                                                    "model": "glm4",
                                                                    "messages": [
                                                                        {
                                                                            "role": "user",
                                                                            "content": [
                                                                                {
                                                                                    "type": "file",
                                                                                    "file_url": {
                                                                                        "url": msg["file_url"]
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": content['text'][23:]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                })
                                                                headers = {
                                                                'Authorization': 'Bearer '+glm4_token,
                                                                'Content-Type': 'application/json'
                                                                }

                                                                response = requests.request("POST", url, headers=headers, data=payload)
                                                                postreturn=response
                                                                text=json.loads(postreturn.text)["choices"][0]["message"]["content"]
                                                                chatmessage=text
                                                                glm_id[fwqlb.index(fwqid)]=json.loads(postreturn.text)["id"]
                                                                ok=1
                                                            else:
                                                                #引发异常已便跳出
                                                                raise Exception("未找到引用文件")
                                                        else:
                                                            #引发异常已便跳出
                                                            raise Exception("未找到引用文件")
                                                    except:
                                                        if ok==0:
                                                            print("引用消息解析失败")
                                                            url = "http://124.221.67.43/glm/v1/chat/completions"
                                                            payload = json.dumps({
                                                            "conversation_id":glm_id[fwqlb.index(fwqid)],
                                                            "model": "glm4",
                                                            "messages": [
                                                                {
                                                                    "role": "user",
                                                                    "content": content['text'][23:]
                                                                }
                                                            ],
                                                            "stream": False
                                                            })
                                                            headers = {
                                                            'Authorization': 'Bearer '+glm4_token,
                                                            'Content-Type': 'application/json'
                                                            }

                                                            response = requests.request("POST", url, headers=headers, data=payload)

                                                            print(response.text)
                                                            postreturn=response
                                                            text=json.loads(postreturn.text)["choices"][0]["message"]["content"]
                                                            chatmessage=text
                                                            glm_id[fwqlb.index(fwqid)]=json.loads(postreturn.text)["id"]
                                                        
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
                                                    sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)])},"GLM4")
                                                    print(response.text)
                                                    
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
                                            logger.debug('消息处理完成')
                                        except Exception as e:
                                            time.sleep(3)
                                            if not xerror:
                                                error=traceback.format_exc()
                                            else:
                                                error=str(e)
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            jsonfile=json.dumps({
                                            "chat_id":int(message["data"]["channel_id"]),
                                            "text": "回复消息时出现错误\n你可以重试\n或者使用切换模型功能换一个模型试试\n"+"信息："+str(error),
                                            "reply_to_message_id":int(message["data"]["message_id"])
                                            })
                                            print(jsonfile)
                                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                                            colorize_json(smg2=postreturn.text,pcolor='d')
                                            sentrytool({"userid":str(message["data"]["user_id"]),"fwqid":str(fwqid),"pdid":str(message["data"]["channel_id"]),"m":mxlb[fwqlb.index(fwqid)],"tsc":tsc[fwqlb.index(fwqid)],"hfms":hfms[fwqlb.index(fwqid)],"xxlb":str(messages[fwqlb.index(fwqid)]),"e":str(traceback.format_exc()).replace('\n', '')},"err")
                                else:
                                    print('用户：',userid,'已经操作过快，忽略输入')
                                    
                                
            except Exception as e:
                if 'KeyError' in traceback.format_exc():
                    pass
                else:
                    logger.warning("处理消息错误")
                    error=traceback.format_exc()
                    print(error)
                    postreturn=fanbookbotapi.sendmessage(lingpai,chatid=545093460387282944,text="发生错误:\n"+error,type='text')
                    colorize_json(smg2=postreturn.text,pcolor='d')
        # allrw='空, 荧, 派蒙, 纳西妲, 阿贝多, 温迪, 枫原万叶, 钟离, 荒泷一斗, 八重神子, 艾尔海森, 提纳里, 迪希雅, 卡维, 宵宫, 莱依拉, 赛诺, 诺艾尔, 托马, 凝光, 莫娜, 北斗, 神里绫华, 雷电将军, 芭芭拉, 鹿野院平藏, 五郎, 迪奥娜, 凯亚, 安柏, 班尼特, 琴, 柯莱, 夜兰, 妮露, 辛焱, 珐露珊, 魈, 香菱, 达达利亚, 砂糖, 早柚, 云堇, 刻晴, 丽莎, 迪卢克, 烟绯, 重云, 珊瑚宫心海, 胡桃, 可莉, 流浪者, 久岐忍, 神里绫人, 甘雨, 戴因斯雷布, 优菈, 菲谢尔, 行秋, 白术, 九条裟罗, 雷泽, 申鹤, 迪娜泽黛, 凯瑟琳, 多莉, 坎蒂丝, 萍姥姥, 罗莎莉亚, 留云借风真君, 绮良良, 瑶瑶, 七七, 奥兹, 米卡, 夏洛蒂, 埃洛伊, 博士, 女士, 大慈树王, 三月七, 娜塔莎, 希露瓦, 虎克, 克拉拉, 丹恒, 希儿, 布洛妮娅, 瓦尔特, 杰帕德, 佩拉, 姬子, 艾丝妲, 白露, 星, 穹, 桑博, 伦纳德, 停云, 罗刹, 卡芙卡, 彦卿, 史瓦罗, 螺丝咕姆, 阿兰, 银狼, 素裳, 丹枢, 黑塔, 景元, 帕姆, 可可利亚, 半夏, 符玄, 公输师傅, 奥列格, 青雀, 大毫, 青镞, 费斯曼, 绿芙蓉, 镜流, 信使, 丽塔, 失落迷迭, 缭乱星棘, 伊甸, 伏特加女孩, 狂热蓝调, 莉莉娅, 萝莎莉娅, 八重樱, 八重霞, 卡莲, 第六夜想曲, 卡萝尔, 姬子, 极地战刃, 布洛妮娅, 次生银翼, 理之律者, 真理之律者, 迷城骇兔, 希儿, 魇夜星渊, 黑希儿, 帕朵菲莉丝, 天元骑英, 幽兰黛尔, 德丽莎, 月下初拥, 朔夜观星, 暮光骑士, 明日香, 李素裳, 格蕾修, 梅比乌斯, 渡鸦, 人之律者, 爱莉希雅, 爱衣, 天穹游侠, 琪亚娜, 空之律者, 终焉之律者, 薪炎之律者, 云墨丹心, 符华, 识之律者, 维尔薇, 始源之律者, 芽衣, 雷之律者, 苏莎娜, 阿波尼亚, 陆景和, 莫弈, 夏彦, 左然'
        # allrw=allrw.split(', ')
        # print(allrw)
        logger.info("初始化websocket连接")
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
                logger.warning("处理消息错误")
                print(error)
                postreturn=fanbookbotapi.sendmessage(lingpai,chatid=545093460387282944,text="发生错误:\n"+error,type='text')
                colorize_json(smg2=postreturn.text,pcolor='d')
        def on_close(ws):
            # 连接关闭时的操作
            logger.warning("连接已关闭")
            postreturn=fanbookbotapi.sendmessage(lingpai,chatid=545093460387282944,text="ws连接被关闭",type='text')
            colorize_json(smg2=postreturn.text,pcolor='d')
        def on_open(ws):
            # 连接建立时的操作
            logger.debug("连接已建立")
            sentrytool({"cs":str(b)},"wsok")
            # 发送心跳包
            def send_ping():
                logger.debug('发送：{"type":"ping"}')
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
                time.sleep(10)
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
                try:requests.get(url='https://uptime.betterstack.com/api/v1/heartbeat/cjtmwjvkCypVZu3aSm5Uai3f')
                except:pass
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
                logger.debug('当前警告重置时间：'+str(jgczsj))
                if jgczsj >= 10:
                    logger.info('警告重置')
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
            websocket.enableTrace(True,level='INFO')
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
        logger.error("出错，这可能导致连接断开并重启")
        postreturn=fanbookbotapi.sendmessage(lingpai,chatid=545093460387282944,text="发生异常:\n"+str(traceback.format_exc())+"\n尝试次数:"+str(b)+"/30\n尝试重新启动...",type='text')
        print(postreturn.text)
        sentrytool({"e":str(traceback.format_exc()).replace('\n', '')},"error")
        logger.warning("尝试重新启动...")
        continue

logger.critical("出错次数超过30次，程序终止")
input("按回车退出")
