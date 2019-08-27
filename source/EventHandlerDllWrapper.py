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
	def GetEvent(self, index: c_uint, e: ctypes.POINTER(EventData)) -> ctypes.c_bool: ...
	def FlushEvents(self) -> None: ...
	def RegisterAndPump_Async(self) -> None: ...
	def RegisterAndPump_Join(self) -> None: ...


def getEventHandlerDll() -> EventHandlerDll:
	dll = ctypes.cdll.LoadLibrary(r"eventHandler.dll")

	dll.GetEvent.restype = ctypes.c_bool
	dll.GetEvent.argtypes = ctypes.c_uint, ctypes.POINTER(EventData),

	dll.GetEventCount.restype = ctypes.c_uint
	dll.GetEventCount.argtypes = None

	dll.FlushEvents.restype = None
	dll.FlushEvents.argtypes = None

	dll.RegisterAndPump_Async.restype = ctypes.c_int
	dll.RegisterAndPump_Async.argtypes = None

	dll.RegisterAndPump_Join.restype = None
	dll.RegisterAndPump_Join.argtypes = None
	return dll
