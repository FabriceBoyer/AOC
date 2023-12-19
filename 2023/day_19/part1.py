from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Part:
    values: list[int]  # x,m,a,s order


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
parts: list[Part] = []

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

# parse
part_parsing = False
for line in lines:
    if line == "":  # separator
        part_parsing = True
        continue
    if not part_parsing:
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
    else:
        cat_split = line[1:-1].split(",")
        values: list[int] = []
        for cat_str in cat_split:
            split = cat_str.split("=")
            value: int = int(split[1])
            values.append(value)  # always in xmas order
        parts.append(Part(values.copy()))

in_wf: Workflow = wf_dict["in"]
cat_map: dict[str, int] = {"x": 0, "m": 1, "a": 2, "s": 3}


def is_rule_true_for_part(rule_: Rule, part_: Part) -> bool:
    value_: int = part_.values[cat_map[rule_.category]]
    if rule_.condition == "<":
        return value_ < rule_.value
    if rule_.condition == ">":
        return value_ > rule_.value
    raise ValueError(f"unknown condition {rule_.condition}")


def is_part_accepted(part_: Part) -> bool:
    accepted: bool = False
    current_wf: Workflow = in_wf
    while True:
        # print(f"current wf is '{current_wf.name}'")
        target_wf_: str = current_wf.default_target_wf
        for rule_ in current_wf.rules:
            if is_rule_true_for_part(rule_, part_):
                target_wf_ = rule_.target_wf
                # print(f"rule {rule_.raw_str} is TRUE, jumping to WF {target_wf_}")
                break
        if target_wf_ in ("A", "R"):
            accepted = target_wf_ == "A"
            if accepted:
                print(f"part {part.values} Accepted")
            else:
                print(f"part {part.values} REJECTED")
            break

        current_wf = wf_dict[target_wf_]

    return accepted


total: int = 0
for part in parts:
    if is_part_accepted(part):
        total += sum(part.values)
    # print("")

print(total)
