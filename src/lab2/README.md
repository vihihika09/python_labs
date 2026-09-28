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
