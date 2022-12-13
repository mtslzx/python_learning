
# TODO: FIX THIS CODE

class Matrix:
    """행렬을 추상화한 class 정의"""
    def __init__(self, row: int = 0, col: int = 0) -> None:
        """self row col"""
        self.row = row
        self.col = col
        self.data = list()  # [[1,2,3], [4,5,6]]
        cnt = 1
        for i in range(self.row):
            self.data.append([])
            for _ in range(self.col):
                self.data[i].append(cnt)
                cnt += 1
                

    
    def getElement(self):
        pass
    
    def getTranspose(self) -> list:
        return list(map(list, list(zip(*self.data))))
    
    def doTranspose(self) -> None:
        self.data = list(map(list, list(zip(*self.data))))
        return None
    
    def tupletolist(self):
        return list(map(list, self.data))
    
    def __str__(self):
        return str(self.data).replace("], ", "]\n").replace("[[", "[").replace("]]", "]")  # 문자열 처리로 해결하기
    
    def __repr__(self):  # https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__
        pass 
    
    def __add__(self, other):
        temp = Matrix()
        for i, j in zip(self.data, other.data):
            for k in range(len(self.data[0])):
                temp.data.append(list(map(lambda x, y: x + y, i, j)))
                print(f"i: {i}, j: {j} k : {k} i[k]: {i[k]} j[k]: {j[k]}")
                
                temp.data.append(list(i[k] + j[k]))
            
            #temp.data.append(list(map(lambda x: x * i)))
        return temp
    
    def __mul__(self, value: int) -> list:
        temp = Matrix()
        for i in self.data: 
            temp.data.append(list(map(lambda x: x * value, i)))
        return temp



if __name__ == "__main__":
    m1 = Matrix(2,3)
    print(m1.data)
    print(m1.getTranspose())
    print(type(m1))
    print(m1)
    m1.doTranspose()
    print(type(m1))
    print(m1)
    m2 = m1 * 3
    print(type(m2))
    print(m2)
    m3 = m1 + m2
    print(type(m3))
    print(m3)



# 코드 실행부
if __name__ == "__ma__":
    m1 = Matrix(2,3)
    print("print(m1)")
    print(m1)
    
    print("print(m1.getElement(2,2))")
    print(m1.getElement(2,2))
    m1.setElement(2,2,-10)
    
    print("print(m1)")
    print(m1)
    
    print("print(m1.getTranspose())")
    print(m1.getTranspose()) 
    print("print(m1)")
    print(m1)
    
    print("print(m1.doTranspose())")
    print(m1.doTranspose()) 
    print("print(m1)")
    print(m1)
    
    m2 = m1 * 3
    print("print(m2)")
    print(m2)
    
    m3 = m1 + m2
    print("print(m3)")
    print(m3)
                                    