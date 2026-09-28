# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)
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
![](../../images/lab02/ex1_Вывод.png)
