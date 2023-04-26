import os
import multiprocessing

exec_files = ('exec.py')
#exec_files = ('get_cmd.py', 'exec.py', 'const_check.py')

def execute(process):
	os.system(f"python3 {process}")

process_pool = multiprocessing.Pool(processes = len(exec_files))
process_pool.map(execute, exec_files)
