# 14726번: 신용카드 판별 - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-31256KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-40ms-informational?style=flat-square)

공식이 주어진 문제이므로! 공식만 구현하면 쉽게 통과할 것 같다.

<!-- end -->

## 문제

[문제 링크](https://boj.kr/14726)


<p>신용카드는 총 16자리의 숫자로 구성되어 있다. 언뜻 보기에는 무작위로 된 숫자로 구성되어 있는 것 같이 보이지만 그 속에는 하나의 수학적 비밀이 숨겨져 있다. 그중 하나가 카드 번호가 유효 한지 유효하지 않은 지 검사하는 Luhn 공식이다. 그 공식은 다음과 같다.</p>

<ol>
<li>신용카드의 16자리 숫자에서 맨 우측 수부터 세어 홀수 번째 수는 그대로 두고, 짝수 번째 수를 2배로 만든다.</li>
<li>2배로 만든 짝수 번째 수가 10 이상인 경우, 각 자리의 숫자를 더하고 그 수로 대체한다.</li>
<li>이와 같이 얻은 모든 자리의 수를 더한다.</li>
<li>그 합이 10으로 나뉘면 “정당한 번호”(유효)이고 그렇지 않으면 “부당한 번호”(유효하지 않음)로 판정된다.</li>
</ol>

<p>다음 공식을 이용해 주어진 신용카드의 번호가 유효한지, 유효하지 않은 지 판단해라.</p>



## 입력

첫째 줄에 테스트 케이스의 수 T(1 ≤ T ≤ 1000)이 주어진다.

## 출력

신용카드의 번호가 유효하면 “T”, 유효하지 않으면 “F”를 한 줄 씩 출력한다.

## 소스코드

[소스코드 보기](신용카드%20판별.py)