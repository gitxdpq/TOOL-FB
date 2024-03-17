# PHIÊN BẢN SHARE TẠI WEBSITE : GITHUB.COM/GITXDPQ
# KHÔNG ĐEM ĐI BÁN / SỬA CHỮA / ...
# HỔ TRỢ SUPPORT : Facebook.com/wuok.x.KashinKoji


___Admin___ = '___Admin___ = Dương Phú Quốc'
import requests,os
from pystyle import Write,Colors,Colorate,Anime,Center
from datetime import datetime
sos = []
list_id_groups = []
do = '\033[1;31m'
xanh_la = '\033[1;32m'
vang = '\033[1;33m'
xanh_bien = '\033[1;34m'
hong = '\033[1;35m'
luc_bao = '\033[1;36m'
trang = '\033[1;37m'
def gach():
    Write.Print('────────────────────────────────────────────────────────\n', Colors.yellow_to_red, interval = 0.0025)

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    ban = f'''
     -- SHARE TẠI WEBSITE: github.com/gitxdpq --
     -- Phiên Bản Free Và Suột Code No Encode --
   -- Copyright By {___Admin___}/ @Wuoc'sDev -- 
────────────────────────────────────────────────────────
'''
    banner = (Colorate.Horizontal(Colors.purple_to_red, ban))
    print(banner)
def out_groups(x,dem,cookie,id_ck,fb_dtsg,jazoest):
    id_groups_out = list_id_groups[x]
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-encoding': 'br',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.129", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '',
        'sec-ch-ua-platform': 'Windows',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'viewport-width': '631',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupCometLeaveForumMutation',
        'x-fb-lsd': 'Lu1C-MO2DQYSGnoSQK18UY',
    }

    data = {
        'av': id_ck,
        '__user': id_ck,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupCometLeaveForumMutation',
        'variables': '{"imageMediaType":"image/x-auto","input":{"attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,unexpected,1710651450305,177100,2361831622,,","group_id":"'+id_groups_out+'","actor_id":"'+id_ck+'","client_mutation_id":"3"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"ordering":["viewer_added"],"scale":1,"groupID":"'+id_groups_out+'","__relay_internal__pv__VideoPlayerRelayReplaceDashManifestWithPlaylistrelayprovider":false,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":false}',
        'server_timestamps': 'true',
        'doc_id': '7357194924394591',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    #print(response.json())
    try:
        check = response.json()['data']['leave_forum_group']['group']['id']
        print(f'{do}[{vang}{dem}{xanh_bien}] {hong}| {xanh_la}STT: {vang}{x} {hong}| {luc_bao}{datetime.now().strftime("%H:%M:%S")} {hong}| {vang}OUT GROUPS THÀNH CÔNG')
    except:
        print(f'{do}[{vang}{dem}{xanh_bien}] {hong}| {xanh_la}STT: {vang}{x} {hong}| {luc_bao}{datetime.now().strftime("%H:%M:%S")} {hong}| {do}OUT GROUPS THẤT BẠI')
def get_id_groups(cookie,id_ck,fb_dtsg,jazoest):
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-encoding': 'br',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    data = {
        'av': id_ck,
        '__user': id_ck,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupsCometJoinsRootQuery',
        'variables': '{"ordering":["viewer_added"],"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '6985470494844388',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    try:
        check = response.json() ['data']['viewer']['all_joined_groups']['tab_groups_list']['edges']
        return check
    except:
        return 'error'
def ___main___():
    logo()
    cookie = input(f'{trang}>>> {xanh_la}Nhập Cookie Acc Cầm Groups: {luc_bao}')
    Write.Print('Đang Check Live Cookie\r', Colors.yellow_to_red, interval = 0.0125)

    id_ck = cookie.split('c_user=')[1].split(';')[0]
    get_dt_ck = requests.get('https://mbasic.facebook.com/profile.php?='+id_ck, headers={'cookie':cookie}).text
    try:
        name_profile = get_dt_ck.split('<title>')[1].split('</title>')[0]
        fb_dtsg = get_dt_ck.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = get_dt_ck.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
        Write.Print('<SUCESS> Cookie Live !!!   \n', Colors.green_to_cyan, interval = 0.0125)
    except:
        Write.Print('<ERROR> Cookie Die, Vui Lòng Nhập Cookie Khác !\n', Colors.red, interval = 0.0125)
        quit()
    logo()
    Write.Print(f'Name Profile FaceBook: {name_profile}\n', Colors.purple_to_red, interval = 0.0035)
    gach()
    check_group = get_id_groups(cookie,id_ck,fb_dtsg,jazoest)
    dem_groups = 0
    for groups in check_group:
        id_group = groups['node']['id']
        name_group = groups['node']['name']
        print(f'{do}[{vang}{dem_groups}{xanh_bien}] {xanh_la}UID GROUPS: {vang}{id_group} {hong}| {xanh_la}NAME GROUPS: {vang}{name_group}')
        list_id_groups.append(id_group)
        dem_groups += 1
    gach()
    chon_id = input(f'{do}[{vang}</>{xanh_bien}] {hong}=> {xanh_la}Nhập Số {do}[{xanh_la}Vd: {vang}1+2+3+4 {hong}| {xanh_la}Chạy Hết Nhập {hong}"{vang}all{hong}"{do}]{xanh_la}: {luc_bao}')
    try:
        if chon_id != 'all' or 'All' or 'ALL':
            num = chon_id.split('+')
        #print(num)
            for add in num:
                sos.append(add)
        #print(sos)
    except:
        pass
    gach()
    dem = 0
    if chon_id.lower() == "all":
        for x in range(10000000):
            try:
                out_groups(x,dem,cookie,id_ck,fb_dtsg,jazoest)
                dem += 1
            except:
                print('Done !')
                break

    else:
        for x in sos:
            out_groups(int(x),dem,cookie,id_ck,fb_dtsg,jazoest)
            dem += 1


if ___Admin___ in requests.get('https://raw.githubusercontent.com/gitxdpq/TOOL-FB/main/out_groups.py').text: ___main___()
else: print('Out !'); quit()
