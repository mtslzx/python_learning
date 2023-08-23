# 3448번: 문자 인식 - <img src="https://static.solved.ac/tier_small/5.svg" style="height:20px" /> Bronze I

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-31256KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-44ms-informational?style=flat-square)

구현 자체는 간단해 보이는데 정답률이 낮은 건... 뭔가 함정이 있을 듯.
빈 줄이 있을 때까지 입력받고 문자열에서 #가 몇 개 있는지와 전체 문자열의 길이를 구한 다음 계산해서 출력하면 될 것 같다.
다만 공백문자도 인식된 문자인지 알아야 할 것 같다.

한 번에 성공했다..! 공백문자도 문자열의 일부로 포함했어야 하는 듯.
여러 줄을 입력받는 부분에서 문자열을 합칠 때

The i#put consists of N test ca#es. The number... 가 아닌
The i#put consists ofN test ca#es. The number... 처럼 다음 줄을 띄워주지 않고 붙여주었다.

개인적으로 이번에 작성한 코드가 매우 짧고 간결해서 만족한다!
round() 함수를 사용하지 않고 f-string을 통해 출력한 부분도 나름 좋다고 생각한다.

숏코딩 순위에도 올라갔다~~!

<!-- end -->

## 문제

[문제 링크](https://boj.kr/3448)


<p>동혁이는 새로운 이미지 문자 인식 프로그램을 만들었다. 이 프로그램은 종이에 쓰여 있는 글자를 스캔한 뒤, 텍스트 파일로 저장한다. 동혁이는 밤을 새며 열심히 프로그램을 만들었지만, 프로그램의 신뢰도는 100%가 아니며, 어떤 글자는 인식하지 못했다. 결국 동혁이는 100%가 아니라는 점에서 실망하였고, 대전으로 도망가게 되었다.</p>

<p>대전으로 도망가버린 동혁이를 대신해서, 동혁이가 만든 이미지 문자 인식 프로그램의 인식률을 계산하는 프로그램을 작성하시오.</p>

<p>인식률은 인식한 문자의 수를 R, 전체 문자의 수를 A라고 했을 때, R/A이다. 줄바꿈 문자는 문자로 세지 않는다.</p>



## 입력

입력은 N개의 테스트 케이스로 구성되어 있다. 첫째 줄에 테스트 케이스의 개수 N이 주어진다. 각 테스트 케이스는 적어도 한 줄이고, 인식하지 못한 문자는 '#'로 표시한다. 각 테스트 케이스의 다음에는 빈 줄이 한 칸씩 있다. 각 줄은 100글자를 넘지 않고, 줄의 수도 200줄을 넘지 않는다.

## 출력

각 테스트 케이스에 대해서 인식률을 계산한 뒤 다음과 같이 출력한다. 각 줄은 "Efficiency ratio is X%."와 같은 형태로 출력해야 한다. X는 인식률을 퍼센트로 표시한 것이고, 소수점 두자리 이상인 경우에는 둘째 자리에서 반올림해서 출력한다.&nbsp;단, 반올림 결과가 정수이면 정수 부분만 출력한다.

## 소스코드

[소스코드 보기](문자%20인식.py)