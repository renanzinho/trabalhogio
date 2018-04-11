from Bem import Bem
from Candidato import Candidato
from Node import Node
from LinkedList import DoubleLinkedList

class Controle:

	def carregarCandidatos(path):
		listaCandidatos = DoubleLinkedList()

		with open(path, 'r', encoding='iso-8859-1') as file:
			
			for line in file:

				parse = line.split(';')
				parse = list(map(lambda x: x[1:(len(x)-1)], parse))

				listaCandidatos.add(Candidato(
					anoEleicao 				= parse[1],
		            uf 						= parse[4],
		            codigoCargo				= parse[7],
		            descricaoCargo			= parse[8],
		            nomeCandidato			= parse[9],
		            idCandidato				= parse[10],
		            numeroUrna				= parse[11],
		            cpf						= parse[12],
		            nomeNaUrna				= parse[13],
		            numeroPartido			= parse[16],
		            nomePartido  			= parse[18],
		            siglaPartido			= parse[17],
		            codigoOcupacaoCandidato	= parse[23],
		            descricaoOcupacao		= parse[24],
		            dataNascimento			= parse[25],
		            sexoCandidato			= parse[29],
		            grauInstrucao			= parse[31],
		            estadoCivil				= parse[33],
		            ufNascimento			= parse[38],
		            nomeMunicipioNascimento	= parse[40],
		            situacaoPosPleito		= parse[43],
		            situacaoCandidatura		= parse[15]
				))

		return listaCandidatos


	def carregarBens(path, listaCandidatos):

		with open(path, 'r', encoding='iso-8859-1') as file:

			for line in file:
				
				parse = line.split(';')
				parse = list(map(lambda x: x[1:(len(x)-1)], parse))

				idCandidato = parse[5]
				candidato = listaCandidatos.searchId(idCandidato)
				if candidato.bens is None:
					candidato.bens = DoubleLinkedList()
					caididato.bens.add(Bem(
						codigoBem				= parse[6],
						descricaoTipoBem		= parse[7],
						descricaoDetalhadaBem	= parse[8],
						valorBem				= parse[9]
					))
				else:
					caididato.bens.add(Bem(
						codigoBem				= parse[6],
						descricaoTipoBem		= parse[7],
						descricaoDetalhadaBem	= parse[8],
						valorBem				= parse[9]
					))


	


