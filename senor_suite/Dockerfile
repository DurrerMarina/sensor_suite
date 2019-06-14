FROM duckietown/rpi-duckiebot-base:master18

RUN [ "cross-build-start" ]

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install DateTime
RUN apt-get install python-smbus
RUN apt-get install python-yaml
# RUN apt-get install ros-kinetic-message-generation
RUN apt-get install i2c-tools

#Copy the package
RUN mkdir -p /catkin_ws/src/sensor_suite
COPY sensor_suite /catkin_ws/src/sensor_suite
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash; cd /catkin_ws; catkin_make"

RUN [ "cross-build-end" ]

CMD /bin/bash -c "source /catkin_ws/devel/setup.bash; rosrun sensor_suite sensor_suite_scanner_node.py" ]
