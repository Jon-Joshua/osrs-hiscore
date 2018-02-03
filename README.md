## osrs-hiscore

Old School Runescape Hiscore wrapper written in python using requests libray.


```
>>> from osrshiscore import OSRSHiscore
>>> p = OSRSHiscore()
>>> q = q.get('Lynx Titan')
>>> q['overall']
{'rank': 1, 'level': 2277, 'experience': 4282456875}
>>> q['overall']['experience']
4282456875
```
