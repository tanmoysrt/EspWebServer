import requests

ENDPOINT = "https://www.fast2sms.com/dev/bulkV2"
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def sendSms(guardian_phone_no, message):
    request_url = f"{ENDPOINT}?authorization={API_KEY}&route=v3&sender_id=TXTIND&message_text={message}&language=english&numbers={guardian_phone_no}"
    req = requests.get(request_url)
    print(f"{req}")