from plone.app.sarissa.tests import base

JS = '++resource++plone.app.sarissa/sarissa.js'
PROFILE = 'plone.app.sarissa:default'

class TestIntegration(base.TestCase):

    def test_jsregistry(self):
        jsregistry = self.portal.portal_javascripts
        sarissa = jsregistry.getResource('sarissa.js')
        self.failUnless(not sarissa.getEnabled())
        new_sarissa = jsregistry.getResource(JS)
        self.failUnless(new_sarissa.getEnabled())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return base.build_test_suite((TestIntegration,))
