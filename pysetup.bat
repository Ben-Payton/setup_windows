@echo off
echo "What is your name? (This will only be used for git):"
set /p username=Enter your username:
echo "What is your email? (This will only be used for git):"
set /p useremail=Enter your email:

git config --global user.name %username%
git config --global user.email %useremail%

call conda create --name scienv python scipy numpy matplotlib pandas seaborn jupyter

call conda activate scienv
call pip install ben_sci_tools
call python quicksetup.py