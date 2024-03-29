# 1181번: 단어 정렬 - <img src="https://static.solved.ac/tier_small/6.svg" style="height:20px" /> Silver V

<!-- performance -->
![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-33708KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-916ms-informational?style=flat-square)

우선 조건을 살펴보면,
1. 길이가 짧은 순으로는 각 단어의 길이를 len() 함수로 계산해 .sort()로 정렬하면 간단하게 해결될 것이다..
2. 길이가 같으면 사전 순으로는 .sort()를 쓰면 해결될 것 같다.

[딕셔너리 자료형 정리](https://blockdmask.tistory.com/450)를 통해 딕셔너리 자료형을 이해하였다.
딕셔너리를 하나 만들어 키 값에 모든 단어를 집어넣고 벨류값으로 단어의 길이를 몽땅 넣을 생각이다.
그런다음 벨류값만 뽑아낸 리스트를 통해 set 자료형을 만들어 중복값을 없애고, 정렬시킨다음
그 리스트로 for문을 돌려 중복된 값들끼리 sort를 진행할 예정이다. 이렇게 진행한다면, 2번 조건을 만족시키며, for문이 오름차순으로 진행되므로 문자열이 제일 작은 단어부터 print 되므로 자연스럽게 1번 조건 해결이다.


<!-- end -->

## 문제

[문제 링크](https://boj.kr/1181)


<p>알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.</p>

<ol>
<li>길이가 짧은 것부터</li>
<li>길이가 같으면 사전 순으로</li>
</ol>

<p>단, 중복된 단어는 하나만 남기고 제거해야 한다.</p>



## 입력

첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

## 출력

조건에 따라 정렬하여 단어들을 출력한다.

## 소스코드

[소스코드 보기](단어%20정렬.py)
