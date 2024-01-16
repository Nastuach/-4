# TODO решите задачу
import json
def task() -> float:
    with open("input.json",'r') as f:
        _list=json.load(f)
    s=0
    for d in _list:
        s+=d["score"]*d["weight"]
    return round(s,3)


print(task())
