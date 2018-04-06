import textwrap

class Bem:

	def __init__(self,
			codigoBem,
			descricaoTipoBem,
			descricaoDetalhadaBem,
			valorBem):

		self.__codigoBem 				= codigoBem
		self.__descricaoTipoBem 		= descricaoTipoBem
		self.__descricaoDetalhadaBem 	= descricaoDetalhadaBem
		self.__valorBem 				= valorBem

	@property
	def codigoBem(self):
		return self.__codigoBem

	@codigoBem.setter
	def codigoBem(self, new):
		self.__codigoBem = codigoBem

	@property
	def descricaoTipoBem(self):
		return self.__descricaoTipoBem

	@property
	def descricaoDetalhadaBem(self):
		return self.__descricaoDetalhadaBem

	@descricaoDetalhadaBem.setter
	def descricaoDetalhadaBem(self, new):
		self.__descricaoDetalhadaBem = new

	@property
	def valorBem(self):
		return self.__valorBem

	@valorBem.setter
	def valorBem(self, new):
		self.__valorBem = new


	def __str__(self):
		return '''\
%s -- %s -- %.2f
Descrição: %s
		''' % (self.__codigoBem, self.__descricaoTipoBem, self.__valorBem,
			'\n'.join(textwrap.wrap(width=80, text=self.__descricaoDetalhadaBem)))

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.__valorBem == other.valorBem and self.__descricaoDetalhadaBem == other.descricaoDetalhadaBem

	def __lt__(self, other):
		if self.__valorBem < other.valorBem:
			return True
		elif self.__valorBem == other.valorBem:
			if self.__codigoBem < other.codigoBem:
				return True
			elif self.__codigoBem == other.codigoBem:
				return self.__descricaoDetalhadaBem < other.descricaoDetalhadaBem
			else:
				return False
		else:
			return False

	# isso ta meio estranho, mas eh oq tem pra hj
	def __le__(self, other):
		return self.__valorBem <= other.valorBem

	def __ne__(self, other):
		return self.__valorBem != other.valorBem or self.__descricaoDetalhadaBem != other.descricaoDetalhadaBem

	def __gt__(self, other):
		if self.__valorBem > other.valorBem:
			return True
		elif self.__valorBem == other.valorBem:
			if self.__codigoBem > other.codigoBem:
				return True
			elif self.codigoBem == other.codigoBem:
				return self.__descricaoDetalhadaBem > other.descricaoDetalhadaBem
			else:
				return False
		else:
			return False

	# ta estranho igual o outro la, mas eh oq tem pra hj
	def __ge__(self, other):
		return self.__valorBem > other.valorBem

