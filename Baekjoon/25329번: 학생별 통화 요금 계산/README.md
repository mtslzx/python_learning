# 25329번: 학생별 통화 요금 계산 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Failed-critical?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-0KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-0ms-informational?style=flat-square)

어지저찌 그냥 풀고 있었는데 2%에서 바로 틀렸습니다..
예제는 다 맞는데 왜 틀리는건지 이해가 안되어서... 다시 풀어봐야할듯~ -23.09.04-

<!-- end -->

## 문제

[문제 링크](https://boj.kr/25329)


<p class="0" style="text-indent:1.2pt">학생들이 한 달간 통화한 <em>n</em>개의 통화 기록 <em>A</em>가 주어진다. 한 개의 통화 기록은 통화 시간과 학생 이름이 공백으로 구분되어 주어진다. 한 학생의 통화 기록이 여러 번 주어질 수 있다. 통화 시간은 시:분 형태로 주어지고 시와 분은 길이가 2인 문자열이다. 학생 이름은 알파벳 소문자로 이루어져 있다. 통화 요금표는 다음과 같다.</p>

<ul>
<li class="0" style="text-indent: 1.2pt;">기본 시간(분): 100분, 기본 요금(원): 10, 단위 시간(분): 50, 단위 요금(원): 3</li>
</ul>

<p class="0" style="text-indent: 1.2pt;">통화 요금은 학생별로 한 달간 통화한 누적 통화 시간에 대하여 청구된다. 누적 통화 시간이 기본 시간 이하라면 기본 요금이 청구된다. 누적 통화 시간이 기본 시간을 초과하면, 기본 요금에 더해서 초과한 시간에 대해서 단위 시간마다 단위 요금이 청구된다. 초과한 시간이 단위 시간으로 나누어떨어지지 않으면 올림 한다.</p>

<p class="0" style="text-indent: 1.2pt;">통화 요금이 많은 학생부터 이름과 통화 요금을 출력하자. 통화 요금이 같은 학생은 학생 이름 기준으로 오름차순으로 출력하자.</p>



## 입력

첫 번째 줄에 통화 기록의 개수 <em>n</em>이 주어진다.

## 출력

첫 번째 줄부터 통화 요금이 많은 학생부터 학생 이름과 통화 요금을 공백을 사이에 두고 순서대로 출력한다. 통화 요금이 같은 학생은 학생 이름 기준으로 오름차순으로 출력한다. 한 줄에 한 학생의 정보를 출력한다.

## 소스코드

[소스코드 보기](학생별%20통화%20요금%20계산.py)