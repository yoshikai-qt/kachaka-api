# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kachaka-api.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11kachaka-api.proto\x12\x0bkachaka_api\"\x1a\n\x08Metadata\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\x10\"-\n\x06Result\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\nerror_code\x18\x03 \x01(\x05\"\x1b\n\x05\x45rror\x12\x12\n\nerror_code\x18\x02 \x01(\x05\"1\n\tRosHeader\x12\x12\n\nstamp_nsec\x18\x01 \x01(\x03\x12\x10\n\x08\x66rame_id\x18\x02 \x01(\t\"+\n\x04Pose\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\r\n\x05theta\x18\x03 \x01(\x01\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\"^\n\x06Pose3d\x12&\n\x08position\x18\x01 \x01(\x0b\x32\x14.kachaka_api.Vector3\x12,\n\x0borientation\x18\x02 \x01(\x0b\x32\x17.kachaka_api.Quaternion\"T\n\x05Twist\x12$\n\x06linear\x18\x01 \x01(\x0b\x32\x14.kachaka_api.Vector3\x12%\n\x07\x61ngular\x18\x02 \x01(\x0b\x32\x14.kachaka_api.Vector3\"M\n\x14Pose3dWithCovariance\x12!\n\x04pose\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Pose3d\x12\x12\n\ncovariance\x18\x02 \x03(\x01\"L\n\x13TwistWithCovariance\x12!\n\x05twist\x18\x01 \x01(\x0b\x32\x12.kachaka_api.Twist\x12\x12\n\ncovariance\x18\x02 \x03(\x01\"w\n\x03Map\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nresolution\x18\x03 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x12!\n\x06origin\x18\x06 \x01(\x0b\x32\x11.kachaka_api.Pose\"\xe0\x01\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1f\n\x04pose\x18\x03 \x01(\x0b\x32\x11.kachaka_api.Pose\x12\'\n\x04type\x18\x04 \x01(\x0e\x32\x19.kachaka_api.LocationType\x12%\n\x1dundock_shelf_aligning_to_wall\x18\x05 \x01(\x08\x12\'\n\x1fundock_shelf_avoiding_obstacles\x18\x06 \x01(\x08\x12 \n\x18ignore_voice_recognition\x18\x07 \x01(\x08\"9\n\tShelfSize\x12\r\n\x05width\x18\x01 \x01(\x01\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x01\x12\x0e\n\x06height\x18\x03 \x01(\x01\"3\n\x10RecognizableName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdeletable\x18\x02 \x01(\x08\"\xc2\x02\n\x05Shelf\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1f\n\x04pose\x18\x03 \x01(\x0b\x32\x11.kachaka_api.Pose\x12$\n\x04size\x18\x04 \x01(\x0b\x32\x16.kachaka_api.ShelfSize\x12\x30\n\nappearance\x18\x05 \x01(\x0e\x32\x1c.kachaka_api.ShelfAppearance\x12\x39\n\x12recognizable_names\x18\x07 \x03(\x0b\x32\x1d.kachaka_api.RecognizableName\x12\x18\n\x10home_location_id\x18\x08 \x01(\t\x12/\n\nspeed_mode\x18\t \x01(\x0e\x32\x1b.kachaka_api.ShelfSpeedMode\x12 \n\x18ignore_voice_recognition\x18\n \x01(\x08\"\xae\x02\n\x06RosImu\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12,\n\x0borientation\x18\x02 \x01(\x0b\x32\x17.kachaka_api.Quaternion\x12\x1e\n\x16orientation_covariance\x18\x03 \x03(\x01\x12.\n\x10\x61ngular_velocity\x18\x04 \x01(\x0b\x32\x14.kachaka_api.Vector3\x12#\n\x1b\x61ngular_velocity_covariance\x18\x05 \x03(\x01\x12\x31\n\x13linear_acceleration\x18\x06 \x01(\x0b\x32\x14.kachaka_api.Vector3\x12&\n\x1elinear_acceleration_covariance\x18\x07 \x03(\x01\"\xaf\x01\n\x0bRosOdometry\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x16\n\x0e\x63hild_frame_id\x18\x02 \x01(\t\x12/\n\x04pose\x18\x03 \x01(\x0b\x32!.kachaka_api.Pose3dWithCovariance\x12/\n\x05twist\x18\x04 \x01(\x0b\x32 .kachaka_api.TwistWithCovariance\"\xeb\x01\n\x0cRosLaserScan\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x11\n\tangle_min\x18\x02 \x01(\x01\x12\x11\n\tangle_max\x18\x03 \x01(\x01\x12\x17\n\x0f\x61ngle_increment\x18\x04 \x01(\x01\x12\x16\n\x0etime_increment\x18\x05 \x01(\x01\x12\x11\n\tscan_time\x18\x06 \x01(\x01\x12\x11\n\trange_min\x18\x07 \x01(\x01\x12\x11\n\trange_max\x18\x08 \x01(\x01\x12\x0e\n\x06ranges\x18\t \x03(\x01\x12\x13\n\x0bintensities\x18\n \x03(\x01\"i\n\x10RegionOfInterest\x12\x10\n\x08x_offset\x18\x01 \x01(\r\x12\x10\n\x08y_offset\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\r\n\x05width\x18\x04 \x01(\r\x12\x12\n\ndo_rectify\x18\x05 \x01(\x08\"\xee\x01\n\rRosCameraInfo\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x18\n\x10\x64istortion_model\x18\x04 \x01(\t\x12\t\n\x01\x44\x18\x05 \x03(\x01\x12\t\n\x01K\x18\x06 \x03(\x01\x12\t\n\x01R\x18\x07 \x03(\x01\x12\t\n\x01P\x18\x08 \x03(\x01\x12\x11\n\tbinning_x\x18\t \x01(\r\x12\x11\n\tbinning_y\x18\n \x01(\r\x12*\n\x03roi\x18\x0b \x01(\x0b\x32\x1d.kachaka_api.RegionOfInterest\"\x95\x01\n\x08RosImage\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x10\n\x08\x65ncoding\x18\x04 \x01(\t\x12\x14\n\x0cis_bigendian\x18\x05 \x01(\x08\x12\x0c\n\x04step\x18\x06 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c\"\xab\x01\n\x13RosTransformStamped\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x16\n\x0e\x63hild_frame_id\x18\x02 \x01(\t\x12)\n\x0btranslation\x18\x03 \x01(\x0b\x32\x14.kachaka_api.Vector3\x12)\n\x08rotation\x18\x04 \x01(\x0b\x32\x17.kachaka_api.Quaternion\"Z\n\x12RosCompressedImage\x12&\n\x06header\x18\x01 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"t\n\x0fObjectDetection\x12\r\n\x05label\x18\x01 \x01(\r\x12*\n\x03roi\x18\x02 \x01(\x0b\x32\x1d.kachaka_api.RegionOfInterest\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x17\n\x0f\x64istance_median\x18\x04 \x01(\x01\"D\n\x17ObjectDetectionFeatures\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05shape\x18\x02 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x02\"\xbd\x04\n\x07\x43ommand\x12;\n\x12move_shelf_command\x18\x01 \x01(\x0b\x32\x1d.kachaka_api.MoveShelfCommandH\x00\x12?\n\x14return_shelf_command\x18\x02 \x01(\x0b\x32\x1f.kachaka_api.ReturnShelfCommandH\x00\x12?\n\x14undock_shelf_command\x18\x05 \x01(\x0b\x32\x1f.kachaka_api.UndockShelfCommandH\x00\x12\x46\n\x18move_to_location_command\x18\x07 \x01(\x0b\x32\".kachaka_api.MoveToLocationCommandH\x00\x12=\n\x13return_home_command\x18\x08 \x01(\x0b\x32\x1e.kachaka_api.ReturnHomeCommandH\x00\x12;\n\x12\x64ock_shelf_command\x18\t \x01(\x0b\x32\x1d.kachaka_api.DockShelfCommandH\x00\x12\x32\n\rspeak_command\x18\x0c \x01(\x0b\x32\x19.kachaka_api.SpeakCommandH\x00\x12>\n\x14move_to_pose_command\x18\r \x01(\x0b\x32\x1e.kachaka_api.MoveToPoseCommandH\x00\x12\x30\n\x0clock_command\x18\x0f \x01(\x0b\x32\x18.kachaka_api.LockCommandH\x00\x42\t\n\x07\x63ommand\"L\n\x10MoveShelfCommand\x12\x17\n\x0ftarget_shelf_id\x18\x01 \x01(\t\x12\x1f\n\x17\x64\x65stination_location_id\x18\x02 \x01(\t\"-\n\x12ReturnShelfCommand\x12\x17\n\x0ftarget_shelf_id\x18\x01 \x01(\t\"-\n\x12UndockShelfCommand\x12\x17\n\x0ftarget_shelf_id\x18\x01 \x01(\t\"3\n\x15MoveToLocationCommand\x12\x1a\n\x12target_location_id\x18\x01 \x01(\t\"\x13\n\x11ReturnHomeCommand\"\x12\n\x10\x44ockShelfCommand\"\x1c\n\x0cSpeakCommand\x12\x0c\n\x04text\x18\x01 \x01(\t\"6\n\x11MoveToPoseCommand\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0b\n\x03yaw\x18\x03 \x01(\x01\"#\n\x0bLockCommand\x12\x14\n\x0c\x64uration_sec\x18\x01 \x01(\x01\"\x0e\n\x0c\x45mptyRequest\"5\n\nGetRequest\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\"^\n\x1cGetRobotSerialNumberResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x15\n\rserial_number\x18\x02 \x01(\t\"S\n\x17GetRobotVersionResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x0f\n\x07version\x18\x02 \x01(\t\"`\n\x14GetRobotPoseResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x1f\n\x04pose\x18\x02 \x01(\x0b\x32\x11.kachaka_api.Pose\"\x9c\x01\n\x16GetBatteryInfoResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x1c\n\x14remaining_percentage\x18\x02 \x01(\x01\x12;\n\x13power_supply_status\x18\x03 \x01(\x0e\x32\x1e.kachaka_api.PowerSupplyStatus\"[\n\x11GetPngMapResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x1d\n\x03map\x18\x02 \x01(\x0b\x32\x10.kachaka_api.Map\"\x9c\x01\n\x1aGetObjectDetectionResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12&\n\x06header\x18\x02 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12-\n\x07objects\x18\x03 \x03(\x0b\x32\x1c.kachaka_api.ObjectDetection\"\xad\x01\n\"GetObjectDetectionFeaturesResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12&\n\x06header\x18\x02 \x01(\x0b\x32\x16.kachaka_api.RosHeader\x12\x36\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32$.kachaka_api.ObjectDetectionFeatures\"^\n\x11GetRosImuResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12 \n\x03imu\x18\x02 \x01(\x0b\x32\x13.kachaka_api.RosImu\"m\n\x16GetRosOdometryResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12*\n\x08odometry\x18\x02 \x01(\x0b\x32\x18.kachaka_api.RosOdometry\"k\n\x17GetRosLaserScanResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\'\n\x04scan\x18\x02 \x01(\x0b\x32\x19.kachaka_api.RosLaserScan\"\x7f\n#GetFrontCameraRosCameraInfoResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12/\n\x0b\x63\x61mera_info\x18\x02 \x01(\x0b\x32\x1a.kachaka_api.RosCameraInfo\"o\n\x1eGetFrontCameraRosImageResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12$\n\x05image\x18\x02 \x01(\x0b\x32\x15.kachaka_api.RosImage\"\x83\x01\n(GetFrontCameraRosCompressedImageResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12.\n\x05image\x18\x02 \x01(\x0b\x32\x1f.kachaka_api.RosCompressedImage\"~\n\"GetBackCameraRosCameraInfoResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12/\n\x0b\x63\x61mera_info\x18\x02 \x01(\x0b\x32\x1a.kachaka_api.RosCameraInfo\"n\n\x1dGetBackCameraRosImageResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12$\n\x05image\x18\x02 \x01(\x0b\x32\x15.kachaka_api.RosImage\"\x82\x01\n\'GetBackCameraRosCompressedImageResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12.\n\x05image\x18\x02 \x01(\x0b\x32\x1f.kachaka_api.RosCompressedImage\"}\n!GetTofCameraRosCameraInfoResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12/\n\x0b\x63\x61mera_info\x18\x02 \x01(\x0b\x32\x1a.kachaka_api.RosCameraInfo\"\x83\x01\n\x1cGetTofCameraRosImageResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12$\n\x05image\x18\x02 \x01(\x0b\x32\x15.kachaka_api.RosImage\x12\x14\n\x0cis_available\x18\x03 \x01(\x08\"\x97\x01\n&GetTofCameraRosCompressedImageResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12.\n\x05image\x18\x02 \x01(\x0b\x32\x1f.kachaka_api.RosCompressedImage\x12\x14\n\x0cis_available\x18\x03 \x01(\x08\"\x8b\x01\n\x13StartCommandRequest\x12%\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x14.kachaka_api.Command\x12\x12\n\ncancel_all\x18\x02 \x01(\x08\x12\x16\n\x0etts_on_success\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x12\n\ndeferrable\x18\x05 \x01(\x08\"O\n\x14StartCommandResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\x12\x12\n\ncommand_id\x18\x02 \x01(\t\"c\n\x15\x43\x61ncelCommandResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\x12%\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x14.kachaka_api.Command\"\xa7\x01\n\x17GetCommandStateResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12(\n\x05state\x18\x02 \x01(\x0e\x32\x19.kachaka_api.CommandState\x12%\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x14.kachaka_api.Command\x12\x12\n\ncommand_id\x18\x04 \x01(\t\"\xa7\x01\n\x1cGetLastCommandResultResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12#\n\x06result\x18\x02 \x01(\x0b\x32\x13.kachaka_api.Result\x12%\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\x14.kachaka_api.Command\x12\x12\n\ncommand_id\x18\x04 \x01(\t\"6\n\x0fProceedResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"\x86\x01\n\x14GetLocationsResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12(\n\tlocations\x18\x02 \x03(\x0b\x32\x15.kachaka_api.Location\x12\x1b\n\x13\x64\x65\x66\x61ult_location_id\x18\x03 \x01(\t\"b\n\x12GetShelvesResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12#\n\x07shelves\x18\x02 \x03(\x0b\x32\x12.kachaka_api.Shelf\"U\n\x18GetMovingShelfIdResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x10\n\x08shelf_id\x18\x02 \x01(\t\")\n\x15ResetShelfPoseRequest\x12\x10\n\x08shelf_id\x18\x01 \x01(\t\"=\n\x16ResetShelfPoseResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"-\n\x1bSetAutoHomingEnabledRequest\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"C\n\x1cSetAutoHomingEnabledResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"X\n\x1cGetAutoHomingEnabledResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"P\n\x1eSetManualControlEnabledRequest\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x1e\n\x16use_shelf_registration\x18\x02 \x01(\x08\"F\n\x1fSetManualControlEnabledResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"[\n\x1fGetManualControlEnabledResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"2\n\x1dSetFrontTorchIntensityRequest\x12\x11\n\tintensity\x18\x01 \x01(\x05\"E\n\x1eSetFrontTorchIntensityResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"1\n\x1cSetBackTorchIntensityRequest\x12\x11\n\tintensity\x18\x01 \x01(\x05\"D\n\x1dSetBackTorchIntensityResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\":\n\x17SetRobotVelocityRequest\x12\x0e\n\x06linear\x18\x01 \x01(\x01\x12\x0f\n\x07\x61ngular\x18\x02 \x01(\x01\"?\n\x18SetRobotVelocityResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"0\n\x18\x41\x63tivateLaserScanRequest\x12\x14\n\x0c\x64uration_sec\x18\x01 \x01(\x01\"@\n\x19\x41\x63tivateLaserScanResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\"{\n\x1aGetStaticTransformResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x34\n\ntransforms\x18\x02 \x03(\x0b\x32 .kachaka_api.RosTransformStamped\"S\n\x1bGetDynamicTransformResponse\x12\x34\n\ntransforms\x18\x01 \x03(\x0b\x32 .kachaka_api.RosTransformStamped\"(\n\x0cMapListEntry\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x12GetMapListResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\x33\n\x10map_list_entries\x18\x02 \x03(\x0b\x32\x19.kachaka_api.MapListEntry\"N\n\x17GetCurrentMapIdResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\n\n\x02id\x18\x02 \x01(\t\"\'\n\x15LoadMapPreviewRequest\x12\x0e\n\x06map_id\x18\x01 \x01(\t\"\\\n\x16LoadMapPreviewResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\x12\x1d\n\x03map\x18\x02 \x01(\x0b\x32\x10.kachaka_api.Map\"\"\n\x10\x45xportMapRequest\x12\x0e\n\x06map_id\x18\x01 \x01(\t\"\x83\x02\n\x11\x45xportMapResponse\x12I\n\x10middle_of_stream\x18\x01 \x01(\x0b\x32-.kachaka_api.ExportMapResponse.MiddleOfStreamH\x00\x12\x43\n\rend_of_stream\x18\x02 \x01(\x0b\x32*.kachaka_api.ExportMapResponse.EndOfStreamH\x00\x1a\x1e\n\x0eMiddleOfStream\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x1a\x32\n\x0b\x45ndOfStream\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.ResultB\n\n\x08response\" \n\x10ImportMapRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"H\n\x11ImportMapResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.kachaka_api.Result\x12\x0e\n\x06map_id\x18\x02 \x01(\t\"\x80\x01\n\x07History\x12\n\n\x02id\x18\x01 \x01(\t\x12%\n\x07\x63ommand\x18\x04 \x01(\x0b\x32\x14.kachaka_api.Command\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\x12\n\nerror_code\x18\x06 \x01(\x05\x12\x1d\n\x15\x63ommand_executed_time\x18\x07 \x01(\x03\"j\n\x16GetHistoryListResponse\x12\'\n\x08metadata\x18\x01 \x01(\x0b\x32\x15.kachaka_api.Metadata\x12\'\n\thistories\x18\x02 \x03(\x0b\x32\x14.kachaka_api.History*\xc3\x01\n\x11PowerSupplyStatus\x12#\n\x1fPOWER_SUPPLY_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1cPOWER_SUPPLY_STATUS_CHARGING\x10\x01\x12#\n\x1fPOWER_SUPPLY_STATUS_DISCHARGING\x10\x02\x12$\n POWER_SUPPLY_STATUS_NOT_CHARGING\x10\x03\x12\x1c\n\x18POWER_SUPPLY_STATUS_FULL\x10\x04*f\n\x0cLocationType\x12\x1d\n\x19LOCATION_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15LOCATION_TYPE_CHARGER\x10\x01\x12\x1c\n\x18LOCATION_TYPE_SHELF_HOME\x10\x02*\xd4\x01\n\x0fShelfAppearance\x12 \n\x1cSHELF_APPEARANCE_UNSPECIFIED\x10\x00\x12\"\n\x1eSHELF_APPEARANCE_DEFAULT_SHELF\x10\x01\x12+\n\'SHELF_APPEARANCE_KACHAKA_SHELF_3DRAWERS\x10\x02\x12+\n\'SHELF_APPEARANCE_KACHAKA_SHELF_2DRAWERS\x10\x03\x12!\n\x1dSHELF_APPEARANCE_KACHAKA_BASE\x10\x08*i\n\x0eShelfSpeedMode\x12 \n\x1cSHELF_SPEED_MODE_UNSPECIFIED\x10\x00\x12\x18\n\x14SHELF_SPEED_MODE_LOW\x10\x01\x12\x1b\n\x17SHELF_SPEED_MODE_NORMAL\x10\x02*\x8d\x01\n\x0bObjectLabel\x12\x1c\n\x18OBJECT_LABEL_UNSPECIFIED\x10\x00\x12\x17\n\x13OBJECT_LABEL_PERSON\x10\x01\x12\x16\n\x12OBJECT_LABEL_SHELF\x10\x02\x12\x18\n\x14OBJECT_LABEL_CHARGER\x10\x03\x12\x15\n\x11OBJECT_LABEL_DOOR\x10\x04*c\n\x0c\x43ommandState\x12\x1d\n\x19\x43OMMAND_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43OMMAND_STATE_PENDING\x10\x01\x12\x19\n\x15\x43OMMAND_STATE_RUNNING\x10\x02\x32\xa6\x1f\n\nKachakaApi\x12Z\n\x14GetRobotSerialNumber\x12\x17.kachaka_api.GetRequest\x1a).kachaka_api.GetRobotSerialNumberResponse\x12P\n\x0fGetRobotVersion\x12\x17.kachaka_api.GetRequest\x1a$.kachaka_api.GetRobotVersionResponse\x12J\n\x0cGetRobotPose\x12\x17.kachaka_api.GetRequest\x1a!.kachaka_api.GetRobotPoseResponse\x12N\n\x0eGetBatteryInfo\x12\x17.kachaka_api.GetRequest\x1a#.kachaka_api.GetBatteryInfoResponse\x12\x44\n\tGetPngMap\x12\x17.kachaka_api.GetRequest\x1a\x1e.kachaka_api.GetPngMapResponse\x12V\n\x12GetObjectDetection\x12\x17.kachaka_api.GetRequest\x1a\'.kachaka_api.GetObjectDetectionResponse\x12\x66\n\x1aGetObjectDetectionFeatures\x12\x17.kachaka_api.GetRequest\x1a/.kachaka_api.GetObjectDetectionFeaturesResponse\x12\x44\n\tGetRosImu\x12\x17.kachaka_api.GetRequest\x1a\x1e.kachaka_api.GetRosImuResponse\x12N\n\x0eGetRosOdometry\x12\x17.kachaka_api.GetRequest\x1a#.kachaka_api.GetRosOdometryResponse\x12P\n\x0fGetRosLaserScan\x12\x17.kachaka_api.GetRequest\x1a$.kachaka_api.GetRosLaserScanResponse\x12h\n\x1bGetFrontCameraRosCameraInfo\x12\x17.kachaka_api.GetRequest\x1a\x30.kachaka_api.GetFrontCameraRosCameraInfoResponse\x12^\n\x16GetFrontCameraRosImage\x12\x17.kachaka_api.GetRequest\x1a+.kachaka_api.GetFrontCameraRosImageResponse\x12r\n GetFrontCameraRosCompressedImage\x12\x17.kachaka_api.GetRequest\x1a\x35.kachaka_api.GetFrontCameraRosCompressedImageResponse\x12\x66\n\x1aGetBackCameraRosCameraInfo\x12\x17.kachaka_api.GetRequest\x1a/.kachaka_api.GetBackCameraRosCameraInfoResponse\x12\\\n\x15GetBackCameraRosImage\x12\x17.kachaka_api.GetRequest\x1a*.kachaka_api.GetBackCameraRosImageResponse\x12p\n\x1fGetBackCameraRosCompressedImage\x12\x17.kachaka_api.GetRequest\x1a\x34.kachaka_api.GetBackCameraRosCompressedImageResponse\x12\x64\n\x19GetTofCameraRosCameraInfo\x12\x17.kachaka_api.GetRequest\x1a..kachaka_api.GetTofCameraRosCameraInfoResponse\x12Z\n\x14GetTofCameraRosImage\x12\x17.kachaka_api.GetRequest\x1a).kachaka_api.GetTofCameraRosImageResponse\x12n\n\x1eGetTofCameraRosCompressedImage\x12\x17.kachaka_api.GetRequest\x1a\x33.kachaka_api.GetTofCameraRosCompressedImageResponse\x12S\n\x0cStartCommand\x12 .kachaka_api.StartCommandRequest\x1a!.kachaka_api.StartCommandResponse\x12N\n\rCancelCommand\x12\x19.kachaka_api.EmptyRequest\x1a\".kachaka_api.CancelCommandResponse\x12P\n\x0fGetCommandState\x12\x17.kachaka_api.GetRequest\x1a$.kachaka_api.GetCommandStateResponse\x12Z\n\x14GetLastCommandResult\x12\x17.kachaka_api.GetRequest\x1a).kachaka_api.GetLastCommandResultResponse\x12\x42\n\x07Proceed\x12\x19.kachaka_api.EmptyRequest\x1a\x1c.kachaka_api.ProceedResponse\x12J\n\x0cGetLocations\x12\x17.kachaka_api.GetRequest\x1a!.kachaka_api.GetLocationsResponse\x12\x46\n\nGetShelves\x12\x17.kachaka_api.GetRequest\x1a\x1f.kachaka_api.GetShelvesResponse\x12R\n\x10GetMovingShelfId\x12\x17.kachaka_api.GetRequest\x1a%.kachaka_api.GetMovingShelfIdResponse\x12Y\n\x0eResetShelfPose\x12\".kachaka_api.ResetShelfPoseRequest\x1a#.kachaka_api.ResetShelfPoseResponse\x12k\n\x14SetAutoHomingEnabled\x12(.kachaka_api.SetAutoHomingEnabledRequest\x1a).kachaka_api.SetAutoHomingEnabledResponse\x12Z\n\x14GetAutoHomingEnabled\x12\x17.kachaka_api.GetRequest\x1a).kachaka_api.GetAutoHomingEnabledResponse\x12t\n\x17SetManualControlEnabled\x12+.kachaka_api.SetManualControlEnabledRequest\x1a,.kachaka_api.SetManualControlEnabledResponse\x12`\n\x17GetManualControlEnabled\x12\x17.kachaka_api.GetRequest\x1a,.kachaka_api.GetManualControlEnabledResponse\x12q\n\x16SetFrontTorchIntensity\x12*.kachaka_api.SetFrontTorchIntensityRequest\x1a+.kachaka_api.SetFrontTorchIntensityResponse\x12n\n\x15SetBackTorchIntensity\x12).kachaka_api.SetBackTorchIntensityRequest\x1a*.kachaka_api.SetBackTorchIntensityResponse\x12_\n\x10SetRobotVelocity\x12$.kachaka_api.SetRobotVelocityRequest\x1a%.kachaka_api.SetRobotVelocityResponse\x12\x62\n\x11\x41\x63tivateLaserScan\x12%.kachaka_api.ActivateLaserScanRequest\x1a&.kachaka_api.ActivateLaserScanResponse\x12\x46\n\nGetMapList\x12\x17.kachaka_api.GetRequest\x1a\x1f.kachaka_api.GetMapListResponse\x12P\n\x0fGetCurrentMapId\x12\x17.kachaka_api.GetRequest\x1a$.kachaka_api.GetCurrentMapIdResponse\x12Y\n\x0eLoadMapPreview\x12\".kachaka_api.LoadMapPreviewRequest\x1a#.kachaka_api.LoadMapPreviewResponse\x12L\n\tExportMap\x12\x1d.kachaka_api.ExportMapRequest\x1a\x1e.kachaka_api.ExportMapResponse0\x01\x12L\n\tImportMap\x12\x1d.kachaka_api.ImportMapRequest\x1a\x1e.kachaka_api.ImportMapResponse(\x01\x12N\n\x0eGetHistoryList\x12\x17.kachaka_api.GetRequest\x1a#.kachaka_api.GetHistoryListResponse\x12V\n\x12GetStaticTransform\x12\x17.kachaka_api.GetRequest\x1a\'.kachaka_api.GetStaticTransformResponse\x12\\\n\x13GetDynamicTransform\x12\x19.kachaka_api.EmptyRequest\x1a(.kachaka_api.GetDynamicTransformResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kachaka_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POWERSUPPLYSTATUS']._serialized_start=9834
  _globals['_POWERSUPPLYSTATUS']._serialized_end=10029
  _globals['_LOCATIONTYPE']._serialized_start=10031
  _globals['_LOCATIONTYPE']._serialized_end=10133
  _globals['_SHELFAPPEARANCE']._serialized_start=10136
  _globals['_SHELFAPPEARANCE']._serialized_end=10348
  _globals['_SHELFSPEEDMODE']._serialized_start=10350
  _globals['_SHELFSPEEDMODE']._serialized_end=10455
  _globals['_OBJECTLABEL']._serialized_start=10458
  _globals['_OBJECTLABEL']._serialized_end=10599
  _globals['_COMMANDSTATE']._serialized_start=10601
  _globals['_COMMANDSTATE']._serialized_end=10700
  _globals['_METADATA']._serialized_start=34
  _globals['_METADATA']._serialized_end=60
  _globals['_RESULT']._serialized_start=62
  _globals['_RESULT']._serialized_end=107
  _globals['_ERROR']._serialized_start=109
  _globals['_ERROR']._serialized_end=136
  _globals['_ROSHEADER']._serialized_start=138
  _globals['_ROSHEADER']._serialized_end=187
  _globals['_POSE']._serialized_start=189
  _globals['_POSE']._serialized_end=232
  _globals['_VECTOR3']._serialized_start=234
  _globals['_VECTOR3']._serialized_end=276
  _globals['_QUATERNION']._serialized_start=278
  _globals['_QUATERNION']._serialized_end=334
  _globals['_POSE3D']._serialized_start=336
  _globals['_POSE3D']._serialized_end=430
  _globals['_TWIST']._serialized_start=432
  _globals['_TWIST']._serialized_end=516
  _globals['_POSE3DWITHCOVARIANCE']._serialized_start=518
  _globals['_POSE3DWITHCOVARIANCE']._serialized_end=595
  _globals['_TWISTWITHCOVARIANCE']._serialized_start=597
  _globals['_TWISTWITHCOVARIANCE']._serialized_end=673
  _globals['_MAP']._serialized_start=675
  _globals['_MAP']._serialized_end=794
  _globals['_LOCATION']._serialized_start=797
  _globals['_LOCATION']._serialized_end=1021
  _globals['_SHELFSIZE']._serialized_start=1023
  _globals['_SHELFSIZE']._serialized_end=1080
  _globals['_RECOGNIZABLENAME']._serialized_start=1082
  _globals['_RECOGNIZABLENAME']._serialized_end=1133
  _globals['_SHELF']._serialized_start=1136
  _globals['_SHELF']._serialized_end=1458
  _globals['_ROSIMU']._serialized_start=1461
  _globals['_ROSIMU']._serialized_end=1763
  _globals['_ROSODOMETRY']._serialized_start=1766
  _globals['_ROSODOMETRY']._serialized_end=1941
  _globals['_ROSLASERSCAN']._serialized_start=1944
  _globals['_ROSLASERSCAN']._serialized_end=2179
  _globals['_REGIONOFINTEREST']._serialized_start=2181
  _globals['_REGIONOFINTEREST']._serialized_end=2286
  _globals['_ROSCAMERAINFO']._serialized_start=2289
  _globals['_ROSCAMERAINFO']._serialized_end=2527
  _globals['_ROSIMAGE']._serialized_start=2530
  _globals['_ROSIMAGE']._serialized_end=2679
  _globals['_ROSTRANSFORMSTAMPED']._serialized_start=2682
  _globals['_ROSTRANSFORMSTAMPED']._serialized_end=2853
  _globals['_ROSCOMPRESSEDIMAGE']._serialized_start=2855
  _globals['_ROSCOMPRESSEDIMAGE']._serialized_end=2945
  _globals['_OBJECTDETECTION']._serialized_start=2947
  _globals['_OBJECTDETECTION']._serialized_end=3063
  _globals['_OBJECTDETECTIONFEATURES']._serialized_start=3065
  _globals['_OBJECTDETECTIONFEATURES']._serialized_end=3133
  _globals['_COMMAND']._serialized_start=3136
  _globals['_COMMAND']._serialized_end=3709
  _globals['_MOVESHELFCOMMAND']._serialized_start=3711
  _globals['_MOVESHELFCOMMAND']._serialized_end=3787
  _globals['_RETURNSHELFCOMMAND']._serialized_start=3789
  _globals['_RETURNSHELFCOMMAND']._serialized_end=3834
  _globals['_UNDOCKSHELFCOMMAND']._serialized_start=3836
  _globals['_UNDOCKSHELFCOMMAND']._serialized_end=3881
  _globals['_MOVETOLOCATIONCOMMAND']._serialized_start=3883
  _globals['_MOVETOLOCATIONCOMMAND']._serialized_end=3934
  _globals['_RETURNHOMECOMMAND']._serialized_start=3936
  _globals['_RETURNHOMECOMMAND']._serialized_end=3955
  _globals['_DOCKSHELFCOMMAND']._serialized_start=3957
  _globals['_DOCKSHELFCOMMAND']._serialized_end=3975
  _globals['_SPEAKCOMMAND']._serialized_start=3977
  _globals['_SPEAKCOMMAND']._serialized_end=4005
  _globals['_MOVETOPOSECOMMAND']._serialized_start=4007
  _globals['_MOVETOPOSECOMMAND']._serialized_end=4061
  _globals['_LOCKCOMMAND']._serialized_start=4063
  _globals['_LOCKCOMMAND']._serialized_end=4098
  _globals['_EMPTYREQUEST']._serialized_start=4100
  _globals['_EMPTYREQUEST']._serialized_end=4114
  _globals['_GETREQUEST']._serialized_start=4116
  _globals['_GETREQUEST']._serialized_end=4169
  _globals['_GETROBOTSERIALNUMBERRESPONSE']._serialized_start=4171
  _globals['_GETROBOTSERIALNUMBERRESPONSE']._serialized_end=4265
  _globals['_GETROBOTVERSIONRESPONSE']._serialized_start=4267
  _globals['_GETROBOTVERSIONRESPONSE']._serialized_end=4350
  _globals['_GETROBOTPOSERESPONSE']._serialized_start=4352
  _globals['_GETROBOTPOSERESPONSE']._serialized_end=4448
  _globals['_GETBATTERYINFORESPONSE']._serialized_start=4451
  _globals['_GETBATTERYINFORESPONSE']._serialized_end=4607
  _globals['_GETPNGMAPRESPONSE']._serialized_start=4609
  _globals['_GETPNGMAPRESPONSE']._serialized_end=4700
  _globals['_GETOBJECTDETECTIONRESPONSE']._serialized_start=4703
  _globals['_GETOBJECTDETECTIONRESPONSE']._serialized_end=4859
  _globals['_GETOBJECTDETECTIONFEATURESRESPONSE']._serialized_start=4862
  _globals['_GETOBJECTDETECTIONFEATURESRESPONSE']._serialized_end=5035
  _globals['_GETROSIMURESPONSE']._serialized_start=5037
  _globals['_GETROSIMURESPONSE']._serialized_end=5131
  _globals['_GETROSODOMETRYRESPONSE']._serialized_start=5133
  _globals['_GETROSODOMETRYRESPONSE']._serialized_end=5242
  _globals['_GETROSLASERSCANRESPONSE']._serialized_start=5244
  _globals['_GETROSLASERSCANRESPONSE']._serialized_end=5351
  _globals['_GETFRONTCAMERAROSCAMERAINFORESPONSE']._serialized_start=5353
  _globals['_GETFRONTCAMERAROSCAMERAINFORESPONSE']._serialized_end=5480
  _globals['_GETFRONTCAMERAROSIMAGERESPONSE']._serialized_start=5482
  _globals['_GETFRONTCAMERAROSIMAGERESPONSE']._serialized_end=5593
  _globals['_GETFRONTCAMERAROSCOMPRESSEDIMAGERESPONSE']._serialized_start=5596
  _globals['_GETFRONTCAMERAROSCOMPRESSEDIMAGERESPONSE']._serialized_end=5727
  _globals['_GETBACKCAMERAROSCAMERAINFORESPONSE']._serialized_start=5729
  _globals['_GETBACKCAMERAROSCAMERAINFORESPONSE']._serialized_end=5855
  _globals['_GETBACKCAMERAROSIMAGERESPONSE']._serialized_start=5857
  _globals['_GETBACKCAMERAROSIMAGERESPONSE']._serialized_end=5967
  _globals['_GETBACKCAMERAROSCOMPRESSEDIMAGERESPONSE']._serialized_start=5970
  _globals['_GETBACKCAMERAROSCOMPRESSEDIMAGERESPONSE']._serialized_end=6100
  _globals['_GETTOFCAMERAROSCAMERAINFORESPONSE']._serialized_start=6102
  _globals['_GETTOFCAMERAROSCAMERAINFORESPONSE']._serialized_end=6227
  _globals['_GETTOFCAMERAROSIMAGERESPONSE']._serialized_start=6230
  _globals['_GETTOFCAMERAROSIMAGERESPONSE']._serialized_end=6361
  _globals['_GETTOFCAMERAROSCOMPRESSEDIMAGERESPONSE']._serialized_start=6364
  _globals['_GETTOFCAMERAROSCOMPRESSEDIMAGERESPONSE']._serialized_end=6515
  _globals['_STARTCOMMANDREQUEST']._serialized_start=6518
  _globals['_STARTCOMMANDREQUEST']._serialized_end=6657
  _globals['_STARTCOMMANDRESPONSE']._serialized_start=6659
  _globals['_STARTCOMMANDRESPONSE']._serialized_end=6738
  _globals['_CANCELCOMMANDRESPONSE']._serialized_start=6740
  _globals['_CANCELCOMMANDRESPONSE']._serialized_end=6839
  _globals['_GETCOMMANDSTATERESPONSE']._serialized_start=6842
  _globals['_GETCOMMANDSTATERESPONSE']._serialized_end=7009
  _globals['_GETLASTCOMMANDRESULTRESPONSE']._serialized_start=7012
  _globals['_GETLASTCOMMANDRESULTRESPONSE']._serialized_end=7179
  _globals['_PROCEEDRESPONSE']._serialized_start=7181
  _globals['_PROCEEDRESPONSE']._serialized_end=7235
  _globals['_GETLOCATIONSRESPONSE']._serialized_start=7238
  _globals['_GETLOCATIONSRESPONSE']._serialized_end=7372
  _globals['_GETSHELVESRESPONSE']._serialized_start=7374
  _globals['_GETSHELVESRESPONSE']._serialized_end=7472
  _globals['_GETMOVINGSHELFIDRESPONSE']._serialized_start=7474
  _globals['_GETMOVINGSHELFIDRESPONSE']._serialized_end=7559
  _globals['_RESETSHELFPOSEREQUEST']._serialized_start=7561
  _globals['_RESETSHELFPOSEREQUEST']._serialized_end=7602
  _globals['_RESETSHELFPOSERESPONSE']._serialized_start=7604
  _globals['_RESETSHELFPOSERESPONSE']._serialized_end=7665
  _globals['_SETAUTOHOMINGENABLEDREQUEST']._serialized_start=7667
  _globals['_SETAUTOHOMINGENABLEDREQUEST']._serialized_end=7712
  _globals['_SETAUTOHOMINGENABLEDRESPONSE']._serialized_start=7714
  _globals['_SETAUTOHOMINGENABLEDRESPONSE']._serialized_end=7781
  _globals['_GETAUTOHOMINGENABLEDRESPONSE']._serialized_start=7783
  _globals['_GETAUTOHOMINGENABLEDRESPONSE']._serialized_end=7871
  _globals['_SETMANUALCONTROLENABLEDREQUEST']._serialized_start=7873
  _globals['_SETMANUALCONTROLENABLEDREQUEST']._serialized_end=7953
  _globals['_SETMANUALCONTROLENABLEDRESPONSE']._serialized_start=7955
  _globals['_SETMANUALCONTROLENABLEDRESPONSE']._serialized_end=8025
  _globals['_GETMANUALCONTROLENABLEDRESPONSE']._serialized_start=8027
  _globals['_GETMANUALCONTROLENABLEDRESPONSE']._serialized_end=8118
  _globals['_SETFRONTTORCHINTENSITYREQUEST']._serialized_start=8120
  _globals['_SETFRONTTORCHINTENSITYREQUEST']._serialized_end=8170
  _globals['_SETFRONTTORCHINTENSITYRESPONSE']._serialized_start=8172
  _globals['_SETFRONTTORCHINTENSITYRESPONSE']._serialized_end=8241
  _globals['_SETBACKTORCHINTENSITYREQUEST']._serialized_start=8243
  _globals['_SETBACKTORCHINTENSITYREQUEST']._serialized_end=8292
  _globals['_SETBACKTORCHINTENSITYRESPONSE']._serialized_start=8294
  _globals['_SETBACKTORCHINTENSITYRESPONSE']._serialized_end=8362
  _globals['_SETROBOTVELOCITYREQUEST']._serialized_start=8364
  _globals['_SETROBOTVELOCITYREQUEST']._serialized_end=8422
  _globals['_SETROBOTVELOCITYRESPONSE']._serialized_start=8424
  _globals['_SETROBOTVELOCITYRESPONSE']._serialized_end=8487
  _globals['_ACTIVATELASERSCANREQUEST']._serialized_start=8489
  _globals['_ACTIVATELASERSCANREQUEST']._serialized_end=8537
  _globals['_ACTIVATELASERSCANRESPONSE']._serialized_start=8539
  _globals['_ACTIVATELASERSCANRESPONSE']._serialized_end=8603
  _globals['_GETSTATICTRANSFORMRESPONSE']._serialized_start=8605
  _globals['_GETSTATICTRANSFORMRESPONSE']._serialized_end=8728
  _globals['_GETDYNAMICTRANSFORMRESPONSE']._serialized_start=8730
  _globals['_GETDYNAMICTRANSFORMRESPONSE']._serialized_end=8813
  _globals['_MAPLISTENTRY']._serialized_start=8815
  _globals['_MAPLISTENTRY']._serialized_end=8855
  _globals['_GETMAPLISTRESPONSE']._serialized_start=8857
  _globals['_GETMAPLISTRESPONSE']._serialized_end=8971
  _globals['_GETCURRENTMAPIDRESPONSE']._serialized_start=8973
  _globals['_GETCURRENTMAPIDRESPONSE']._serialized_end=9051
  _globals['_LOADMAPPREVIEWREQUEST']._serialized_start=9053
  _globals['_LOADMAPPREVIEWREQUEST']._serialized_end=9092
  _globals['_LOADMAPPREVIEWRESPONSE']._serialized_start=9094
  _globals['_LOADMAPPREVIEWRESPONSE']._serialized_end=9186
  _globals['_EXPORTMAPREQUEST']._serialized_start=9188
  _globals['_EXPORTMAPREQUEST']._serialized_end=9222
  _globals['_EXPORTMAPRESPONSE']._serialized_start=9225
  _globals['_EXPORTMAPRESPONSE']._serialized_end=9484
  _globals['_EXPORTMAPRESPONSE_MIDDLEOFSTREAM']._serialized_start=9390
  _globals['_EXPORTMAPRESPONSE_MIDDLEOFSTREAM']._serialized_end=9420
  _globals['_EXPORTMAPRESPONSE_ENDOFSTREAM']._serialized_start=9422
  _globals['_EXPORTMAPRESPONSE_ENDOFSTREAM']._serialized_end=9472
  _globals['_IMPORTMAPREQUEST']._serialized_start=9486
  _globals['_IMPORTMAPREQUEST']._serialized_end=9518
  _globals['_IMPORTMAPRESPONSE']._serialized_start=9520
  _globals['_IMPORTMAPRESPONSE']._serialized_end=9592
  _globals['_HISTORY']._serialized_start=9595
  _globals['_HISTORY']._serialized_end=9723
  _globals['_GETHISTORYLISTRESPONSE']._serialized_start=9725
  _globals['_GETHISTORYLISTRESPONSE']._serialized_end=9831
  _globals['_KACHAKAAPI']._serialized_start=10703
  _globals['_KACHAKAAPI']._serialized_end=14709
# @@protoc_insertion_point(module_scope)
