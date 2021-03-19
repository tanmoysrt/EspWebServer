import requests
import asyncio

ENDPOINT = "https://www.fast2sms.com/dev/bulkV2"
API_KEY = "yvQzOrxVlRi5u1NkKjHD4owgp2SZYA9sfch3BFnbt0LeqJUda88dbCc4psDgJLBvPMSiV53n9Wj2aKNG"

def sendSms(guardian_phone_no, message):
    request_url = f"{ENDPOINT}?authorization={API_KEY}&route=v3&sender_id=TXTIND&message_text={message}&language=english&numbers={guardian_phone_no}"
    req = requests.get(request_url)
    print(f"{req}")