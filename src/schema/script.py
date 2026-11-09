from pydantic import BaseModel, Field
from typing import List, Optional

class Scene(BaseModel):
    scene_number: int
    duration_seconds: int = Field(default=5, description="Estimated duration of the scene in seconds")
    narration: str = Field(description="Voiceover text for this scene")
    visual_description: str = Field(description="Visual cues, on-screen text, or B-roll ideas")

class VideoScript(BaseModel):
    title: str = Field(description="Title or main concept of the video")
    target_platform: str = Field(default="TikTok", description="Platform target e.g. TikTok, Shorts, Reels")
    hook: str = Field(description="Attention-grabbing opening hook line")
    scenes: List[Scene] = Field(default_factory=list, description="Ordered scenes in the script")
    call_to_action: Optional[str] = Field(default=None, description="Closing call to action")
