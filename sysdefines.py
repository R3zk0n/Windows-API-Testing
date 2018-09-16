from ctypes import *
import ctypes
from ctypes.wintypes import BYTE, WORD, DWORD, WCHAR
# Let's map the Microsoft types to ctypes for clarity
BYTE      = c_ubyte
WORD      = c_ushort
DWORD     = c_ulong
LPBYTE    = POINTER(c_ubyte)
LPTSTR    = POINTER(c_char) 
HANDLE    = c_void_p
PVOID     = c_void_p
LPVOID    = c_void_p
UINT_PTR  = c_ulong
SIZE_T    = c_ulong



# Supporting struct for the SYSTEM_INFO_UNION union
class PROC_STRUCT(Structure):
    _fields_ = [
        ("wProcessorArchitecture",    WORD),
        ("wReserved",                 WORD),
]


# Supporting union for the SYSTEM_INFO struct
class SYSTEM_INFO_UNION(Union):
    _fields_ = [
        ("dwOemId",    DWORD),
        ("sProcStruc", PROC_STRUCT),
]

# SYSTEM_INFO structure is populated when a call to 
# kernel32.GetSystemInfo() is made. We use the dwPageSize
# member for size calculations when setting memory breakpoints
class SYSTEM_INFO(Structure):
    _fields_ = [
        ("uSysInfo", SYSTEM_INFO_UNION),
        ("dwPageSize", DWORD),
        ("lpMinimumApplicationAddress", LPVOID),
        ("lpMaximumApplicationAddress", LPVOID),
        ("dwActiveProcessorMask", DWORD),
        ("dwNumberOfProcessors", DWORD),
        ("dwProcessorType", DWORD),
        ("dwAllocationGranularity", DWORD),
        ("wProcessorLevel", WORD),
        ("wProcessorRevision", WORD),
]

class OSVERSIONINFO(ctypes.Structure):
    _fields_ = (('dwOSVersionInfoSize', DWORD),
                ('dwMajorVersion',      DWORD),
                ('dwMinorVersion',      DWORD),
                ('dwBuildNumber',       DWORD),
                ('dwPlatformId',        DWORD),
                ('szCSDVersion',        WCHAR * 128))    

class OSVERSIONINFOEX(OSVERSIONINFO):
    _fields_ = (('wServicePackMajor', WORD),
                ('wServicePackMinor', WORD),
                ('wSuiteMask',        WORD),
                ('wProductType',      BYTE),
                ('wReserved',         BYTE))