# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)
## Задание 1 — arrays.py
## Min_Max
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0: raise ValueError('Пустой список')
    mi=nums[0]
    ma=nums[0]
    for i in nums:
        if i<mi:
            mi=i
        if i>ma:
            ma=i
    ans=(mi,ma)
    return ans
```
### Тест-кейсы
```python
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))
```
![](../../images/lab02/ex1_Вывод.png)

## Unique_sorted
```python 
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений (по возрастанию)
    [3, 1, 2, 1, 3] → [1, 2, 3]
    """
    a=set(nums)
    nums=[]
    nums.extend(a)
    n=len(nums)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return (nums)
```
### Тест-кейсы
```python
print(unique_sorted([3,3,2,1,4]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![](../../images/lab02/ex1.2_out.png)

## Flatten
```python 
def flatten(mat: list[list | tuple]) -> list:
    """Расплющивает список списков/кортежей в один список по строкам (row-major)
    [[1], [], [2, 3]] → [1, 2, 3]
    """
    result=[]
    for i in mat:
        if type(i)==list or type(i)==tuple:
            result+=i
        else:
            raise TypeError('неверный тип данных')
    return result
```
### Тест-кейсы
```python
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![](../../images/lab02/ex1.3_out.png)


## Задание 2
## Transpose
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    """Поменять строки и столбцы местами в прямоугольной матрице
    [[1, 2], [3, 4]] → [[1, 3], [2, 4]]
    """
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError('«матрица рваная» (строки разной длины)')
    if mat==[]: return []    
    cnt_stolb=len(mat[0])
    
    ans=[]
    for j in range(cnt_stolb):
        a=[]
        for row in mat:
            a.append(row[j])
        ans.append(a)
    return ans
```
### Тест-кейсы:
```python
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![](../../images/lab02/ex2.1_out.png)

## Row_sums
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке. Требуется прямоугольность 
    [[1, 2, 3], [4, 5, 6]] → [6, 15]
    """
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError('Рваная матрица')
    ans=[]
    for row in mat:
        ans.append(sum(row))
    return ans
```
### Тест-кейсы
```python
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3],]))
```
![](../../images/lab02/ex2.2_out.png)

## Col_sums
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """ Сумма по каждому столбцу. Требуется прямоугольность.
    [[1, 2, 3], [4, 5, 6]] → [5, 7, 9] """
    
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError('рвананя матрица')
    ans=[]
    st=len(mat[0])
    for j in range(st):
        cnt=0
        for row in mat:
            cnt+=row[j]
        ans.append(cnt)
    return ans
```
### Тест-кейс
```python
print(col_sums([[1,2,3],[4,5,6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![](../../images/lab02/ex2.3_out.png)