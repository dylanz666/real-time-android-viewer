from pydantic import BaseModel
from typing import Literal, Optional


class ScreenAction(BaseModel):
    action: Literal["touch", "swipe", "touch_down", "touch_up"]
    start_x: Optional[int] = None
    start_y: Optional[int] = None
    start_x_percent: Optional[float] = None
    start_y_percent: Optional[float] = None
    end_x: Optional[int] = None
    end_y: Optional[int] = None
    end_x_percent: Optional[float] = None
    end_y_percent: Optional[float] = None
    main_key: Optional[str] = None
    bind_key: Optional[str] = None
    device_id: Optional[str] = None
