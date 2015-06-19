
import Forge

class Write():
	def __init__( self, ui ):

		ffmpegPath = "C:/Program Files/FFMPEG/bin/"
		
		inFps = 25
		inFile = ui.input.textfield_inputPath.getValue()
		inRes = "hd1080"
		outRes = "1920x1080"
		outCodec = "libx264"
		outFps = 25
		outFile = ui.output.textfield_outputPath.getValue()

		cmd = "%sffmpeg -framerate %i  -i %s -s:v %s -c:v %s -profile:v high -crf 20 -pix_fmt yuv420p -r %i %s" %(ffmpegPath, inFps, inFile, outRes, outCodec, outFps, outFile)

		
		preset= ui.console.dropmenu_encode.getValue()
		if preset == 0:
			cmd = "%sffmpeg -framerate %i  -i %s -s:v %s -c:v %s -profile:v high -crf 20 -pix_fmt yuv420p -r %i %s" %(ffmpegPath, inFps, inFile, outRes, outCodec, outFps, outFile)			
		elif preset == 1:		
			cmd = "%sffmpeg -i %s -r %i -s %s %s" %(ffmpegPath, inFile, inFps, inRes, outFile)

		Forge.core.Process.execShell(cmd)



