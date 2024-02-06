# JPMC Task 1
Starter repo for task 1 of the JPMC software engineering program

## Steps to create local environment
python3 -m pip --version  
python3 -m pip install --upgrade pip  
pip install python-dateutil  

## create a git patch with multiple N commits
git format-patch -N –stdout > multi_commit.patch  
N is the number of total commit  