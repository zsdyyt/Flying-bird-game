from django.shortcuts import render
from django.contrib.auth.models import User
import time
import serial
from dwebsocket import require_websocket
from dwebsocket.decorators import accept_websocket,require_websocket

#ser = serial.Serial( #下面这些参数根据情况修改
  #port='COM6',
  #baudrate=9600,
#)
clients = []

print('333')
firsta=[1,2,5,4]

def modify_message(message):
    return message.lower()


@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'index.html')
    else:
        for message in request.websocket:
            request.websocket.send(message)#发送消息到客户端

def echo_once(request):
  message = request.websocket.wait()
  request.websocket.send(message)

# Create your views here.
def hello(request):
  firsta=''
  #firsta=ser.read(3)
  #return render(request, 'index.html', {'firsta':firsta})
  while (firsta == ''):
    while (firsta != '1'):
      return render(request, 'demo.html')
      firsta=''
    else:
      firsta=''