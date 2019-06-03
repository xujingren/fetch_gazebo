from manipulation_client import*

rospy.init_node("move_to")
while not rospy.Time.now():
    pass

move_base=MoveBaseClient()
torso_action = FollowTrajectoryClient("torso_controller", ["torso_lift_joint"])
head_action=PointHeadClient()
grasping_client=GraspingClient()

rospy.loginfo("move to ..")
move_base.goto(0,0.9,1.57)
rospy.loginfo("raise torso..")
torso_action.move_to([0.2,])
rospy.loginfo("look at..")
head_action.look_at(0,1.5,0,"map")
rospy.loginfo("Update scene..")
grasping_client.updateScene()
rospy.loginfo("Get graspable cube..")
cube,grasps=grasping_client.getGraspableCube()
if cube==None:
    rospy.logwarn("Perception failed!")
if grasping_client.pick(cube,grasps):
    rospy.loginfo("Pick successfully..")
