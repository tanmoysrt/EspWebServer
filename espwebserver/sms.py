import requests
from queue import Queue


ENDPOINT = "https://www.fast2sms.com/dev/bulkV2"
API_KEY = "yvQzOrxVlRi5u1NkKjHD4owgp2SZYA9sfch3BFnbt0LeqJUda88dbCc4psDgJLBvPMSiV53n9Wj2aKNG"


def sendSms(guardian_phone_no, message):
    request_url = f"{ENDPOINT}?authorization={API_KEY}&route=v3&sender_id=TXTIND&message_text={message}&language=english&numbers={guardian_phone_no}"
    req = requests.get(request_url)
    print(req)

queue = Queue(maxsize=100)
queue.put(lambda : sendSms("9333584419","First Sms"))
queue.put(lambda : sendSms("9333584419","Second Sms"))
queue.put(lambda : sendSms("9333584419","Third Sms"))


while True:
    f = queue.get()
    f()