from django.test import TestCase
from .models import Law, Lawyer, Articles


# Create your tests here.
class LawTestCase(TestCase):
    '''
    Class that defines the test suite for the Law Model
    '''
    def SetUp(self):
        '''
        