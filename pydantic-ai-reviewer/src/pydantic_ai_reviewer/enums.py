from enum import Enum


class UpdateType(str, Enum):
    RECOMMEND_ADVANCE = "recommend_advance"
    RECOMMEND_DECLINE = "recommend_decline"
    RECOMMEND_FOLLOW_UP = "recommend_follow_up"
