import time
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup


def hostloc():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    sess = requests.session()
    sess.headers = headers

    login_data = {
        'fastloginfield': 'username',
        'username': 'Roo00kie',
        'password': '642078995abcABC!',
        'quickforward': 'yes!',
        'handlekey': 'ls!',
    }
    sess.post(
        url='https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1',
        data=login_data)

    r_forum = sess.get(url='https://www.hostloc.com/forum.php')
    if 'Roo00kie' in r_forum.text:
        print('hostloc_points login success')
    soup = BeautifulSoup(r_forum.text, 'html.parser')
    points0 = soup.find('a', attrs={'id': 'extcreditmenu'}).get_text().split(': ')[1]

    space_uids = ['42279', '41800', '41801', '41802', '41803',
                  '41804', '42200', '42201', '42202', '42203']

    for space_uid in space_uids:
        url = 'https://www.hostloc.com/space-uid-' + space_uid + '.html'
        sess.get(url)
        time.sleep(2)

    r_forum = sess.get(url='https://www.hostloc.com/forum.php')
    soup = BeautifulSoup(r_forum.text, 'html.parser')
    points1 = soup.find('a', attrs={'id': 'extcreditmenu'}).get_text().split(': ')[1]

    print('points : {} to {}'.format(points0, points1))
    print('\n')
    print('______________________________')
    print('\n')


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(hostloc, 'interval', hours=8)
    scheduler.start()