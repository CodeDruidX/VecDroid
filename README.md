# VecDroid
Convert vector from components into Angles+Len performance
Представье обычный вектор заданный компонентами по координатам:
```python
v_old=[6,5]
```
Но однажды мне понадобилось его представить так:
```python
v_new={"len":7.8,"angle":50.2°}
```
![image](https://user-images.githubusercontent.com/52743561/186671920-35a74f17-9016-4913-ab95-7e8ac198947e.png)

По сути своей разложить при помощи арктангенса -_-

Но потом мы с другом пришли к выводу что это возможно для любого N-мерного вектора)

```python
v_old=[6,5,10]
```

```python
v_new={"len":12.7,"angles":[50.2°,38°]}
```

![image](https://user-images.githubusercontent.com/52743561/186673871-971749a2-9765-4152-9442-5671300658c8.png)
