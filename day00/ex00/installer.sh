#!/bin/bash

if [ "$1" = "install-python" ] ; then 

	if command -v python  > /dev/null 2>&1; then
  		echo "Python is already installed, do you want to reinstall it ?"
		read -p "[yes|no]> " answer;
		if [ $answer = "yes" ]; then 
			rm -rf ~/goinfre/miniconda3;
			echo "Python has been removed.";
			sh ~/installers/Miniconda3-latest-MacOSX-x86_64.sh -b -f -p ~/goinfre/miniconda3 > /dev/null 2>&1
			echo "Python has been installed.";
	
		else 
			echo "exit."
		fi

	else
		sh ~/installers/Miniconda3-latest-MacOSX-x86_64.sh -b -f -p ~/goinfre/miniconda3 > /dev/null 2>&1
		echo "Python has been installed."
	fi
fi

if [ "$1" = "install-packages" ] ; then 

	python -V
	if command -v  conda > /dev/null 2>&1; then
		echo "installing packages"
		conda install conda-build jupyter pip;
		conda update --all
		pip install pycodestyle;
		pip install numpy
		pip install matplotlib
		pip install pandas
	else
		echo "conda missing."
	fi
fi

source ~/.zshrc > /dev/null 2>&1

