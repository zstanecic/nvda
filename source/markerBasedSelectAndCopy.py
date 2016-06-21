import textInfos

def doSelectThenCopy(scriptRepeatCount, reviewPositionCopy, ui, log):
	pos = reviewPositionCopy
	if not getattr(pos.obj, "_copyStartMarker", None):
		# Translators: Presented when attempting to copy some review cursor text but there is no start marker.
		ui.message(_("No start marker set"))
		return
	startMarker = pos.obj._copyStartMarker
	# first call, try to set the selection.
	if scriptRepeatCount==0 :
		if getattr(pos.obj, "_selectThenCopyRange", None):
			# we have already tried selecting the text, dont try again. For now selections can not be ammended.
			# Translators: Presented when text has already been marked for selection, but not yet copied.
			ui.message(_("Press twice to copy, or reset the start marker"))
			return
		copyMarker = startMarker.copy()
		# Check if the end position has moved
		if pos.compareEndPoints(startMarker, "endToEnd") > 0: # user has moved the cursor 'forward'
			# start becomes the original start
			copyMarker.setEndPoint(startMarker, "startToStart")
			# end needs to be updated to the current cursor position.
			copyMarker.setEndPoint(pos, "endToEnd")
			copyMarker.move(textInfos.UNIT_CHARACTER, 1, endPoint="end")
			pass
		elif pos.compareEndPoints(startMarker, "endToEnd") <= 0: # user has moved the cursor 'backwards'
			# start becomes the current cursor position position
			copyMarker.setEndPoint(pos, "startToStart")
			# end becomes the original start position plus 1
			copyMarker.setEndPoint(startMarker, "endToEnd")
			copyMarker.move(textInfos.UNIT_CHARACTER, 1, endPoint="end")
			pass
		else:
			# the cursor has not moved
			pass
		if copyMarker.compareEndPoints(copyMarker, "startToEnd") == 0:
			# Translators: Presented when there is no text selection to copy from review cursor.
			ui.message(_("No text to copy"))
			pos.obj._copyStartMarker = None;
			return
		pos.obj._selectThenCopyRange = copyMarker
		# for applications such as word, where the selected text is not automatically spoken we must monitor it ourself
		try:
			# old selection info must be saved so that its possible to report on the changes to the selection.
			oldInfo=pos.obj.makeTextInfo(textInfos.POSITION_SELECTION)
		except Exception as e:
			log.debug("Error trying to get initial selection information %s" % e)
			pass
		try:
			copyMarker.updateSelection()
			if hasattr(pos.obj, "waitForAndSpeakSelectionChange"):
				# wait for applications such as word to update their selection so that we can detect it
				try:
					pos.obj.waitForAndSpeakSelectionChange(oldInfo)
				except Exception as e:
					log.debug("Error trying to wait for the selection to update and then speak the selection %s" % e)
					pass
			# Translators: Presented when some review text has been selected
			ui.message(_("Selection made"))
		except NotImplementedError:
			# we are unable to select the text, leave the _copyStartMarker in place in case the user wishes to copy the text.
			# Translators: Presented when unable to select the marked text.
			ui.message(_("Can't select text, press twice to copy"))
			return
	elif scriptRepeatCount==1: # the second call, try to copy the text
		copyMarker = pos.obj._selectThenCopyRange
		if copyMarker.copyToClipboard():
			# Translators: Presented when some review text has been copied to clipboard.
			ui.message(_("Review selection copied to clipboard"))
		else:
			# Translators: Presented when unable to copy to the clipboard because of an error.
			ui.message(_("Unable to copy"))
		# on the second call always clean up the start marker
		pos.obj._selectThenCopyRange = None
		pos.obj._copyStartMarker = None
	else: # an unknown number of getLastScriptRepeatCount() calls
		return
	return
