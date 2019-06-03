from manipulation_client import*

rospy.init_node("base_sequence")
while not rospy.Time.now():
    pass

move_base=MoveBaseClient()
torso_action=FollowTrajectoryClient("torso_controller",["torso_lift_joint"])
head_action=PointHeadClient()
grasping_client=GraspingClient()

rospy.loginfo("Move to the first base position..")
move_base.goto(-1.75,0.9,1.57)
rospy.loginfo("Raise the torso..")
torso_action.move_to([0.4,])
rospy.loginfo("Look at..")
head_action.look_at(-2.1,1.6,0,"map")
# while not rospy.is_shutdown():
rospy.loginfo("Update scene..")
grasping_client.updateScene()
rospy.loginfo("Get graspable cube..")
cube1,grasps=grasping_client.getGraspableCube()
if cube1==None:
    rospy.logwarn("Perception failed!")
if grasping_client.pick(cube1,grasps):
    rospy.loginfo("Pick successfully..")


rospy.loginfo("Move to the second base position..")
move_base.goto(-0.75,0.9,1.57)

rospy.loginfo("Move to the third base position..")
move_base.goto(0.25,0.9,1.57)

rospy.loginfo("Move to the fourth base position..")
move_base.goto(1.25,0.9,1.57)