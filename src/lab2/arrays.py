#Задание 1
# 1.1
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Поиск минимума и максимума
    [3, -1, 5, 5, 0] → (-1, 5)
    """
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
# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))

#################################################################################################################

#1.2
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений (по возрастанию)
    [3, 1, 2, 1, 3] → [1, 2, 3]
    """
    unikal=set(nums)
    nums=[]
    nums.extend(unikal)
    n=len(nums)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return (nums)
# print(unique_sorted([3,3,2,1,4]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

#####################################################################################################################

#1.3
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
# print(flatten([[1, 2], [3, 4]]))
# print(flatten([[1, 2], (3, 4, 5)]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"]))