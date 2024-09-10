
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
  
class ImagePublisher(Node):
  
  def __init__(self):
    super().__init__('image_publisher')
    self.publisher_ = self.create_publisher(Image, '/camera/rgb/image_raw', 1)
    timer_period = 0.02
    self.timer = self.create_timer(timer_period, self.timer_callback)
    #Uncomment when on Nano
    self.cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")

    #Uncomment when on other devices
    #self.cap = cv2.VideoCapture(0)

    self.br = CvBridge()
    
  def timer_callback(self):
    ret, frame = self.cap.read()
    if ret == True:
      msg = self.br.cv2_to_imgmsg(frame, encoding="rgb8")
      msg.header.frame_id = ("camera_link_optical")
      self.publisher_.publish(msg)
      #self.get_logger().info('Publishing video frame')
    else:
      self.get_logger().info('failed video frame')
   
def main(args=None):
  rclpy.init(args=args)
  image_publisher = ImagePublisher()
  rclpy.spin(image_publisher)
  image_publisher.destroy_node()
  rclpy.shutdown()
   
if __name__ == '__main__':
  main()