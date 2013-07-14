# /usr/bin/sh

#### This is just to remember what I did when setting up the EC2 AMIs
sudo apt-get update
sudo apt-get upgrade

cd
cd Downloads/
sudo chmod 777 canopy-1.0.3-rh5-64.sh
sudo ./canopy-1.0.3-rh5-64.sh

cd
cd Canopy/
./canopy

mkdir Code
cd Code/

# Install Canopy before this..
easy_install pip

ssh-keygen -t rsa -C "erik.ziegler@ulg.ac.be"
cat ../.ssh/id_rsa.pub

git clone git@github.com:nipy/nibabel.git
git clone git@github.com:swederik/nipype.git
git clone git@github.com:swederik/BrainImagingPipelines.git
git clone git@github.com:swederik/dipy.git
git clone git@github.com:swederik/connectomeviewer.git
git clone git@github.com:LTS5/cmp.git
git clone git@github.com:CyclotronResearchCentre/CRCcodes.git

#python setup.py develop

sudo apt-get install geany htop

easy_install pip
pip install nipy
pip install protobuf
pip install cfflib
pip install cython
pip install networkx
pip install sphinx
pip install nipy
pip install nitime

mkdir Processing
cd Processing/
mkdir Data
python -c "import nipype; nipype.test()"

sudo apt-get install subversion
pip install urllib3 email
sudo apt-get install g++ python libglib2.0-dev libgtk2.0-dev libglibmm-2.4-dev libgtkmm-2.4-dev libgtkglext1-dev libgsl0-dev libgl1-mesa-dev libglu1-mesa-dev
svn checkout http://mrtrix.googlecode.com/svn/trunk/ mrtrix-read-only
cd mrtrix-read-only
./build
sudo ./build install
streamtrack

sudo nano /etc/vsftpd.conf
sudo /etc/init.d/vsftpd restart
sudo service vsftpd restart
