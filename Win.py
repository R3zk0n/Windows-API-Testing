from ctypes import *
import sys
from sysdefines import *
import time
import win32api
kernel32 = windll.kernel32


def getnames():
	hostname = win32api.GetComputerName()
	user = win32api.GetUserName()
	location = win32api.GetWindowsDirectory()
	version = win32api.GetVersion()
	print "Hostname: "+ hostname
	print "Username: "+user
	print "Windows Directory Location: "+location	
	print version


def get_version():
		info = OSVERSIONINFO()
		print info.dwMajorVersion

		


def system_info():
		system_info = SYSTEM_INFO()

		kernel32.GetSystemInfo(byref(system_info))

		page_size = system_info.dwPageSize
		NumProcesses = system_info.dwNumberOfProcessors
		print("Page Size Avaiable: " + str(page_size))
		if NumProcesses == 0:
			print "X86 Intel Arch Detected"
	

if __name__ == '__main__':
	system_info()
	get_version()
	getnames()