# -*- coding: utf-8 -*-
from play.plone.behaviors.play_teste import IPlayTesteMarker
from play.plone.testing import PLAY_PLONE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class PlayTesteIntegrationTest(unittest.TestCase):

    layer = PLAY_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_play_teste(self):
        behavior = getUtility(IBehavior, 'play.plone.play_teste')
        self.assertEqual(
            behavior.marker,
            IPlayTesteMarker,
        )
