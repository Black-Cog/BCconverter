
import Anvil.core

class Output():
	def __init__( self, parent ):

		# defind layouts
		layout_main = Anvil.core.Layout( parent=parent )

		# defind text
		text_outputPath = Anvil.core.Text( text='path :', w=50 )

		# defind textfield
		self.textfield_outputPath = Anvil.core.Textfield( text='', w=250 )

		# defind layouts content
		layout_main.add( [text_outputPath, self.textfield_outputPath] )
