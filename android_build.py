import subprocess
import shlex
import getpass
import os

print("Enter type of build: [1] for Debug or [2] for Release")
buildType = int(input("Enter build type:"))
if buildType == 1:
	print("Building Android project on debug mode")
	subprocess.call(shlex.split('./gradlew assembleDebug'))
elif buildType == 2:
	print("Building Android project on release mode")
	# subprocess.call(shlex.split('./gradlew assembleRelease'))
	# Get system username
	username = getpass.getuser()
	buildToolsPath = "/Users/" + username + "/Library/Android/sdk/build-tools/"
	print("Build path " + buildToolsPath)
	# Get all the top or immediate directory from the buildToolsPath
	# These are usually Android version folder names like 29.0.3 or 30.0.2
	directoryList = next(os.walk(buildToolsPath))[1]
	largestVersion = 0
	largestVersionFull = ""
	for directory in directoryList:
		# Split the version number
		versionSplit = directory.split(".")
		majorVersion = int(versionSplit[0])
		if largestVersion == 0:
			largestVersion = majorVersion
			largestVersionFull = directory
		else:
			if majorVersion > largestVersion:
				largestVersion = majorVersion
				largestVersionFull = directory
	print("Latest version is " + largestVersionFull)
	apkSignerPath = buildToolsPath + largestVersionFull + "/apksigner"
	print("Apksigner path " + apkSignerPath)
	# print("dir list " + directoryList)
	# for dirPath,dirNames,fileNames in os.walk(buildToolsPath):
	# 	print(dirNames.next())
else:
	print("You entered the wrong option.")

# subprocess.call(shlex.split('./gradlew assembleRelease'))
# subprocess.call(shlex.split('/Users/lawrencegimenez/Library/Android/sdk/build-tools/30.0.2/apksigner sign --ks Credentials/onlinejobs.keystore --ks-key-alias onlinejobs --ks-pass pass:PrY7qTRgGaxeQ5sweD --key-pass pass:PrY7qTRgGaxeQ5sweD --out app/build/outputs/apk/release/onlinejobs-signed.apk app/build/outputs/apk/release/app-release-unsigned.apk'))
# subprocess.call(shlex.split('/Users/lawrencegimenez/Library/Android/sdk/build-tools/30.0.2/zipalign 4 app/build/outputs/apk/release/onlinejobs-signed.apk onlinejobs-aligned.apk'))