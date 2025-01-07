import json
import urllib.request
import os
import random

def lambda_handler(event, context):
    # TODO implement
    
    motivationalQuates = [
        "今日も一日頑張ろう！",
        "挑戦することで成長がある！",
        "小さな一歩が大きな成果に繋がる！",
        "失敗を恐れず前進しよう！",
        "努力は必ず報われる！"
    ]
    motivationalQuate = random.choice(motivationalQuates)
    
    message = {
        
        "text": motivationalQuate
        
    }
    
    hdr = {'Content-Type': 'application/json; charset=utf-8'}
    
    req = urllib.request.Request(os.environ["MY_WEBHOOK"], json.dumps(message).encode('utf-8'), hdr)
    response = urllib.request.urlopen(req)
    response.read()
    
    return {
        'statusCode': 200,
    }
