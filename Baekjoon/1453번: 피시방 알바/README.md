# 1453번: 피시방 알바 - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-34104KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-80ms-informational?style=flat-square)![](https://img.shields.io/badge/Code_Length-45_Byte-goodt?style=flat-square)

파이썬 한정..? 쉬운 문제. 각 손님이 앉고 싶어 하는 자리는 먼저 온 사람이 선점하면 앉을 수 없으므로 각 손님이 앉고 싶어하는 자리들 중 중복되는 값을 제외한다.
이렇게 되면 늦게와서 원하는 자리를 잡지 못하는 손님이 빠졌으므로, 총 손님의 수 N에서 현재 앉아있는 (먼저 자리를 선점한) 손님의 수를 빼주면 거절당한 손님의 수를 얻을 수 있다.

45B의 코드 길이로 문제를 해결했다!

<!-- end -->

## 문제

[문제 링크](https://boj.kr/1453)


<p>세준이는 피시방에서 아르바이트를 한다. 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.</p>

<p>들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고싶어한다. 따라서 들어오면서 번호를 말한다. 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절당한다.</p>

<p>거절당하는 사람의 수를 출력하는 프로그램을 작성하시오. 자리는 맨 처음에 모두 비어있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.</p>



## 입력

첫째 줄에 손님의 수 N이 주어진다. N은 100보다 작거나 같다. 둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리가 입력으로 주어진다.

## 출력

첫째 줄에 거절당하는 사람의 수를 출력한다.

## 소스코드

[소스코드 보기](피시방%20알바.py)