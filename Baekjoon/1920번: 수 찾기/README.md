# 1920번: 수 찾기 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Failed-critical?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-0KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-0ms-informational?style=flat-square)

이건 무조건... 일반적으로 풀면 시간초과가 날 것 같다.
하지만 그냥 어떤 값이 주어지던 존재하는지 아닌지만 알아내면 되는 것 아닌가?
처음 받은 정수들을 set 자료형으로 중복을 없애버리고 두번째 정수들에서 in 을 통해 존재하는지 유무로 값을 출력하면 될 것 같다. 출력초과... 로 실패 - 23/08/16

<!-- end -->

## 문제

[문제 링크](https://boj.kr/1920)


<p>N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.</p>



## 입력

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2<sup>31</sup> 보다 크거나 같고 2<sup>31</sup>보다 작다.

## 출력

M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

## 소스코드

[소스코드 보기](수%20찾기.py)