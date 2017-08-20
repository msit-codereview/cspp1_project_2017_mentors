class FileClass(object):
	"""docstring for FileClass"""
	def __init__(self,filename,wordFreq):
		self.fileName = filename
		self.word_freq = wordFreq

	def set_fileName(self,filename):
		self.fileName = filename

	def get_fileName(self):
		return self.filename

	def word_freq(self,wordFreq):
		self.word_freq = wordFreq
		
	def get_wordsFreq(self):
		return self.word_freq
		