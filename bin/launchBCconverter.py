

###############################################################################################
# Environment
###############################################################################################


import sys

softwareEnvironment = 'f:/software/'

FORGE_VERSION = '0.0.0.1dev'
ANVIL_VERSION = '0.0.0.1dev'

forgePath  = '%sforge_%s' %( softwareEnvironment, FORGE_VERSION )
anvilPath  = '%sanvil_%s' %( softwareEnvironment, ANVIL_VERSION )
parentPath = '/'.join( sys.path[0].replace('\\', '/').split('/')[:-2] )

envs = [ forgePath, anvilPath, parentPath ]

for env in envs:
	sys.path.append( env )



###############################################################################################
# Launcher
###############################################################################################


from PySide import QtCore, QtGui
import Forge
import BCconverter

interpreter = Forge.core.System().interpreter()
app = QtGui.QApplication(sys.argv)
widget = BCconverter.ui.ClassLoader()
widget.app().show()
sys.exit( app.exec_() )
