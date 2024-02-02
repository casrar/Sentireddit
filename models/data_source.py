from dataclasses import dataclass

@dataclass
class DataSource:
    id: str
    subreddit: str
    query: str