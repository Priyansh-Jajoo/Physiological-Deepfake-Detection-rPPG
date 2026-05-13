import cv2
from mtcnn import MTCNN

class ForensicProcessor:
    def __init__(self):
        self.detector = MTCNN() # Face detection for ROI

    def get_biological_roi(self, frame):
        """Extracts the Green channel from the forehead/cheeks to target rPPG signals."""
        result = self.detector.detect_faces(frame)
        if result:
            x, y, w, h = result[0]['box']
            # Target the forehead area (upper 20% of the box)
            forehead = frame[y:y+int(h*0.2), x:x+w]
            return forehead[:, :, 1] # Green channel has highest SNR for blood flow
        return None
