FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    locales \
    software-properties-common \
    curl

# Configure locales
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG en_US.UTF-8

# Add ROS repository
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN ubuntu_codename=$(sh -c '. /etc/os-release && echo $UBUNTU_CODENAME') && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $ubuntu_codename main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    ros-foxy-desktop \
    ros-foxy-ros-base \
    ros-dev-tools \
    python3-argcomplete

# Source ROS environment
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

# Set the entrypoint to a shell prompt
CMD ["/bin/bash"]
