import cv2
from app.core.config import get_settings
from app.models.detector import PersonDetector
from app.utils.drawing import draw_corner_rect
from app.utils.fps import FPSMonitor
from app.utils.video import VideoProcessor

def process_video():
    """Process video for person detection and counting using CUDA acceleration"""
    try:
        # Get and validate settings
        settings = get_settings()
        settings.validate_paths()
        
        # Initialize components
        video_processor = VideoProcessor(
            settings.video_path, 
            (settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT)
        )
        detector = PersonDetector(settings.model_path, settings.CONFIDENCE)
        fps_monitor = FPSMonitor()
        
        # Open video
        video_processor.open()
        
        # Pre-allocate variables for better performance
        people_count = 0
        frame_count = 0
        
        print(f"Processing video: {settings.video_path}")
        print(f"Model: {settings.model_path}")
        print(f"Confidence threshold: {settings.CONFIDENCE}")
        
        while True:
            # Increment frame counter
            frame_count += 1
            
            # Start timing the frame
            fps_monitor.start_frame()
            
            # Read frame
            img = video_processor.read_frame()
            if img is None:
                print("End of video reached")
                break
            
            # Calculate FPS
            fps_current = fps_monitor.update()
            
            # Detect people
            result = detector.detect(img)
            
            # Process results
            if result:
                # Get keypoints if available
                if hasattr(result, 'keypoints') and result.keypoints is not None:
                    # Draw keypoints and skeleton
                    img = result.plot()
                
                # Process bounding boxes
                if hasattr(result, 'boxes') and result.boxes is not None:
                    boxes = result.boxes
                    people_count = len(boxes)
                    
                    for box in boxes:
                        # Get box coordinates
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                        h, w = y2 - y1, x2 - x1
                        
                        # Draw rectangle
                        img = draw_corner_rect(
                            img, 
                            [x1, y1, w, h],
                            l=9,
                            t=3, 
                            colorR=(255, 0, 255),
                            colorC=(255, 255, 76)
                        )
                        
                        # Draw confidence
                        conf = float(box.conf[0])
                        cv2.putText(img, f"{conf:.2f}", (x1, y1-10),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    people_count = 0
                
            # Display people count
            cv2.putText(img, f"People: {people_count}", (20, 50),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Display FPS
            cv2.putText(img, f"FPS: {fps_current:.1f}", (20, 90),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Display the frame
            cv2.imshow("Person Detection", img)
            
            # End timing the frame
            processing_time = fps_monitor.end_frame()
            
            # Calculate remaining time to wait to maintain original video speed
            frame_delay = video_processor.frame_delay
            wait_time = max(1, int((frame_delay - processing_time) * 1000)) if processing_time < frame_delay else 1
            
            # Check for exit with the calculated wait time
            key = cv2.waitKey(wait_time) & 0xFF
            if key == 27 or key == ord('q'):  # ESC or 'q' key
                print("User terminated")
                break
            
            # Check if window was closed
            if cv2.getWindowProperty("Person Detection", cv2.WND_PROP_VISIBLE) < 1:
                print("Window closed")
                break
            
            # If processing is too slow, print a warning (only occasionally to avoid spam)
            if processing_time > frame_delay and frame_count % 30 == 0:
                print(f"Warning: Processing time ({processing_time:.3f}s) exceeds frame time ({frame_delay:.3f}s)")
        
        # Clean up
        video_processor.close()
        
        # Print processing statistics
        stats = fps_monitor.get_stats(video_processor.fps)
        print(f"Average processing time per frame: {stats['avg_processing_time']:.3f}s")
        print(f"Required time per frame for real-time: {stats['required_time_for_realtime']:.3f}s")
        
        if not stats['is_realtime']:
            print(f"Processing is {1/stats['speed_factor']:.1f}x slower than real-time")
        else:
            print(f"Processing is {stats['speed_factor']:.1f}x faster than real-time")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

def main():
    """Main application entry point"""
    print("Starting person detection application with CUDA acceleration")
    return process_video()

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
