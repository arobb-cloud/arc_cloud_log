import os
from datetime import datetime

LOG_FILE = "sample_logs/app_log.txt"

def analyze_log():
	if not os.path.exists(LOG_FILE):
		print(f"Log file not found: {LOG_FILE}")
		return

	error_count = 0
	warning_count = 0
	total_lines = 0

	with open(LOG_FILE, "r") as file:
		for line in file:
			total_lines += 1

			if "ERROR" in line:
				error_count += 1

			if "WARNING" in line:
				warning_count += 1

	print("\n===== Log Analysis Report =====")
	print(f"Run Time: {datetime.now()}")
	print(f"Total Lines: {total_lines}")
	print(f"Errors: {error_count}")
	print(f"Warnings: {warning_count}")

analyze_log()