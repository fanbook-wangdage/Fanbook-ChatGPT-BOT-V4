from flask import Flask, request, render_template
import requests
import sentry_sdk
import ctypes
import json

# 获取控制台窗口句柄
kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()

# 设置窗口标题
if hwnd != 0:
    kernel32.SetConsoleTitleW("api终端进程-1")


sentry_sdk.init(
    dsn="https://c894d75b8b27de0eedce33e01eedd443@o4506008195956736.ingest.sentry.io/4506008631771136",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


app = Flask(__name__)

@app.route('/loaderio-439a96a9294f8d3fb921f0a547ed9fd2/',methods=['GET'])
def lo():
    return 'loaderio-439a96a9294f8d3fb921f0a547ed9fd2'

@app.route('/api/jb', methods=['GET', 'POST'])
def jb():
    code = request.args.get('code')
    try:
        state=request.args.get('state')
        print(state)
        state=state.split('-')
        pdid=state[0]
        xxid=state[1]
        fwqid=state[2]
        fsz=state[3]
        glpd=state[4]
        code = request.args.get('code')
        param2 = request.args.get('pa')
        x=0
    except:
        x=1
    # 定义请求参数
    token_url = "https://a1.fanbook.mobi/open/oauth2/token"
    redirect_uri = "http://1.117.76.68:5000/api/jb"

    # 构建请求头
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic NDU2NDQyODE4ODgyMzEwMTQ0OmdIdEsyTnhoR2EwWlUw"
    }

    # 构建请求体参数
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }

    # 发送POST请求获取访问令牌
    response = requests.post(token_url, headers=headers, data=data)
    lp=response.text
    print(response.text)

    # 解析响应
    if response.status_code == 200:
        token_data = response.json()
    # 在实际应用中，你可以根据参数执行特定的操作
    # 这里只是将参数返回为JSON响应
        response_data = {
            'param1': code
        }
        url="https://a1.fanbook.mobi/open/api/user/getMe"
        headers = {
            "content-type": "application/json",
            "authorization": "Basic "+token_data["access_token"]
        }
        response = requests.post(url, headers=headers)
        print(response.text)
        user_data = response.json()
        print(user_data)
    if x==0:
        lingpai='b27c98a520500c7c0b5f37ee7575b97228baacac1e55cf5c4b5'
        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
        headers = {'content-type':"application/json;charset=utf-8"}
        jsonfile=json.dumps({
        "chat_id":int(glpd),
        "text":"匿名消息-举报消息\n消息id："+str(xxid)+"\n举报用户："+user_data["data"]["nickname"]+"("+user_data["data"]["username"]+')'+'\n发送者：'+fsz+'\n请前往：'+'${#'+str(pdid)+'} 查看消息'
        })
        print(jsonfile)
        postreturn=requests.post(url,data=jsonfile,headers=headers)
        return '举报成功，感谢您的举报，已通知此服务器的管理员，此服务器的管理员会尽快处理！'
    else:
        return str(user_data)+str(lp)
@app.route('/api/get_data1', methods=['GET'])
def get_data1():
    # 使用 request.args.get() 方法获取参数
    code = request.args.get('code')
    param2 = request.args.get('pa')
    # 定义请求参数
    token_url = "https://a1.fanbook.mobi/open/oauth2/token"
    client_id = "469787616032722944"
    client_secret = "ZlrcdBpdRmXSRg8RFcrWEpVhMPTB7ACD"
    redirect_uri = "http://1.117.76.68:5000/api/get_data1"

    # 构建请求头
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic NDY5Nzg3NjE2MDMyNzIyOTQ0OFJGY3JXRXBWa1QVEI3QUNE"
    }

    # 构建请求体参数
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }

    # 发送POST请求获取访问令牌
    response = requests.post(token_url, headers=headers, data=data)

    print(response.text)

    # 解析响应
    if response.status_code == 200:
        token_data = response.json()
    # 在实际应用中，你可以根据参数执行特定的操作
    # 这里只是将参数返回为JSON响应
        response_data = {
            'param1': code,
            'param2': param2
        }
        url="https://a1.fanbook.mobi/open/api/user/getMe"
        headers = {
            "content-type": "application/json",
            "authorization": "Basic "+token_data["access_token"]
        }
        response = requests.post(url, headers=headers)
        print(response.text)
        user_data = response.json()
        print(user_data)
        xxjl=[]
        xxfsz=[]
        xxfszid=[]
        allfwq=False
        idlb=['4562997','372940','13134203','13096018','8928358','6791872','1363608','13633669']
        fwqiflb=[["all"],["532781465822687232"],["516495988547244032"],["487208151620640770"],["543395863498969088"],["436335527214448640"],["285257797744984064"],["550104861367447552"]]
        fwqlb=""
        text=""
        a="""
"""
        if user_data["data"]["username"] in idlb:
            b=0
            with open('xxfszid.txt', 'r',encoding="utf-8") as file:
                b=0
                c=[]
                for line in file:
                    # 删除行尾的换行符
                    item = str(line.strip())
                    print(item)
                    print(item[32:])
                    if str(item[32:]) in fwqiflb[idlb.index(user_data["data"]["username"])] or fwqiflb[idlb.index(user_data["data"]["username"])][0] == "all":
                        xxfszid.append(item)
                        c.append(b)
                    b+=1
            with open('xxjl.txt', 'r',encoding="utf-8") as file:
                b=0
                for line in file:
                    # 删除行尾的换行符
                    item = str(line.strip())
                    if b in c:
                        xxjl.append(item)
                    b+=1
            with open('xxfsz.txt', 'r',encoding="utf-8") as file:
                b=0
                for line in file:
                    # 删除行尾的换行符
                    item = str(line.strip())
                    if b in c:
                        xxfsz.append(item)
                    b+=1
            # 打印加载的列表
            print(xxjl,xxfszid,xxfsz)
            for i in range(len(xxjl)):
                text+=a+xxjl[i]+a+xxfsz[i]+a+xxfszid[i]
            if fwqiflb[idlb.index(user_data["data"]["username"])][0] == "all":
                 fwqlb="以下是所有服务器的回复记录"   
            else:
                fwqlb="以下是服务器id:"+str(fwqiflb[idlb.index(user_data["data"]["username"])])+"的回复记录"
        else:
            text="抱歉，你可能没有权限访问此内容，如果你是拥有ChatGPT的服务器主，请联系id:4562997"
        return render_template('index.html', name=text,username=user_data["data"]["nickname"],userdid=user_data["data"]["username"],fwqlb=fwqlb)

    else:
        return '失败，请重新验证'+str(response.status_code)+response.text

@app.route('/api/get_data_test', methods=['GET'])
def get_data():
    # 创建空列表
    xxjl = []
    xxfsz=[]
    xxfszid=[]
    text=''
    a="""
"""
    # 从文件读取列表
    with open('xxjl.txt', 'r',encoding="utf-8") as file:
        for line in file:
            # 删除行尾的换行符
            item = str(line.strip())
            xxjl.append(item)
    with open('xxfsz.txt', 'r',encoding="utf-8") as file:
        for line in file:
            # 删除行尾的换行符
            item = str(line.strip())
            xxfsz.append(item)
    with open('xxfszid.txt', 'r',encoding="utf-8") as file:
        for line in file:
            # 删除行尾的换行符
            item = str(line.strip())
            xxfszid.append(item)
    # 打印加载的列表
    print(xxjl,xxfszid,xxfsz)
    for i in range(len(xxjl)):
        text+=a+xxjl[i]+a+xxfsz[i]+a+xxfszid[i]
    return render_template('index.html', name=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

