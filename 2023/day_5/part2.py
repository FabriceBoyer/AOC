from __future__ import annotations
from dataclasses import dataclass
import sys


@dataclass
class MapKind:
    source_category: str
    target_category: str
    maps: list[MapRange]


@dataclass
class MapRange:
    kind: MapKind
    destination_start: int
    source_start: int
    range_length: int


@dataclass
class Range:
    start: int
    length: int


kinds: list[MapKind] = list()
seed_ranges: list[Range] = list()

with open("input.txt") as f:
    seeds_str: list[str] = f.readline().split("seeds:")[1].strip().split(" ")
    seeds_int: list[int] = list(map(lambda x: int(x.strip()), seeds_str))

    prev_seed = -1
    for idx, seed in enumerate(seeds_int):
        if idx % 2 == 1:  # odd
            seed_ranges.append(Range(prev_seed, seed))
        else:
            prev_seed = seed

    for line in f:
        if line == "\n":
            continue

        kind_split = line.split("map")
        if len(kind_split) == 2:
            source_target_split = kind_split[0].split("-to-")
            current_map_kind = MapKind(
                source_target_split[0], source_target_split[1], []
            )
            kinds.append(current_map_kind)
            continue

        values = list(map(lambda x: int(x.strip()), line.split(" ")))
        if len(values) == 3:
            current_map = MapRange(current_map_kind, values[0], values[1], values[2])
            current_map_kind.maps.append(current_map)
            continue

        raise Exception("shouldn't be reached")

# sort kind range by start
for kind in kinds:
    kind.maps.sort(key=lambda x: x.source_start)

seed_ranges.sort(key=lambda x: x.start)


current_range_list: list[Range] = seed_ranges
for kind in kinds:  # they are chained in order no need to search name
    new_range_list: list[Range] = []  # reset
    for range_item in current_range_list:
        rem_range: Range = range_item  # remaining range
        for map_item in kind.maps:  # sorted by source and not overlapping
            map_item_source_end = map_item.source_start + map_item.range_length
            while rem_range.length > 0:
                if rem_range.start < map_item.source_start:  # start before beginning of map_item
                    non_intersect_length = min(map_item.source_start - rem_range.start, rem_range.length)
                    new_range_list.append(Range(rem_range.start, non_intersect_length))  # iso mapping default
                    rem_range = Range(rem_range.start+non_intersect_length, rem_range.length - non_intersect_length)
                    continue  # bypass rest of loop

                elif rem_range.start < map_item_source_end:  # start before end of map_item
                    intersect_length = min(map_item_source_end - rem_range.start, rem_range.length)
                    offset = rem_range.start - map_item.source_start  # from map_item_source_start
                    new_range_list.append(Range(map_item.destination_start + offset, intersect_length))
                    rem_range = Range(rem_range.start+intersect_length, rem_range.length - intersect_length)
                    continue

                else:
                    break  # continue with another map_item but same rem_range

    # swap list with new destination list before switching kind
    current_range_list = new_range_list

lowest = sys.maxsize
for range_item in current_range_list:
    lowest = min(range_item.start, lowest)
print(lowest)
