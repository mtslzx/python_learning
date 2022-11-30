from bs4 import BeautifulSoup

with open("./weather.html", 'r', encoding='UTF-8') as f:
    html = BeautifulSoup(open('weather.html').read(), "html.parser")  # bs4로 html 파싱
    table = html.find_all('table', class_='tbl_weather tbl_today4')
    th_scope = table[0].find_all('th', scope='row')
    temps = table[0].find_all('span', class_='temp')
    j = 0  # 온도가 한 리스트에 다 있으므로 구분을 위한 카운터
    for i in range(len(th_scope)):
        date = th_scope[i].find_all('span')  # 날짜 추출
        date = date[0].text.replace('(', '').replace(')', '')  # 날짜에서 괄호 제거
        lowTemp = temps[j].text  # 오전온도 추출
        highTemp = temps[j + 1].text  # 오후온도 추출
        j += 2  # 2개씩 리스트에서 추출하므로 2씩 증가
        print(f"{date} : {lowTemp} ~ {highTemp}")




