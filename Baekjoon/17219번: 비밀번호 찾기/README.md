# 17219번: 비밀번호 찾기 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

문제를 천천히 읽다가 예제 입력을 보고 놀랬다!
문제를 출제한 사람이 유애나라 정말 마음에 드는 문제.. ㅋㅋ
무조건 풀어보도록 하자!

우선 시간초과를 고려하지 않고 그냥 마구잡이로 만들어보려고 한다.
사이트 주소와 비밀번호를 딕셔너리로 각각 키, 벨류로 저장한 다음, 주어지는 사이트 주소를 딕셔너리에서 직접 참조하거나 get() 메서드로 찾아내려고 한다.
우선 한번 부딪혀 보자.

생각보다 되게 간단한 문제여서 입력 방식마다 시간 차이가 얼마나 날까 궁금해서 테스트 해보기로 했다.

파이썬의 가장 기본적인 input()을 사용할 경우
-> ![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-49344KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-15184ms-informational?style=flat-square)

sys 모듈을 임포트해서 사용하는 sys.stdin을 사용할 경우
-> ![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-49176KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-224ms-informational?style=flat-square)

open(0)를 사용할 경우
-> 코드를 짜다가 실패했다.

예상치 못하게 엄청난 차이가 나서 당황했다. 모듈을 임포트 해서 메모리 사용량이 더 클 것이라 예상했으나 적지만 메모리를 덜 사용한 모습을 볼 수 있었고, 시간에서 엄청난 차이를 보였는데 무려 65배 가까이 빨라진 모습이다...

앞으로 알고리즘 문제를 풀거나 할 때는 sys.stdin을 사용하거나 open(0)을 연구해 보아야겠다.

from sys import stdin
input = stdin.readline
로 input을 대체해버리는 경우도 있다.


<!-- end -->

## 문제

[문제 링크](https://boj.kr/17219)


<p>2019 HEPC - MAVEN League의 "<a href="/problem/17218">비밀번호 만들기</a>"와 같은 방식으로 비밀번호를 만든 경민이는 한 가지 문제점을 발견하였다. 비밀번호가 랜덤으로 만들어져서 기억을 못 한다는 것이었다! 그래서 경민이는 메모장에 사이트의 주소와 비밀번호를 저장해두기로 했다. 하지만 컴맹인 경민이는 메모장에서 찾기 기능을 활용하지 못하고&nbsp;직접 눈으로 사이트의 주소와 비밀번호를 찾았다. 메모장에 저장된 사이트의 수가 늘어나면서&nbsp;경민이는 비밀번호를 찾는 일에 시간을 너무 많이 쓰게 되었다. 이를 딱하게 여긴 문석이는 경민이를 위해 메모장에서 비밀번호를 찾는 프로그램을 만들기로 결심하였다! 문석이를 도와 경민이의 메모장에서 비밀번호를 찾아주는 프로그램을 만들어보자.</p>



## 입력

첫째 줄에 저장된 사이트 주소의 수 N(1&nbsp;≤ N&nbsp;≤ 100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1&nbsp;≤ M&nbsp;≤ 100,000)이 주어진다.

## 출력

첫 번째 줄부터 M개의 줄에 걸쳐&nbsp;비밀번호를 찾으려는 사이트 주소의 비밀번호를 차례대로 각 줄에 하나씩 출력한다.

## 소스코드

[소스코드 보기](비밀번호%20찾기.py)