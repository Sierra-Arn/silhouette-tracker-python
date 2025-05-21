# app/models/detector.py
import torch
from ultralytics import YOLO

class PersonDetector:
    """Class for detecting people in images using YOLOv8 model with CUDA acceleration"""
    
    def __init__(self, model_path, confidence=0.8):
        """
        Initialize the detector
        
        Args:
            model_path (str): Path to the YOLO model file
            confidence (float): Detection confidence threshold
        """
        self.model_path = model_path
        self.confidence = confidence
        self.device = self._get_device()
        self.model = self._load_model()
        
    def _get_device(self):
        """Get the CUDA device to use"""
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA is required but not available on this system")
        
        device = 0
        print(f"Using GPU device: {torch.cuda.get_device_name(device)}")
        return device
    
    def _load_model(self):
        """Load the YOLO model to GPU"""
        print(f"Loading model from: {self.model_path}")
        model = YOLO(self.model_path)
        model.to(self.device)
        return model
    
    def detect(self, frame):
        """
        Detect people in a frame
        
        Args:
            frame: Input image frame
            
        Returns:
            Detection results
        """
        results = self.model.predict(
            source=frame, 
            classes=0,  # Only detect people
            conf=self.confidence, 
            verbose=False,
            device=self.device
        )
        
        return results[0] if results and len(results) > 0 else None
