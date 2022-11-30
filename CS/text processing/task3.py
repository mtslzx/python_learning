

with open("./weather.html", 'r', encoding='UTF-8') as f:
    html = f.read()
    html_splited = html.split('<!-- 테이블2 -->')[1].split('<!-- 기온변화 -->')[0]
    j = 0
    for i in range(1, 6):
        date = html_splited.split('<th scope="row">')[i]  # scope="row"인 부분을 기준으로 나눔
        date = date.split('<span>')[1].split('</span>')[0]  # 나눈 라인에서 span 태그 찾기
        date = date.replace('(', '').replace(')', '')  # 출력을 위해 괄호 정리
        lowTemp = html_splited.split('<span class="temp">')[j+1].split('</span')[0]  # class="temp" 인 부분을 기준으로 나눔
        highTemp = html_splited.split('<span class="temp">')[j+2].split('</span>')[0]  # class="temp" 인 부분을 기준으로 나눔
        if int(lowTemp) < 10:
            lowTemp = ' ' + lowTemp
        print(f"{date} : {lowTemp} ~ {highTemp}")  # 서식화
        j += 2
    
    
    
    



