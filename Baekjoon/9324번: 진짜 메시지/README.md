# 9324번: 진짜 메시지 - <img src="https://static.solved.ac/tier_small/6.svg" style="height:20px" /> Silver V

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-33444KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-448ms-informational?style=flat-square)


문제의 설명이 조금 이해하기 어려웠는데, "각 문자가 세 번째 등장할 때 한 번 더 문자가 삽입된다." 가 제일 중요한 부분이다.
만약, AAAAAAA 라는 문자열이 있다면, 출력은 AAA*A*AAA*A*A 이 된다. 굵게 표시된 문자는 한 번 더 삽입된 문자다.
이 부분을 구현하면 되는 문제이고, 최대 10만자가 주어질 것이므로 시간 효율성을 추구해야 한다.

코드를 짜면서 갈팡질팡 하다보니 굉장히 보기 난해한 코드가 되어버렸다.
간단히 모든 문자열을 확인한 후 카운트를 세며 각 문자가 3번째 등장한 경우 그 다음 문자가 동일한 문자인지 확인하는 코드이다. 


<!-- end -->

## 문제

[문제 링크](https://boj.kr/9324)


<p>스파이들은 사령부와 통신하기 위해서 SMTP(비밀 메시지 전송&nbsp;프로토콜)를 사용해 비밀 회선으로 전자 메시지를 보낸다. 메시지가 적들에 의해 조작되어&nbsp;보내진 것이 아닌 진짜 메시지라는 것을 표시하기 위해 모든 메시지는 회선에 노이즈가 있었거나 발신&nbsp;측에서 손을 떨면서 메시지를 보낸&nbsp;것처럼 변형되는데,&nbsp;이 변형 알고리즘은 메시지를 가로채는 자들이 우연히&nbsp;변형&nbsp;규칙을&nbsp;흉내&nbsp;낼 수 없을 정도로 정교하다. 또한 요원들의 머리에 총구가 겨눠져 강제로 메시지를 말한 경우 간단히&nbsp;실수를 의도적으로 넣어 이 메시지가 강제로 쓰인 메시지라는 것을 알려줄 수 있다.</p>

<p>알고리즘대로 정확하게 변형된 메시지는 각 문자가 세 번째 등장할 때 한 번 더 문자가 삽입된다. 예를 들면 요원이 "<code>HELLOTHEREWELLBEFINE</code>" 라는 메시지를 보내고 싶어&nbsp;했다면 "<code>HELLOTHEREEWELLLBEFINEE</code>" 는 정확한 변형이다. 몇&nbsp;년 동안 이 메시지들의 진짜 여부는 고도로 훈련된 원숭이들이 판별해내었다. 그러나 사령부에 도착하는 메시지들의 양이 많이 늘어나면서 이 작업을 자동으로 처리해주는 프로그램을 고안하기로 하였다.</p>



## 입력

첫째 줄에 100 이하의 테스트 케이스의 개수가 주어진다. 그리고 각 테스트 케이스마다 대문자로만 이루어진 10만자 이하의 문자열 M이 한 줄에 주어진다. 이 문자열은 검사해야할 메시지다.

## 출력

테스트 케이스마다 메시지 M이 진짜 메시지면 “OK”를, 가짜 메시지면 “FAKE”를 한 줄에 출력한다.

## 소스코드

[소스코드 보기](진짜%20메시지.py)