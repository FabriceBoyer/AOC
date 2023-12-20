from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Workflow:
    name: str
    rules: list[Rule]
    default_target_wf: str


@dataclass
class Rule:
    raw_str: str
    category: str
    condition: str
    value: int
    target_wf: str


wf_dict: dict[str, Workflow] = {}

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

# parse
for line in lines:
    if line == "":  # separator
        break
    wf_split = line[:-1].split("{")
    wf_name = wf_split[0]
    wf_rules = wf_split[1].split(",")
    rules: list[Rule] = []
    for rule_str in wf_rules[:-1]:
        rule_split = rule_str.split(":")
        target_wf: str = rule_split[1]
        category: str = rule_split[0][0]
        condition: str = rule_split[0][1]
        value: int = int(rule_split[0][2:])
        rules.append(Rule(rule_str, category, condition, value, target_wf))
    default_target_wf: str = wf_rules[-1]
    wf_dict[wf_name] = Workflow(wf_name, rules.copy(), default_target_wf)

in_wf: Workflow = wf_dict["in"]
cat_map: dict[str, int] = {"x": 0, "m": 1, "a": 2, "s": 3}

# start from Accepted workflow result and work upwards

total: int = 0

print(total)
