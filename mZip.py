import zipfile
import glob, os
import sys
path = str(sys.argv[1])
try:
	os.chdir(path)
except:
	print("Wrong path")
for file in glob.glob("*.zip"):
	zipPath = path+os.path.sep+file
	dirPath = path+os.path.sep+file.replace(".zip","")
	try:
		with zipfile.ZipFile(zipPath, 'r') as zip_ref:
			zip_ref.extractall(dirPath)
			print(f"Successfully extracted : {file}")
	except:
		print(f"Error extracting : {file}")


