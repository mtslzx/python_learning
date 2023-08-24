# 2422번: 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 - <img src="https://static.solved.ac/tier_small/7.svg" style="height:20px" /> Silver IV

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Failed-critical?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-0KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-0ms-informational?style=flat-square)

경우의 수를 구하기만 하면 되므로, 모든 섞어먹는 경우의 수를 구한 다음. 섞어먹으면 안되는 조합의 경우의 수를 구해서 빼주면 될 것 같다. 는... 조금 힘들어졌다. 다시 도전할 예정 - 23.08.24


<!-- end -->

## 문제

[문제 링크](https://boj.kr/2422)


<p>한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다. 아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다. 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때, 선택하는 방법이 몇 가지인지 구하려고 한다.</p>



## 입력

첫째 줄에 정수 N과 M이 주어진다. N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수이다. 아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다. 같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

## 출력

첫째 줄에, 가능한 방법이 총 몇 개 있는지 출력한다.

## 소스코드

[소스코드 보기](한윤정이%20이탈리아에%20가서%20아이스크림을%20사먹는데.py)