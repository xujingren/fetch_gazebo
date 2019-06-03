import rospy
from nav_msgs.msg import Odometry

rospy.init_node("joint_state_sub")

def callBack(msg):
    print msg.pose.pose.position

sub=rospy.Subscriber("odom",Odometry,callBack)
rospy.spin()