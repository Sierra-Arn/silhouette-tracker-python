# app/core/config.py
from functools import lru_cache
import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings and configuration."""
    
    # Model settings
    MODEL_NAME: str = Field(default="yolov8m-pose.pt", description="Name of the YOLO model file")
    MODELS_DIR: str = Field(default="models", description="Directory containing model files")
    CONFIDENCE: float = Field(default=0.8, ge=0.0, le=1.0, description="Detection confidence threshold")
    
    # Video settings
    VIDEO_NAME: str = Field(default="example-pexels.mp4", description="Name of the video file to process")
    VIDEOS_DIR: str = Field(default="videos", description="Directory containing video files")
    
    # Display settings
    DISPLAY_WIDTH: int = Field(default=1020, gt=0, description="Width of the display window")
    DISPLAY_HEIGHT: int = Field(default=720, gt=0, description="Height of the display window")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    @property
    def model_path(self) -> str:
        """Full path to the model file"""
        return os.path.join(self.MODELS_DIR, self.MODEL_NAME)
    
    @property
    def video_path(self) -> str:
        """Full path to the video file"""
        return os.path.join(self.VIDEOS_DIR, self.VIDEO_NAME)
    
    def validate_paths(self):
        """Validate that required files and directories exist"""
        # Check if model file exists
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        
        # Check if video file exists
        if not os.path.exists(self.video_path):
            raise FileNotFoundError(f"Video file not found at {self.video_path}")
        
        return True

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings