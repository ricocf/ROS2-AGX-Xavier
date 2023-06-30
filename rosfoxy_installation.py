import subprocess

subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'install', 'locales'])
subprocess.run(['sudo', 'locale-gen', 'en_US', 'en_US.UTF-8'])
subprocess.run(['sudo', 'update-locale', 'LC_ALL=en_US.UTF-8', 'LANG=en_US.UTF-8'])
subprocess.run(['export', 'LANG=en_US.UTF-8'])
subprocess.run(['sudo', 'apt', 'install', 'software-properties-common'])
subprocess.run(['sudo', 'add-apt-repository', 'universe'])


subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'install', 'curl', '-y'])

subprocess.run(['sudo', 'curl', '-sSL', 'https://raw.githubusercontent.com/ros/rosdistro/master/ros.key', '-o', '/usr/share/keyrings/ros-archive-keyring.gpg'])

ubuntu_codename = subprocess.run(['. /etc/os-release && echo $UBUNTU_CODENAME'], shell=True, capture_output=True, text=True).stdout.strip()
subprocess.run(['echo', f"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu {ubuntu_codename} main", '|', 'sudo', 'tee', '/etc/apt/sources.list.d/ros2.list', '>', '/dev/null'], shell=True)

subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'upgrade'])
subprocess.run(['sudo', 'apt', 'install', 'ros-foxy-desktop', 'python3-argcomplete'])
subprocess.run(['sudo', 'apt', 'install', 'ros-foxy-ros-base', 'python3-argcomplete'])
subprocess.run(['sudo', 'apt', 'install', 'ros-dev-tools'])
subprocess.run(['source', '/opt/ros/foxy/setup.bash'])
