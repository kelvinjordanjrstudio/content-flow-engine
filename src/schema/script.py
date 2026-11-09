from typing import List, Optional
from pydantic import BaseModel, Field

class HookModel(BaseModel):
    visual_cue: str = Field(..., description="Visual instructions or camera framing for the hook.")
    spoken_text: str = Field(..., description="The exact words spoken during the hook.")

class SceneModel(BaseModel):
    timestamp: str = Field(..., description="Timestamp range for the scene (e.g., '0:00 - 0:05').")
    visual: str = Field(..., description="Visual action or B-roll description.")
    audio: str = Field(..., description="Voiceover or dialogue spoken during this scene.")
    pacing_notes: Optional[str] = Field(None, description="Pacing, transition, or editing notes.")

class MetadataModel(BaseModel):
    estimated_duration_seconds: int = Field(..., description="Estimated total runtime in seconds.")
    tags: List[str] = Field(..., description="SEO tags or platform keywords.")
    call_to_action: str = Field(..., description="Final call to action for the viewer.")

class VideoScriptModel(BaseModel):
    title: str = Field(..., description="Catchy title for the short-form video.")
    platform: str = Field(..., description="Target social platform (e.g., TikTok, Reels, Shorts).")
    hook: HookModel
    scenes: List[SceneModel]
    metadata: MetadataModel