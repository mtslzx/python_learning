# 10988번: 팰린드롬인지 확인하기 - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-34906KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-64ms-informational?style=flat-square)

1259번 팰린드롬수를 먼저 풀어버려서... 코드를 좀 우려먹으려고 한다..
출력부분만 바꾸고 바로 제출했더니 EOF 에러가 났다. 이 문제에서는 지속적으로 값을 입력받지 않아서 생긴 문제였다.
반복문을 제거하니 바로 정답!
한가지 신기한점은 1259번과 메모리 사용량이 동일하다..! 우연인가?

<!-- end -->

## 문제

[문제 링크](https://boj.kr/10988)


<p>알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.</p>

<p>팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.&nbsp;</p>

<p>level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.</p>



## 입력

첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

## 출력

첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

## 소스코드

[소스코드 보기](팰린드롬인지%20확인하기.py)