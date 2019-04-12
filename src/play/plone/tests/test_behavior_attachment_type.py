# -*- coding: utf-8 -*-
from play.plone.behaviors.attachment_type import IAttachmentTypeMarker
from play.plone.testing import PLAY_PLONE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class AttachmentTypeIntegrationTest(unittest.TestCase):

    layer = PLAY_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_attachment_type(self):
        behavior = getUtility(IBehavior, 'play.plone.attachment_type')
        self.assertEqual(
            behavior.marker,
            IAttachmentTypeMarker,
        )
