import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pub_initialpose',  # ノードのパッケージ名を指定
            executable='publish_initialpose',  # ノードの実行可能ファイル名を指定
            output='screen',  # ログ出力設定
            name='pub_pose_node',  # ノード名を指定
            # 他のパラメーターやremappingを追加
            # 例: remappings=[('/input_topic', '/new_input_topic')]
            # 例: parameters=[{'param_name': 'param_value'}]
        ),
    ])



"""
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # 既存の launch ファイルのコンポーネントをここに追加

        # 新しいコマンドを実行するアクションを追加
        launch.actions.ExecuteProcess(
            cmd=["ros2", "topic", "pub", "-1", "/initialpose", "geometry_msgs/PoseWithCovarianceStamped",
                 "{ header: {stamp: {sec: 0, nanosec: 0}, frame_id: 'map'}, pose: { pose: {position: {x: 0.0, y: 0.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}}, } }"],
            output='screen',  # コマンドの出力をターミナルに表示
        )

    ])
"""
