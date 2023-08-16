#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mtslzx <boj.kr/u/mtslzx>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1920                           #+#        #+#      #+#     #
#    Solved: 2023/08/16 22:20:15 by mtslzx        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

input()
availableNumberList = set(list(input().replace(" ", "")))
input()
searchNumberList = list(input().replace(" ", ""))

for i in searchNumberList:
    if i in availableNumberList: print("1")
    else: print("0")