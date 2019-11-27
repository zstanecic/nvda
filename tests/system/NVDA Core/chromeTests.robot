# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2019 NV Access Limited
# This file may be used under the terms of the GNU General Public License, version 2 or later.
# For more details see: https://www.gnu.org/licenses/gpl-2.0.html
*** Settings ***
Documentation	HTML test cases in Chrome
Default Tags	NVDA	smoke test

Library	OperatingSystem
Library	Process
Library	sendKey.py
Library	nvdaRobotLib.py
Library	helperLib.py

Test Setup	start NVDA	standard-dontShowWelcomeDialog.ini
Test Teardown	quit NVDA

Variables	webTestVariables.py

*** Test Cases ***

checkbox labelled by inner element
	[Documentation]	A checkbox labelled by an inner element should not read the label element twice.
	start chrome	checkboxLabelledByInnerElement.html
	${chrome page title} =	catenate double space	test case  Google Chrome
	${INDEX} =	wait for specific speech	${chrome page title}
	wait for speech to finish

	${post read all index} =	get next speech index
	send key	\t
	wait for speech to finish
	${actual speech} =	get speech from index until now	${post read all index}
	${button speech} =	catenate double space	Before	button
	assert strings are equal	${actual speech}	${button speech}

	${after button index} =	get next speech index
	send key	\t
	wait for speech to finish
	${actual speech} =	get speech from index until now	${after button index}
	assert strings are equal	${actual speech}	${CHECK_BOX_LABELLED_BY_INNER_ELEMENT_SPEECH}
