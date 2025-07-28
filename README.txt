📷 Motion Detection with Timestamp Logging

This project focuses on detecting motion — specifically the entry and exit of any moving object within the camera frame.

🔍 Key Features:
- ✅ Detects motion by comparing frames using image processing techniques.
- ✅ Automatically draws a rectangle around the detected moving object.
- ✅ Records and logs the timestamp when:
  - An object enters the frame.
  - An object exits the frame.
- ✅ Saves all timestamps into an Excel file for easy review.

🛠️ How It Works:
1. The program captures video from a camera.
2. It continuously checks for movement by comparing each frame with the initial one.
3. When an object is detected (based on significant motion), it:
   - Highlights the object with a green rectangle.
   - Records the start time.
4. When the object disappears from the frame:
   - It records the end time.
5. At the end of the session, all entry and exit times are saved to a file.

🌍 Real-World Applications:
- Wildlife monitoring: Helps geographic researchers and nature photographers to automatically detect and timestamp wildlife movement without scanning 24 hours of footage manually.
- Traffic monitoring: With further enhancements (like speed tracking), it can be used to monitor vehicles, detect violations, or analyze traffic patterns.
- Workplace monitoring: Can be integrated with facial recognition to log employees’ entry and exit times and store them in individual records for attendance tracking.
