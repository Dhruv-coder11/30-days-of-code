f = int(input("Enter Free disk size in bytes.. "))
u = int(input("Enter Used disk size in bytes.. "))
o = int(input("Enter Old file size in bytes.. "))
n = int(input("Enter new File size in bytes.. "))

totalDiskSize = f + u
currentUsedDiskSize = u - 0
currentUsedDiskSize = currentUsedDiskSize + n
currentFreeDiskSize = totalDiskSize - currentUsedDiskSize

print("Free Space Available", currentFreeDiskSize, "bytes")