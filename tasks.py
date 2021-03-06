from microsoftbotframework import ReplyToActivity
import requests
import json
import socket 

def echo_response(message):
  print(message)
  user_id = ''
  send_msg = ''
  if message["type"] == "message":
    user_id = message["from"]["id"]
    send_msg = message["text"] +"|"+ user_id
    s = socket.socket()
#     host = '13.125.9.203'
    host = '222.106.22.63'
    port = 12222

    s.connect((host, port))
    print('Connected to', host)

    s.send(send_msg.encode('utf-8'))
    # Halts
    print('[Waiting for response...]')
    recv_msg = s.recv(4096).decode('utf-8')
    print(recv_msg)
    s.close()
    ReplyToActivity(fill=message, text=recv_msg).send()
#     if "카드" in message["text"]:
#       print(message["from"]["id"])  
#       msg = "카드 서비스 준비 중 입니다."
#     elif "비교" in message["text"]:
#       msg = "비교 서비스 준비 중 입니다."
#     elif "안녕" in message["text"]:
#       msg = "안녕하세요."
#     else:
#       msg = "응답할 수 없음"
  elif message["type"] == "conversationUpdate":
    if "card_bot_test" in message["membersAdded"][0]["id"]: 
      send_msg = "카드 추천 챗봇 입니다.\n\n아래와 같은 형식으로 입력해주세요.\n\n▶ 하나 신용/체크카드 추천해줘\n\n▶ 나한테 맞는 카드 추천해줘\n\n▶ 내 카드/○○카드 혜택 알려줘\n\n▶ ◇◇카드랑 △△카드 비교해줘\n"
      ReplyToActivity(fill=message, text=send_msg).send()
    else:
      pass
    
  
