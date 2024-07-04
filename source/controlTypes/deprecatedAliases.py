# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2022 NV Access Limited
# This file may be used under the terms of the GNU General Public License, version 2 or later.
# For more details see: https://www.gnu.org/licenses/gpl-2.0.html

"""
This module contains aliases for symbols used before controlTypes was refactored.
These values should not be extended, they are for backwards compatibility with add-ons only.
It is recommended that add-ons convert to use the Role, and State symbols directly rather than
continuing to rely on the aliases (I.E. 'ROLE_*' and 'STATE_*' symbols) this module provides.
Using controlTypes.Role and controlTypes.State will make your add-on code consistent with NVDA core.
"""

import typing
from .role import (
	Role,
	_roleLabels,
)
from .state import (
	State,
	_stateLabels,
	_negativeStateLabels,
)
from .processAndLabelStates import (
	_processNegativeStates,
	_processPositiveStates,
)

# Do not extend
roleLabels = _roleLabels
"Deprecated. Recommendation: prefer to use controlTypes.Role.displayString instead"
stateLabels = _stateLabels
"Deprecated. Recommendation: prefer to use controlTypes.State.displayString instead"
negativeStateLabels = _negativeStateLabels
"Deprecated. Recommendation: prefer to use controlTypes.State.negativeDisplayString instead"
processNegativeStates = _processNegativeStates
"Deprecated. Recommendation: prefer to use controlTypes.processAndLabelStates instead"
processPositiveStates = _processPositiveStates
"Deprecated. Recommendation: prefer to use controlTypes.processAndLabelStates instead"
# Do not extend
# Recommendation: prefer to use controlTypes.Role directly
ROLE_UNKNOWN = Role.UNKNOWN
ROLE_WINDOW = Role.WINDOW
ROLE_TITLEBAR = Role.TITLEBAR
ROLE_PANE = Role.PANE
ROLE_DIALOG = Role.DIALOG
ROLE_CHECKBOX = Role.CHECKBOX
ROLE_RADIOBUTTON = Role.RADIOBUTTON
ROLE_STATICTEXT = Role.STATICTEXT
ROLE_EDITABLETEXT = Role.EDITABLETEXT
ROLE_BUTTON = Role.BUTTON
ROLE_MENUBAR = Role.MENUBAR
ROLE_MENUITEM = Role.MENUITEM
ROLE_POPUPMENU = Role.POPUPMENU
ROLE_COMBOBOX = Role.COMBOBOX
ROLE_LIST = Role.LIST
ROLE_LISTITEM = Role.LISTITEM
ROLE_GRAPHIC = Role.GRAPHIC
ROLE_HELPBALLOON = Role.HELPBALLOON
ROLE_TOOLTIP = Role.TOOLTIP
ROLE_LINK = Role.LINK
ROLE_TREEVIEW = Role.TREEVIEW
ROLE_TREEVIEWITEM = Role.TREEVIEWITEM
ROLE_TAB = Role.TAB
ROLE_TABCONTROL = Role.TABCONTROL
ROLE_SLIDER = Role.SLIDER
ROLE_PROGRESSBAR = Role.PROGRESSBAR
ROLE_SCROLLBAR = Role.SCROLLBAR
ROLE_STATUSBAR = Role.STATUSBAR
ROLE_TABLE = Role.TABLE
ROLE_TABLECELL = Role.TABLECELL
ROLE_TABLECOLUMN = Role.TABLECOLUMN
ROLE_TABLEROW = Role.TABLEROW
ROLE_TABLECOLUMNHEADER = Role.TABLECOLUMNHEADER
ROLE_TABLEROWHEADER = Role.TABLEROWHEADER
ROLE_FRAME = Role.FRAME
ROLE_TOOLBAR = Role.TOOLBAR
ROLE_DROPDOWNBUTTON = Role.DROPDOWNBUTTON
ROLE_CLOCK = Role.CLOCK
ROLE_SEPARATOR = Role.SEPARATOR
ROLE_FORM = Role.FORM
ROLE_HEADING = Role.HEADING
ROLE_HEADING1 = Role.HEADING1
ROLE_HEADING2 = Role.HEADING2
ROLE_HEADING3 = Role.HEADING3
ROLE_HEADING4 = Role.HEADING4
ROLE_HEADING5 = Role.HEADING5
ROLE_HEADING6 = Role.HEADING6
ROLE_PARAGRAPH = Role.PARAGRAPH
ROLE_BLOCKQUOTE = Role.BLOCKQUOTE
ROLE_TABLEHEADER = Role.TABLEHEADER
ROLE_TABLEBODY = Role.TABLEBODY
ROLE_TABLEFOOTER = Role.TABLEFOOTER
ROLE_DOCUMENT = Role.DOCUMENT
ROLE_ANIMATION = Role.ANIMATION
ROLE_APPLICATION = Role.APPLICATION
ROLE_BOX = Role.BOX
ROLE_GROUPING = Role.GROUPING
ROLE_PROPERTYPAGE = Role.PROPERTYPAGE
ROLE_CANVAS = Role.CANVAS
ROLE_CAPTION = Role.CAPTION
ROLE_CHECKMENUITEM = Role.CHECKMENUITEM
ROLE_DATEEDITOR = Role.DATEEDITOR
ROLE_ICON = Role.ICON
ROLE_DIRECTORYPANE = Role.DIRECTORYPANE
ROLE_EMBEDDEDOBJECT = Role.EMBEDDEDOBJECT
ROLE_ENDNOTE = Role.ENDNOTE
ROLE_FOOTER = Role.FOOTER
ROLE_FOOTNOTE = Role.FOOTNOTE
ROLE_GLASSPANE = Role.GLASSPANE
ROLE_HEADER = Role.HEADER
ROLE_IMAGEMAP = Role.IMAGEMAP
ROLE_INPUTWINDOW = Role.INPUTWINDOW
ROLE_LABEL = Role.LABEL
ROLE_NOTE = Role.NOTE
ROLE_PAGE = Role.PAGE
ROLE_RADIOMENUITEM = Role.RADIOMENUITEM
ROLE_LAYEREDPANE = Role.LAYEREDPANE
ROLE_REDUNDANTOBJECT = Role.REDUNDANTOBJECT
ROLE_ROOTPANE = Role.ROOTPANE
ROLE_EDITBAR = Role.EDITBAR
ROLE_TERMINAL = Role.TERMINAL
ROLE_RICHEDIT = Role.RICHEDIT
ROLE_RULER = Role.RULER
ROLE_SCROLLPANE = Role.SCROLLPANE
ROLE_SECTION = Role.SECTION
ROLE_SHAPE = Role.SHAPE
ROLE_SPLITPANE = Role.SPLITPANE
ROLE_VIEWPORT = Role.VIEWPORT
ROLE_TEAROFFMENU = Role.TEAROFFMENU
ROLE_TEXTFRAME = Role.TEXTFRAME
ROLE_TOGGLEBUTTON = Role.TOGGLEBUTTON
ROLE_BORDER = Role.BORDER
ROLE_CARET = Role.CARET
ROLE_CHARACTER = Role.CHARACTER
ROLE_CHART = Role.CHART
ROLE_CURSOR = Role.CURSOR
ROLE_DIAGRAM = Role.DIAGRAM
ROLE_DIAL = Role.DIAL
ROLE_DROPLIST = Role.DROPLIST
ROLE_SPLITBUTTON = Role.SPLITBUTTON
ROLE_MENUBUTTON = Role.MENUBUTTON
ROLE_DROPDOWNBUTTONGRID = Role.DROPDOWNBUTTONGRID
ROLE_MATH = Role.MATH
ROLE_GRIP = Role.GRIP
ROLE_HOTKEYFIELD = Role.HOTKEYFIELD
ROLE_INDICATOR = Role.INDICATOR
ROLE_SPINBUTTON = Role.SPINBUTTON
ROLE_SOUND = Role.SOUND
ROLE_WHITESPACE = Role.WHITESPACE
ROLE_TREEVIEWBUTTON = Role.TREEVIEWBUTTON
ROLE_IPADDRESS = Role.IPADDRESS
ROLE_DESKTOPICON = Role.DESKTOPICON
ROLE_INTERNALFRAME = Role.INTERNALFRAME
ROLE_DESKTOPPANE = Role.DESKTOPPANE
ROLE_OPTIONPANE = Role.OPTIONPANE
ROLE_COLORCHOOSER = Role.COLORCHOOSER
ROLE_FILECHOOSER = Role.FILECHOOSER
ROLE_FILLER = Role.FILLER
ROLE_MENU = Role.MENU
ROLE_PANEL = Role.PANEL
ROLE_PASSWORDEDIT = Role.PASSWORDEDIT
ROLE_FONTCHOOSER = Role.FONTCHOOSER
ROLE_LINE = Role.LINE
ROLE_FONTNAME = Role.FONTNAME
ROLE_FONTSIZE = Role.FONTSIZE
ROLE_BOLD = Role.BOLD
ROLE_ITALIC = Role.ITALIC
ROLE_UNDERLINE = Role.UNDERLINE
ROLE_FGCOLOR = Role.FGCOLOR
ROLE_BGCOLOR = Role.BGCOLOR
ROLE_SUPERSCRIPT = Role.SUPERSCRIPT
ROLE_SUBSCRIPT = Role.SUBSCRIPT
ROLE_STYLE = Role.STYLE
ROLE_INDENT = Role.INDENT
ROLE_ALIGNMENT = Role.ALIGNMENT
ROLE_ALERT = Role.ALERT
ROLE_DATAGRID = Role.DATAGRID
ROLE_DATAITEM = Role.DATAITEM
ROLE_HEADERITEM = Role.HEADERITEM
ROLE_THUMB = Role.THUMB
ROLE_CALENDAR = Role.CALENDAR
ROLE_VIDEO = Role.VIDEO
ROLE_AUDIO = Role.AUDIO
ROLE_CHARTELEMENT = Role.CHARTELEMENT
ROLE_DELETED_CONTENT = Role.DELETED_CONTENT
ROLE_INSERTED_CONTENT = Role.INSERTED_CONTENT
ROLE_LANDMARK = Role.LANDMARK
ROLE_ARTICLE = Role.ARTICLE
ROLE_REGION = Role.REGION
ROLE_FIGURE = Role.FIGURE
ROLE_MARKED_CONTENT = Role.MARKED_CONTENT
# Do not extend
# Recommendation: prefer to use controlTypes.State directly
STATE_UNAVAILABLE = State.UNAVAILABLE
STATE_FOCUSED = State.FOCUSED
STATE_SELECTED = State.SELECTED
STATE_BUSY = State.BUSY
STATE_PRESSED = State.PRESSED
STATE_CHECKED = State.CHECKED
STATE_HALFCHECKED = State.HALFCHECKED
STATE_READONLY = State.READONLY
STATE_EXPANDED = State.EXPANDED
STATE_COLLAPSED = State.COLLAPSED
STATE_INVISIBLE = State.INVISIBLE
STATE_VISITED = State.VISITED
STATE_LINKED = State.LINKED
STATE_HASPOPUP = State.HASPOPUP
STATE_PROTECTED = State.PROTECTED
STATE_REQUIRED = State.REQUIRED
STATE_DEFUNCT = State.DEFUNCT
STATE_INVALID_ENTRY = State.INVALID_ENTRY
STATE_MODAL = State.MODAL
STATE_AUTOCOMPLETE = State.AUTOCOMPLETE
STATE_MULTILINE = State.MULTILINE
STATE_ICONIFIED = State.ICONIFIED
STATE_OFFSCREEN = State.OFFSCREEN
STATE_SELECTABLE = State.SELECTABLE
STATE_FOCUSABLE = State.FOCUSABLE
STATE_CLICKABLE = State.CLICKABLE
STATE_EDITABLE = State.EDITABLE
STATE_CHECKABLE = State.CHECKABLE
STATE_DRAGGABLE = State.DRAGGABLE
STATE_DRAGGING = State.DRAGGING
STATE_DROPTARGET = State.DROPTARGET
STATE_SORTED = State.SORTED
STATE_SORTED_ASCENDING = State.SORTED_ASCENDING
STATE_SORTED_DESCENDING = State.SORTED_DESCENDING
STATE_HASLONGDESC = State.HASLONGDESC
STATE_PINNED = State.PINNED
STATE_HASFORMULA = State.HASFORMULA
STATE_HASCOMMENT = State.HASCOMMENT
STATE_OBSCURED = State.OBSCURED
STATE_CROPPED = State.CROPPED
STATE_OVERFLOWING = State.OVERFLOWING
STATE_UNLOCKED = State.UNLOCKED
# Do not extend


def getDeprecatedLabellingAliasNames() -> typing.List[str]:
	return [
		"roleLabels",
		"stateLabels",
		"negativeStateLabels",
		"processNegativeStates",
		"processPositiveStates",
	]  # do not extend


def getDeprecatedRoleAliasNames() -> typing.List[str]:
	return [
		symbol
		for symbol, thing in globals().items()
		if symbol.startswith("ROLE_")
	]


def getDeprecatedStateAliasNames() -> typing.List[str]:
	return [
		symbol
		for symbol, thing in globals().items()
		if symbol.startswith("STATE_")
	]


# Ensure only the aliases are exposed when deprecations are imported.
# Everything else must be explicitly referenced
__all__ = [
	*getDeprecatedStateAliasNames(),
	*getDeprecatedRoleAliasNames(),
	*getDeprecatedLabellingAliasNames(),
]  # do not extend
