# app/utils/video.py
import cv2

class VideoProcessor:
    """Class for video processing operations"""
    
    def __init__(self, video_path, display_size=(1020, 720)):
        """
        Initialize video processor
        
        Args:
            video_path (str): Path to the video file
            display_size (tuple): Size to resize video frames for display
        """
        self.video_path = video_path
        self.display_size = display_size
        self.capture = None
        self.fps = 0
        self.frame_count = 0
        self.frame_delay = 0
        
    def open(self):
        """Open the video file and get properties"""
        self.capture = cv2.VideoCapture(self.video_path)
        if not self.capture.isOpened():
            raise ValueError(f"Could not open video {self.video_path}")
        
        # Get video properties
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_delay = 1.0 / self.fps
        
        print(f"Video opened: {self.video_path}")
        print(f"Video FPS: {self.fps}, Total frames: {self.frame_count}")
        
        return self.capture
    
    def read_frame(self):
        """Read and resize a frame from the video"""
        if self.capture is None:
            raise ValueError("Video capture not initialized. Call open() first.")
        
        ret, frame = self.capture.read()
        if not ret:
            return None
        
        # Resize frame for display
        resized_frame = cv2.resize(frame, self.display_size)
        return resized_frame
    
    def close(self):
        """Release video resources"""
        if self.capture is not None:
            self.capture.release()
            self.capture = None
            cv2.destroyAllWindows()
            print("Video resources released")
