import os
import sys
# Only thing you need to change.
file = "./itemdef2.dat"


try:
    file_hwnd = open(file, "r+b")
except:
    print("파일을 찾을 수 없습니다!")
    sys.exit()

max_size = os.fstat(file_hwnd.fileno()).st_size
base_offset = 69
ofs = base_offset

while (ofs + 249) < max_size:
    pack = b"\xFF\xFF"
    file_hwnd.seek(ofs)
    file_hwnd.write(pack)
    ofs += 249
    print("[-] 쓴 {0} :: 0+{1:02x} in {2}".format(pack, ofs, file))

file_hwnd.close()

