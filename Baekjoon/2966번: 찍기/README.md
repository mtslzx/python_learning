# 2966번: 찍기 - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-34144KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-64ms-informational?style=flat-square)

간단한 구현 문제인것 같은데... 반복문으로 해결하려고 생각중이다. 문제의 수가 최대 100개라서 반복문과 if문으로 해결이 가능할 것 같다.

if문으로 노가다 하다... 갑자기 엄청난 생각이 들었다. deque 자료형에는 rotate라는 기능이 있는데, 이걸 이용하면 반복되는 패턴을 구현할 수 있으므로, 바로 버리고 덱을 사용해서 코드를 짰다.

마지막 출력부분을 좀 더 깔끔하게 만들고 싶었는데 시간이 없어서.. 그냥 if문 여러개 썼다...

<!-- end -->

## 문제

[문제 링크](https://boj.kr/2966)


<p>상근이, 창영이, 현진이는 역사와 전통을 자랑하는 Sogang ACM-ICPC Team에 가입하려고 한다. 하지만, 가입하려고 하는 모든 지원자는 C언어 필기시험을 통과해야 한다. 이들은 C언어를 할 줄 모른다. 따라서, 필기시험을 모두 찍으려고 한다.</p>

<p>상근이는 A, B, C, A, B, C, A, B, C, A, B, C, ...와 같이 찍어야 통과할 수 있다고 생각한다.&nbsp;</p>

<p>하지만, 창영이는 B, A, B, C, B, A, B, C, B, A, B, C, ...와 같이 찍는 방법이 만점의 지름길이라고 생각한다.</p>

<p>마지막으로, 현진이는 상근이와 창영이를 비웃으면서 C, C, A, A, B, B, C, C, A, A, B, B, ...와 같이 찍어야 통과한다고 말했다.</p>

<p>필기시험의 정답이 주어졌을 때, 상근이, 창영이, 현진이 중에서 가장 많은 문제를 맞힌 사람이 누구인지 구하는 프로그램을 작성하시오.</p>



## 입력

첫째 줄에 필기시험의 문제의 수 N이 주어진다. (1 ≤ N ≤ 100)

## 출력

첫째 줄에 가장 많은 문제를 맞춘 사람이 몇 문제를 맞혔는지 출력한다.

## 소스코드

[소스코드 보기](찍기.py)