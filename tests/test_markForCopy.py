import unittest
import mock
from context import markerBasedSelectAndCopy
import context
import copy
from textInfos import UNIT_CHARACTER


# Not so sure that unittest.mock results in very readable tests. Perhaps if it is used along with
# mockito
# in the style:
# when(reviewCursor).compareEndPoints(startMark, "endToEnd").thenReturn(1)
# when(startMarkCopy).compareEndPoints(startMarkCopy, "startToEnd").thenReturn(1)
# verify(startMarkCopy).updateSelection()
# verifyNoMoreInteractions(startMarkCopy)

# work around issue where mocked class has constructor taking arguments. See 
# http://stackoverflow.com/questions/37923265/why-does-unittest-mock-fail-when-the-production-class-constructor-takes-extra-ar
class wrapped_TextInfo(context.textInfos.TextInfo):
	def __init__(self):
		super(obj=None, position=None)

class BasicTestSuite(unittest.TestCase):
	"""Basic test Cases."""
	
	# happy case
	def test_doSelect(self):
		# create mocks 
		scriptRepeatCount = 0
		ui = mock.MagicMock(name="ui", return_value=None)
		log = mock.MagicMock(name="log", return_value=None)
		reviewCursor = mock.MagicMock(name="reviewCursor", spec=wrapped_TextInfo)
		startMark = mock.MagicMock(name="startMark", spec=wrapped_TextInfo)
		# setup return values
		reviewCursor.compareEndPoints.return_value = 1 # ahead of the start marker
		startMarkCopy = mock.MagicMock(name="startMarkCopy", spec=wrapped_TextInfo)
		startMarkCopy.compareEndPoints.return_value = 1 # selection to copy has range
		startMark.copy.return_value = startMarkCopy
		objMock = mock.MagicMock(name="obj")
		reviewCursor.attach_mock(objMock, "obj")
		reviewCursor.obj._copyStartMarker = startMark
		del objMock._selectThenCopyRange
		del objMock.waitForAndSpeakSelectionChange
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(scriptRepeatCount, reviewCursor, ui, log)
		# expect
		ui.assert_has_calls([mock.call.message(u'Selection made')])
		startMark.assert_has_calls([mock.call.copy()], any_order=True)
		startMarkCopy.assert_has_calls([mock.call.setEndPoint(startMark, "startToStart"), mock.call.setEndPoint(reviewCursor, "endToEnd"), mock.call.move(UNIT_CHARACTER, 1, endpoint="end"), mock.call.updateSelection()], any_order=True)

	def test_doSelect_backwards(self):
		# create mocks 
		scriptRepeatCount = 0
		ui = mock.MagicMock(name="ui", return_value=None)
		log = mock.MagicMock(name="log", return_value=None)
		reviewCursor = mock.MagicMock(name="reviewCursor", spec=wrapped_TextInfo)
		startMark = mock.MagicMock(name="startMark", spec=wrapped_TextInfo)
		# setup return values
		reviewCursor.compareEndPoints.return_value = -1 # behind the start marker
		startMarkCopy = mock.MagicMock(name="startMarkCopy", spec=wrapped_TextInfo)
		startMarkCopy.compareEndPoints.return_value = 1 # selection to copy has range
		startMark.copy.return_value = startMarkCopy
		objMock = mock.MagicMock(name="obj")
		reviewCursor.attach_mock(objMock, "obj")
		reviewCursor.obj._copyStartMarker = startMark
		del objMock._selectThenCopyRange
		del objMock.waitForAndSpeakSelectionChange
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(scriptRepeatCount, reviewCursor, ui, log)
		# expect
		ui.assert_has_calls([mock.call.message(u'Selection made')])
		startMark.assert_has_calls([mock.call.copy()], any_order=True)
		startMarkCopy.assert_has_calls([mock.call.setEndPoint(startMark, "endToEnd"), mock.call.setEndPoint(reviewCursor, "startToStart"), mock.call.move(UNIT_CHARACTER, 1, endpoint="end"), mock.call.updateSelection()], any_order=True)
	
	def test_noStartMarkerSet(self):
		# given
		scriptRepeatCount = 0
		ui = mock.MagicMock(return_value=None)
		log = mock.MagicMock(return_value=None)
		reviewCursor = mock.MagicMock(spec=context.textInfos.TextInfo)
		del reviewCursor.obj._copyStartMarker
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(scriptRepeatCount, reviewCursor, ui, log)
		# expect
		ui.assert_has_calls([mock.call.message(u'No start marker set')])
	
	def test_selectAlreadyPerformed(self):
		# given
		scriptRepeatCount = 0
		ui = mock.MagicMock(return_value=None)
		log = mock.MagicMock(return_value=None)
		reviewCursor = mock.MagicMock(spec=context.textInfos.TextInfo)
		# _copyStartMarker exists
		# _selectThenCopyRange exists
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(scriptRepeatCount, reviewCursor, ui, log)
		# expect
		ui.assert_has_calls([mock.call.message(u'Press twice to copy, or reset the start marker')])


if __name__ == '__main__':
	unittest.main()

