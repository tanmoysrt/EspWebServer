#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal_I2C.h>


#define SS_PIN 16 
#define RST_PIN 2 



MFRC522 mfrc522(SS_PIN, RST_PIN);
LiquidCrystal_I2C lcd(0x3F, 16, 2);


int statuss = 0;
int out = 0;
String endpoint = "http://XXXXXXXXXXXXX/api/verify/";
String api_key = "a46a3aca882111ebbb326fdda74a51ce";
String content = "";

void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Connecting To");
  lcd.setCursor(0, 1);
  lcd.print("WIFI....");
  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }
  WiFi.mode(WIFI_OFF);
  WiFi.mode(WIFI_STA);
  WiFi.begin("XXXXXXXXXX", "XXXXXXXXXx");
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Connected....");
  delay(1000);
  SPI.begin();
  mfrc522.PCD_Init();
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print("READY");
}


void loop()
{
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print("READY");
  if ( ! mfrc522.PICC_IsNewCardPresent())
  {
    content = "";
    return;
  }
  if ( ! mfrc522.PICC_ReadCardSerial())
  {
    content = "";
    return;
  }
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print("Card");
  lcd.setCursor(3, 1);
  lcd.print("Accepted");
  Serial.println();
  Serial.print(" UID tag :");
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println(content.substring(1));
  HTTPClient http;
  String postData = "api_key=" + api_key + "&card_id=" + content.substring(1);
  http.begin(endpoint);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  int httpCode = http.POST(postData);
  String payload = http.getString();
  Serial.println(httpCode);
  Serial.println(payload);
  if(httpCode == 200){
    if(payload != "FAILED"){
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(payload);
        lcd.setCursor(2, 1);
        lcd.print("-- DONE --");
    }
    else{
        lcd.clear();
        lcd.setCursor(4, 0);
        lcd.print("FAILED");
        lcd.setCursor(5, 1);
        lcd.print("RETRY");
    }
  }
  delay(2000);
  
  http.end();

}
