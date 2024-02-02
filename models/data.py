from dataclasses import dataclass

@dataclass
class Data:
    id: str
    body: str
    post_id: str
    comment_id: str
    created_timestamp: int
    data_source: str
    compound: float
    pos: float
    neu: float
    neg: float