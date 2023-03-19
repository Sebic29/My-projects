from dataclasses import dataclass


@dataclass
class ResView:
    res_name: str
    accumulated_points: int
