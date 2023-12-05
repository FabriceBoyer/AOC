from __future__ import annotations
from dataclasses import dataclass
import sys

@dataclass
class MapKind:
    source_category: str
    target_category: str
    maps: list[Map]


@dataclass
class Map:
    kind: MapKind
    destination_start: int
    source_start: int
    range_length: int


kinds: list[MapKind] = list()
maps: list[Map] = list()

with open("input.txt") as f:
    seeds: list[int] = f.readline().split("seeds:")[1].strip().split(" ")
    seeds= list(map(lambda x: int(x.strip()), seeds))

    for line in f:
        if line == "\n":
            continue

        kind_split = line.split("map")
        if len(kind_split) == 2:
            source_target_split = kind_split[0].split("-to-")
            current_map_kind = MapKind(source_target_split[0], source_target_split[1], [])
            kinds.append(current_map_kind)
            continue

        values = list(map(lambda x: int(x.strip()), line.split(" ")))
        if len(values) == 3:
            current_map = Map(current_map_kind, values[0], values[1], values[2])
            maps.append(current_map)
            current_map_kind.maps.append(current_map)
            continue

        raise Exception("shouldn't be possible")


# for item in maps:
# print(f"{item.kind.source_category} {item.kind.target_category} : {item.destination_start} {item.source_start} {item.range_length}")

lowest = sys.maxsize
for seed in seeds:
    current_id = seed
    print(f"******* Working on seed {current_id}")
    for kind in kinds:  # they are chained in order no need to search name
        for map_index, map_item in enumerate(kind.maps):
            if current_id >= map_item.source_start and current_id < (
                map_item.source_start + map_item.range_length
            ):
                print(f"Rule number {map_index} matching id {current_id}")
                current_id = map_item.destination_start + (
                    current_id - map_item.source_start
                )
                print(f"new id is {current_id}")
                break
        print(f"from {kind.source_category} to {kind.target_category} with id {current_id}")
    lowest = min(current_id, lowest)

print(lowest)
