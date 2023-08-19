# 15813번: 너의 이름은 몇 점이니？ - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-31256KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-40ms-informational?style=flat-square)

모든 이름은 대문자 영어로 주어지므로, 이름을 모두 ASCII코드로 변환하면 간단해질 것이다.
ASCII코드 기준 A는 65이니 A를 1점으로 취급하기 위해서 문자를 ASCII코드로 변환 후 -64를 해주고, 이 값들을 전부 더하면 될 것 같다.


<!-- end -->

## 문제

[문제 링크](https://boj.kr/15813)


<p>소윤이는 성필이에게 단단히 화가 났다. 성필이가 자꾸 소윤이의 이름을 놀리는 것이다!</p>

<p>극대노한 소윤이는 이름에 대해 많은 검색을 하던 도중 "이름점수"라는 것을 발견하게 된다. 이름 점수란, 알파벳 하나하나에 점수가 있고 이름에 들어가는 모든 알파벳 점수를 합한 것이라고 한다. 예를 들어 이름이 <strong>SUNG PIL</strong> 이라면,</p>

<ul>
<li>A = 1점</li>
<li>B = 2점</li>
<li>C = 3점</li>
<li>...</li>
<li>Z = 26점</li>
</ul>

<p>인 점수판에 따라 <strong>S(19)+U(21) + N(14) + G(7) + P(16) + I(9) + L(12) = 98점</strong>이다. (즉, 점수는 알파벳 순서이다)&nbsp;</p>

<p>소윤이는 <strong>SO YOON</strong>이므로 <strong>S(19) + O(15) + Y(25) + O(15) + O(15) + N(14) = 103점</strong>으로 성필이보다 "이름점수"가 높았다! 그 사실을 알아챈 소윤이는 성필이에게 자신이 "이름점수"가 더 높다는 것을 전했고 성필이는 아직 충격에서 헤어나오지 못했다고 한다.</p>

<p>이제 소윤이는 사람의 이름을 볼 때 마다 "이름점수"를 계산해본다. 하지만 너무나 많은 사람을 만나기 때문에 계산하기가 귀찮다! 귀찮아진 소윤이를 위해 "이름점수"를 계산하는 프로그램을 만들어 주자.</p>



## 입력

첫 번째 줄에 이름의 길이가 주어진다. 길이는 100자 이하이다

## 출력

주어진 이름에 대한 "이름점수"를 출력해주자.

## 소스코드

[소스코드 보기](너의%20이름은%20몇%20점이니？.py)