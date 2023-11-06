"""
Author: Bisnu Ray
Telegram: https://t.me/SmartBisnuBio
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
import random as R, string as S, json as C, requests as T, re

# Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token
API_TOKEN = 'IHUREIUHRUHIRIUGRE'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# BardBot initialization...
V = 'HFDEBIRBOGJNBOTHGY67Y' #__Secure-1PSID Key
W = 'ERUFGVR4IUGTIYG5R4YTG' #__Secure-1PSIDTS


Q = 'utf-8'
P = False
O = 'https://bard.google.com/'
N = print
M = True
B = Exception
L = 'content'
K = 'conversation_name'
J = 'choice_id'
I = 'SNlM0e'
H = ''
G = None
F = '_reqid'
E = 'response_id'
D = 'conversation_id'

class color:
 def red(*args):
    return print("\033[0;31m" + ' '.join(args) + '\033[0m')

 def cyan(*args):
    return print("\033[0;36m" + ' '.join(args) + '\033[0m')


class BardBot:
        __slots__ = [
                'headers', F, I, D, E, J, 'proxy', 'secure_1psidts',
                'secure_1psid', 'session', 'timeout'
        ]

        def __init__(A, secure_1psid, secure_1psidts, proxy=G, timeout=20):
                D = proxy
                C = secure_1psid
                B = secure_1psidts
                E = {
                        'Host': 'bard.google.com',
                        'X-Same-Domain': '1',
                        'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                        'Content-Type':
                        'application/x-www-form-urlencoded;charset=UTF-8',
                        'Origin': 'https://bard.google.com',
                        'Referer': O
                }
                A._reqid = int(H.join(R.choices(S.digits, k=4)))
                A.proxy = D
                A.conversation_id = H
                A.response_id = H
                A.choice_id = H
                A.secure_1psid = C
                A.secure_1psidts = B
                A.session = T.session()
                A.session.headers = E
                A.session.proxies = D
                A.session.cookies.set('__Secure-1PSID', C)
                if B: A.session.cookies.set('__Secure-1PSIDTS', B)
                A.timeout = timeout

        def __m0e(A):
                if not (A.secure_1psid and
                                A.secure_1psidts) or A.secure_1psid[-1] != '.':
                        raise B('cookieError: Invalid cookies provided')
                C = A.session.get(O, timeout=10, allow_redirects=M)
                if C.status_code != 200:
                        raise B(f"Invalid response: {C.status_code}")
                D = re.search('SNlM0e\\":\\"(.*?)\\"', C.text)
                if not D: raise B('cookieError: Get cookies from: bard.google.com (Must logged In)')
                return D.group(1)

        def ask(A, message):
                N = 'choices'
                O = {
                        'bl': 'boq_assistant-bard-web-server_20230713.13_p0',
                        F: str(A._reqid),
                        'rt': 'c'
                }
                P = [[message], G,
                     [A.conversation_id, A.response_id, A.choice_id]]
                Q = {
                        'f.req': C.dumps([G, C.dumps(P)]),
                        'at': A.__m0e()
                }
                J = A.session.post(
                        'https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
                        params=O,
                        data=Q,
                        timeout=A.timeout)
                K = C.loads(J.content.splitlines()[3])[0][2]
                if not K: return {L: f"Unknown error: {J.text}."}
                B = C.loads(K)
                M = []
                if len(B) >= 3:
                        if len(B[4][0]) >= 4:
                                if B[4][0][4]:
                                        for R in B[4][0][4]:
                                                M.append(R[0][0][0])
                I = {
                        L: B[4][0][1][0],
                        D: B[1][0],
                        E: B[1][1],
                        'factualityQueries': B[3],
                        'textQuery': B[2][0] if B[2] is not G else H,
                        N: [{
                                'id': A[0],
                                L: A[1]
                        } for A in B[4]],
                        'images': M
                }
                A.conversation_id = I[D]
                A.response_id = I[E]
                A.choice_id = I[N][0]['id']
                A._reqid += 100000
                return I
                
bard = BardBot(V, W)

@dp.message_handler(commands=['bard'])
async def handle_bard_command(message: types.Message):
    query = message.text[6:].strip()
    if not query:
        await message.answer("<b>Please provide a Prompt after /bard</b>", parse_mode="HTML")
        return
    loading_msg = await message.answer("<b>Please wait for Bard response...</b>", parse_mode="HTML")

    try:
        bard_response = bard.ask(query)
        await loading_msg.delete()
        await message.answer(f"[Google Bard -> {bard_response['content']} ]", parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        await loading_msg.delete()
        await message.answer(f"<b>Sorry ! Bro Something Wrong : {e}</b>", parse_mode="HTML")


async def handle_empty_bard_command(message):
    await message.answer("<b>Please provide a query after /bard</b>", parse_mode="HTML")

if __name__ == '__main__':
    # Start the bot
    executor.start_polling(dp, skip_updates=True)
