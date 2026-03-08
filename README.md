# Web Cam Pose Estimation

Real-time human pose estimation using webcam or video files with MediaPipe and OpenCV. Detects 33 human pose landmarks and overlays skeleton visualization.

## Demo Video


https://github.com/user-attachments/assets/eaa3b243-fe76-470f-b875-a66763b4560d



## Features
- Live webcam pose detection
- Video file processing
- 33 pose landmarks with connections
- Real-time visualization
- ESC key to exit

## Quick Start

### Prerequisites
```bash
pip install opencv-python mediapipe matplotlib
```

### Run Webcam (Live)
```bash
python web_cam_pose_estimation.py
```

### Run Demo Video
```bash
python web_cam_pose_estimation.py
```
*(Uses included "Mr. Bean and the art of seduction..mp4")*


## Usage

1. **Clone repo**
   ```bash
   git clone https://github.com/ubaidkh07/Web_Cam_Pose_Estimation
   cd Web_Cam_Pose_Estimation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run**
   ```bash
   python web_cam_pose_estimation.py
   ```

## Controls
- **ESC**: Exit or ctrl + c
- **Window**: Shows pose landmarks overlaid on video

## Files
| File | Description |
|------|-------------|
| `web_cam_pose_estimation.py` | Main pose detection script |
| `Mr. Bean and the art of seduction..mp4` | Demo video for testing |

## Requirements
```txt
opencv-python>=4.5.0
mediapipe>=0.10.0
matplotlib>=3.5.0
```

## Customization
- Change `cv2.VideoCapture(0)` for webcam
- Modify `(500, 500)` for different resolution
- Adjust `mp_pose.Pose()` parameters for model confidence

## Troubleshooting
- **No pose detected**: Ensure good lighting and clear human figure
- **Video not playing**: Check file path and format
- **Slow performance**: Reduce frame size or use lighter model

