#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from esccolor import esccolor


class test_esccolor( unittest.TestCase ):
###################################################################
	@classmethod
	def setUpClass(cls): # it is called before test starting
		pass

	@classmethod
	def tearDownClass(cls): # it is called before test ending
		pass

	@classmethod
	def setUp(self): # it is called before each test
		pass

	@classmethod
	def tearDown(self): # it is called after each test
		pass
                
###################################################################
	def test_id(self):
		
		self.assertEqual(esccolor.colorcode['red'], 1)
		self.assertEqual(esccolor.colorcode['cyan'], 6)
		
		self.assertEqual(esccolor.attributecode['low'], 2)
		self.assertEqual(esccolor.attributecode['reverse'], 7)

	def test_color(self):
		text = esccolor.esccolor( 'Red' ) ('__test__')
		print( text )
		self.assertEqual( text, '\033[31m__test__\033[0m' )


		text = esccolor.esccolor( 'Magenta', 'CYAN' ) ('__test__')
		print( text )
		self.assertEqual( text, '\033[35;46m__test__\033[0m' )


		text = esccolor.esccolor( 'Yellow', 'Blue','blink' ) ('__test__')
		print( text )
		self.assertEqual( text, '\033[33;44;5m__test__\033[0m' )

###################################################################
	def suite():
		suite = unittest.TestSuite()
		suite.addTests(unittest.makeSuite(test_esccolor))
		return suite
  
if( __name__ == '__main__' ):
	unittest.main()
