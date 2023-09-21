#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/pose_with_covariance_stamped.hpp"

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("initialpose_publisher");

  // パブリッシャーを作成
  auto publisher = node->create_publisher<geometry_msgs::msg::PoseWithCovarianceStamped>("/initialpose", 10);

  // メッセージを作成
  auto message = std::make_shared<geometry_msgs::msg::PoseWithCovarianceStamped>();
  message->header.stamp.sec = 0;
  message->header.stamp.nanosec = 0;
  message->header.frame_id = "map";
  message->pose.pose.position.x = 0.0;
  message->pose.pose.position.y = 0.0;
  message->pose.pose.position.z = 0.0;
  message->pose.pose.orientation.x = 0.0;
  message->pose.pose.orientation.y = 0.0;
  message->pose.pose.orientation.z = 0.0;
  message->pose.pose.orientation.w = 0.0;

  // メッセージを一度だけパブリッシュ
  publisher->publish(*message);

  rclcpp::shutdown();
  return 0;
}

