# 1871번: 좋은 자동차 번호판 - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

![](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=white) ![](https://img.shields.io/badge/BOJ-Passed-Success?style=flat-square) ![](https://img.shields.io/badge/Memory_Usage-31256KB-informational?style=flat-square) ![](https://img.shields.io/badge/Time_Spend-48ms-informational?style=flat-square)

문자열 부분을 26진법으로 계산하면 되는데 알파뱃의 개수는 총 26개이다. 그러므로 그냥 A = 1, B = 2 ... Z = 26 으로 계산하면 쉽게 해결할 수 있다.
문자열을 받은 후 리스트에 각 원소로 저장한 다음, 하나씩 꺼내서 ASCII 코드로 변환한다. 각 변환된 정수에 -42를 해주면 A = 26 ... 이 되므로 이제 값을 계산해서 좋은 번호판인지 계산하면 되겠다.

숏코딩 하려다 여러 실수를 저질렀다. A를 26으로 맞추는게 아니라 우선 A는 0이 되어야 한다.
거기다 ASCII코드로 A는 65인데 68로 착각해 68을 빼다가 계속 틀린 값을 반환했다..
추가로 자릿수 역시 맨 앞자리를 2제곱을 해야하는데 맨 뒷자리를 2제곱 해버려서....
역시 코드를 짧게 짜는 것 보다, 정답을 맞추는게 훨씬 더 중요하다고 생각된다.


<!-- end -->

## 문제

[문제 링크](https://boj.kr/1871)


<p>앨버타의 자동차 번호판은 ABC-0123 (세 글자, 네 숫자)와 같이 두 부분으로 나누어져 있다.</p>

<p>좋은 번호판은 첫 번째 부분의 가치와 두 번째 부분의 가치의 차이가 100을 넘지 않는 번호판이다.</p>

<p>글자로 이루어진 첫 번째 부분의 가치는 글자를 26진법 수처럼 계산한다. (각 자리가 [A..Z]) 예를 들어, "ABC"의 가치는 28 (0×26<sup>2</sup> + 1×26<sup>1</sup> + 2×26<sup>0</sup>)이 된다. "ABC-0123"은 &nbsp;|28 - 123| ≤ 100 이기 때문에, 좋은 번호판이다.</p>

<p>자동차 번호판이 주어졌을 때, 좋은 번호판인지 아닌지를 구하는 프로그램을 작성하시오.</p>



## 입력

첫째 줄에 번호판의 수 N (1 ≤ N ≤ 100)이 주어진다. 다음 N개 줄에는 자동차 번호판이 LLL-DDDD 형식으로 주어진다.

## 출력

각각의 자동차 번호판에 대해서, 좋은 번호판이면 "nice"를, 아니면 "not nice"를 출력한다.

## 소스코드

[소스코드 보기](좋은%20자동차%20번호판.py)