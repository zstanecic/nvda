import ctypes
from ctypes import wintypes
from ctypes import c_uint

class EventData(ctypes.Structure):
	_fields_ = [
		("idEvent", wintypes.DWORD),
		("hwnd", wintypes.HWND),
		("idObject", wintypes.LONG),
		("idChild", wintypes.LONG),
		("dwEventThread", wintypes.DWORD),
		("dwmsEventTime", wintypes.DWORD),
	]
	idEvent: wintypes.DWORD
	hwnd: wintypes.HWND
	idObject: wintypes.LONG
	idChild: wintypes.LONG
	dwEventThread: wintypes.DWORD
	dwmsEventTime: wintypes.DWORD


class EventHandlerDll:
	def GetEventCount(self) -> c_uint: ...
	def GetEvent(self, index: c_uint, e: ctypes.POINTER(EventData)) -> None: ...
	def SwapEventBuffers(self) -> None: ...
	def InitializeMSAA(self) -> ctypes.c_int: ...
	def ShutdownMSAA(self) -> None: ...


def getEventHandlerDll() -> EventHandlerDll:
	dll = ctypes.cdll.LoadLibrary(r"C:\work\test projects\WinEventLogger\Release\eventHandler.dll")

	dll.GetEvent.restype = None
	dll.GetEvent.argtypes = ctypes.c_uint, ctypes.POINTER(EventData),

	dll.GetEventCount.restype = ctypes.c_uint
	dll.GetEventCount.argtypes = None

	dll.SwapEventBuffers.restype = None
	dll.SwapEventBuffers.argtypes = None

	dll.InitializeMSAA.restype = ctypes.c_int
	dll.InitializeMSAA.argtypes = None

	dll.ShutdownMSAA.restype = ctypes.c_uint
	dll.ShutdownMSAA.argtypes = None
	return dll
