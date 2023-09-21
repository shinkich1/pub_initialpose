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
