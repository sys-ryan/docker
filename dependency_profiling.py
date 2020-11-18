import os, subprocess
import sys


def get_pid(pname):
	res = subprocess.check_output('ps | grep ' + pname, shell=True)
	
	res = ' '.join(res.split())
	res = res.split(' ')[0]
	print('PID : ' + res)
	return res


def get_dep(pid):
	os.system('lsof -p ' + pid + ' > ' + pid + '.temp')
	f = open('./' + pid + '.temp', 'r')
	resf = open('./' + pid + '.dep', 'w')

	lines = f.readlines()
	for idx, line in enumerate(lines):
		if idx == 0:
			continue
		
		line = line = ' '.join(line.split())
		line = line.split(' ')[-1]
		resf.write(line + '\n')
		
	f.close()	
	resf.close()
	
	os.remove('./' + pid + '.temp')

def main():
	pname = str(sys.argv[1])
	pid = get_pid(pname)
	get_dep(pid)	


if __name__ == "__main__":
	main()
