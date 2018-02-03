## osrs-hiscore

Old School Runescape Hiscore wrapper written in python using requests libray.

Example:

```python
>>> from osrshiscore import OSRSHiscore, Hiscores
>>> p = OSRSHiscore(user_agent='osrs-hiscore-example')
>>> q = p.get('Lynx Titan')
>>> q['overall']
{'rank': 1, 'level': 2277, 'experience': 4282456875}
>>> q['overall']['experience']
4282456875
>>> s = p.get('Say Allo', hiscore=Hiscores.IRONMAN)
>>> s['smithing']
{'level': 99, 'rank': 18, 'experience': 15777678}
```
