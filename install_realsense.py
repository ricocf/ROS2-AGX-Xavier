import subprocess

try:
    subprocess.run(['sudo', 'apt-key', 'adv', '--keyserver', 'keyserver.ubuntu.com', '--recv-key', 'F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE'], check=True)
except subprocess.CalledProcessError:
    subprocess.run(['sudo', 'apt-key', 'adv', '--keyserver', 'hkp://keyserver.ubuntu.com:80', '--recv-key', 'F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE'], check=True)

release_codename = subprocess.run(['lsb_release', '-cs'], capture_output=True, text=True).stdout.strip()
subprocess.run(['sudo', 'add-apt-repository', f"deb https://librealsense.intel.com/Debian/apt-repo {release_codename} main", '-u'], check=True)

subprocess.run(['sudo', 'apt-get', 'install', 'librealsense2-utils'], check=True)

subprocess.run(['sudo', 'apt-get', 'install', 'librealsense2-dev'], check=True)
subprocess.run(['realsense-viewer'])
