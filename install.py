
import shlex
import os
import sys
import shutil


softwareEnvironment = 'f:/software/'

FORGE_VERSION = '0.0.0.1dev'
ANVIL_VERSION = '0.0.0.1dev'

forgePath  = '%sforge_%s' %( softwareEnvironment, FORGE_VERSION )
anvilPath  = '%sanvil_%s' %( softwareEnvironment, ANVIL_VERSION )
parentPath = '/'.join( sys.path[0].replace('\\', '/').split('/')[:-1] )

envs = [ forgePath, anvilPath, parentPath ]
for env in envs:
	sys.path.append( env )

import Forge
import BCconverter


###############################################################################################
# Version
###############################################################################################


milestoneVersion = 0 # for announcing major milestones - may contain all of the below
majorVersion     = 0 # backwards-incompatible changes
minorVersion     = 0 # new backwards-compatible features
patchVersion     = 1 # bug fixes


###############################################################################################
# Environment
###############################################################################################


softwareEnvironment = 'f:/software/'
softwareName = 'BCconverter_%s.%s.%s.%sdev/%s' %( milestoneVersion, majorVersion, minorVersion, patchVersion, 'BCconverter' )
softwarePath = '%s%s/' %( softwareEnvironment, softwareName )


###############################################################################################
# Folder creation
###############################################################################################


curentPath = Forge.core.System.getPath( __file__ )
binDir              = 'bin'
coreDir             = 'core'
coreActionsDir      = 'core/Actions'
coreIconDir         = 'core/icon'
uiDir               = 'ui'

Fsystem = Forge.core.System()

for folder in 	[
					binDir,
					coreDir,
					coreActionsDir,
					coreIconDir,
					uiDir,
				]:
	Fsystem.mkdir( '%s%s' %(softwarePath, folder) )

###############################################################################################
# Moving compiles files
###############################################################################################


print '>>> Install Begin'

for folder in 	[
					curentPath,
					binDir,
					coreDir,
					coreActionsDir,
					coreIconDir,
					uiDir,
				]:
	for file in os.listdir( folder ):
		currentFile = '%s/%s' %( folder, file )
		newFile = '%s%s/%s' %( softwarePath, folder, file )

		if folder == binDir:
			shutil.copy( currentFile, newFile )
			print '>>>   "%s" is well compiled.' %( newFile )
		else:
			if '.pyc' in file:
				if folder == curentPath:
					newFile = '%s/%s' %( softwarePath, file )

				if os.path.exists( newFile ):
					os.remove( newFile )

				os.rename( currentFile, newFile )
				print '>>>   "%s" is well compiled.' %( newFile )

			elif '.png' in file:
				if folder == curentPath:
					newFile = '%s/%s' %( softwarePath, file )

				# os.rename( currentFile, newFile )
				shutil.copy(currentFile, newFile)
				print '>>>   "%s" is well copy.' %( newFile )


print '>>> Install End'
