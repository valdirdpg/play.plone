# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import play.plone


class PlayPloneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=play.plone)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'play.plone:default')


PLAY_PLONE_FIXTURE = PlayPloneLayer()


PLAY_PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLAY_PLONE_FIXTURE,),
    name='PlayPloneLayer:IntegrationTesting',
)


PLAY_PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLAY_PLONE_FIXTURE,),
    name='PlayPloneLayer:FunctionalTesting',
)


PLAY_PLONE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLAY_PLONE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlayPloneLayer:AcceptanceTesting',
)
