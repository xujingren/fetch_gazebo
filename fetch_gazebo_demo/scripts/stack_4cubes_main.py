from xu_demo import*

rospy.init_node("stack_4cubes.py")
while not rospy.Time.now():
    pass

move_base=MoveBaseClient()
torso_action=FollowTrajectoryClient("torso_controller",["torso_lift_joint"])
head_action=PointHeadClient()
grasping_client=GraspingClient()

rospy.loginfo("Move to the first location..")
move_base.goto(2.3,2.9,0)
move_base.goto(2.5,2.9,0)
rospy.loginfo("Raise the torso..")
torso_action.move_to([0.4,])
# rospy.loginfo("")
rospy.loginfo("Look at..")
head_action.look_at(3.4,2.9,0,"map")
# while not rospy.is_shutdown():
rospy.loginfo("Update scene..")
grasping_client.updateScene()
rospy.loginfo("Get graspable cube..")
cube1,grasps=grasping_client.getGraspableCube()
if cube1==None:
    rospy.logwarn("Perception failed!")
if grasping_client.pick(cube1,grasps):
    rospy.loginfo("Pick successfully..")

# rospy.logwarn("Picking failed!")
rospy.loginfo("Tuck..")
grasping_client.tuck()

rospy.loginfo("Turn left by 90..")
move_base.goto(2.5,2.9,1.57)
# rospy.loginfo("Move forward to the second location..")
# move_base.goto(2.5,3.7,1.57)
# rospy.loginfo("Turn right by 90..")
# move_base.goto(2.5,3.7,0)
rospy.loginfo("Move to second position..")
move_base.goto(2.5,3.7,0)
rospy.loginfo("Look at..")
head_action.look_at(3.4,3.7,0,"map")
grasping_client.updateScene()
cube2,grasps2=grasping_client.getGraspableCube()
rospy.loginfo("Placing the object..")
place_pose=PoseStamped()
place_pose.pose=cube2.primitive_poses[0]
place_pose.pose.position.z+=0.065
place_pose.header.frame_id=cube2.header.frame_id
grasping_client.place(cube1,place_pose)
rospy.loginfo("Tuck..")
grasping_client.tuck()

rospy.loginfo("Move the third position..")
rospy.loginfo("Turn left by 90..")
move_base.goto(2.5,3.7,1.57)
move_base.goto(2.5,4.3,0)
rospy.loginfo("Move to..")
move_base.goto(4,4.3,-1.57)
head_action.look_at(4,3.7,0,"map")
rospy.loginfo("Update scene..")
grasping_client.updateScene()
rospy.loginfo("Get graspable cube..")
cube3,grasps3=grasping_client.getGraspableCube()
if cube3==None:
    rospy.logwarn("Perception failed!")
if grasping_client.pick(cube3,grasps3):
    rospy.loginfo("Pick successfully..")
rospy.loginfo("Tuck..")
grasping_client.tuck()

rospy.loginfo("Turn right by 90..")
move_base.goto(4.2,4.3,-3.14)
rospy.loginfo("Move to..")
move_base.goto(3.4,4.3,-1.57)

rospy.loginfo("Look at..")
head_action.look_at(3.4,3.7,0,"map")
grasping_client.updateScene()
cube33,grasps33=grasping_client.getGraspableCube()
rospy.loginfo("Placing the object..")

place_pose2=PoseStamped()
place_pose2.pose=cube33.primitive_poses[0]
place_pose2.pose.position.z+=0.065
place_pose2.header.frame_id=cube33.header.frame_id
grasping_client.place(cube3,place_pose2)
rospy.loginfo("Tuck..")
grasping_client.tuck()