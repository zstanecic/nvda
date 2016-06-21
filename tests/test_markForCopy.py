import unittest
import mock
from context import markerBasedSelectAndCopy
import context
import copy
from textInfos import UNIT_CHARACTER

class BasicTestSuite(unittest.TestCase):
	"""Basic test Cases."""
	
	def setUp(self):
		self.scriptRepeatCount = 0
		self.ui = mock.MagicMock(name="ui", return_value=None)
		self.log = mock.MagicMock(name="log", return_value=None)
		self.reviewCursor = mock.MagicMock(name="reviewCursor", spec=wrapped_TextInfo)
		self.objMock = mock.MagicMock(name="obj")
		self.startMark = mock.MagicMock(name="startMark", spec=wrapped_TextInfo)
		self.startMarkCopy = copy(self.startMark)
		
		self.reviewCursor.attach_mock(self.objMock, "obj")
		self.objMock.attach_mock(self.startMark, "_copyStartMarker")
		self.startMark.copy.return_value = self.startMarkCopy
		
	
	# happy case
	def test_doSelect(self):
		self.startMark.set(start=5, end=5)
		self.reviewCursor.set(start=8, end=8)
		del self.objMock._selectThenCopyRange
		del self.objMock.waitForAndSpeakSelectionChange
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(self.scriptRepeatCount, self.reviewCursor, self.ui, self.log)
		# expect
		self.ui.assert_has_calls([mock.call.message(u'Selection made')])
		assert self.objMock._selectThenCopyRange != None
		self.objMock._selectThenCopyRange.assert_has_calls([mock.call.updateSelection])
		assert self.objMock._selectThenCopyRange.start == 5
		assert self.objMock._selectThenCopyRange.end == 9

	def test_doSelect_backwards(self):
		self.startMark.set(start=5, end=5)
		self.reviewCursor.set(start=2, end=2)
		del self.objMock._selectThenCopyRange
		del self.objMock.waitForAndSpeakSelectionChange
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(self.scriptRepeatCount, self.reviewCursor, self.ui, self.log)
		# expect
		self.ui.assert_has_calls([mock.call.message(u'Selection made')])
		assert self.objMock._selectThenCopyRange != None
		self.objMock._selectThenCopyRange.assert_has_calls([mock.call.updateSelection])
		assert self.objMock._selectThenCopyRange.start == 2
		assert self.objMock._selectThenCopyRange.end == 6
	
	def test_noStartMarkerSet(self):
		# given
		del self.reviewCursor.obj._copyStartMarker
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(self.scriptRepeatCount, self.reviewCursor, self.ui, self.log)
		# expect
		self.ui.assert_has_calls([mock.call.message(u'No start marker set')])
	
	def test_selectAlreadyPerformed(self):
		# given
		# _copyStartMarker exists
		# _selectThenCopyRange exists
		# do
		markerBasedSelectAndCopy.doSelectThenCopy(self.scriptRepeatCount, self.reviewCursor, self.ui, self.log)
		# expect
		self.ui.assert_has_calls([mock.call.message(u'Press twice to copy, or reset the start marker')])


if __name__ == '__main__':
	unittest.main()

