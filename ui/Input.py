
import Anvil.core

class Input():
	def __init__( self, parent ):

		# defind layouts
		layout_main = Anvil.core.Layout( parent=parent )


		# defind text
		text_inputPath = Anvil.core.Text( text='path :', w=50 )

		# defind textfield
		self.textfield_inputPath = Anvil.core.Textfield( text='', w=250 )

		# defind layouts content
		layout_main.add( [text_inputPath, self.textfield_inputPath] )
