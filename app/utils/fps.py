# app/utils/fps.py
import time
from collections import deque

class FPSMonitor:
    """Class for monitoring and calculating FPS"""
    
    def __init__(self, history_size=30):
        """
        Initialize FPS monitor
        
        Args:
            history_size (int): Number of frames to keep in history for average calculation
        """
        self.prev_time = 0
        self.current_time = 0
        self.processing_times = deque(maxlen=history_size)
        self.start_time = None
    
    def start_frame(self):
        """Start timing a new frame"""
        self.start_time = time.time()
        return self.start_time
    
    def end_frame(self):
        """
        End timing the current frame
        
        Returns:
            float: Processing time for the frame
        """
        if self.start_time is None:
            raise ValueError("start_frame() must be called before end_frame()")
        
        processing_time = time.time() - self.start_time
        self.processing_times.append(processing_time)
        return processing_time
    
    def update(self):
        """Update FPS calculation"""
        self.current_time = time.time()
        fps = 1 / (self.current_time - self.prev_time) if self.prev_time > 0 else 0
        self.prev_time = self.current_time
        return fps
    
    def get_avg_processing_time(self):
        """Get average processing time per frame"""
        if not self.processing_times:
            return 0
        return sum(self.processing_times) / len(self.processing_times)
    
    def get_stats(self, target_fps):
        """
        Get processing statistics
        
        Args:
            target_fps (float): Target FPS for real-time processing
            
        Returns:
            dict: Statistics about processing performance
        """
        avg_time = self.get_avg_processing_time()
        frame_delay = 1.0 / target_fps if target_fps > 0 else 0
        
        stats = {
            "avg_processing_time": avg_time,
            "required_time_for_realtime": frame_delay,
            "is_realtime": avg_time <= frame_delay,
            "speed_factor": frame_delay / avg_time if avg_time > 0 else float('inf')
        }
        
        return stats
