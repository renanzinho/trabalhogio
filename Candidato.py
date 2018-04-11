import Bem

class Candidato:

    def __init__(self,
            anoEleicao,
            uf,
            codigoCargo,
            descricaoCargo,
            nomeCandidato,
            idCandidato,
            numeroUrna,
            cpf,
            nomeNaUrna,
            numeroPartido,
            nomePartido,
            siglaPartido,
            codigoOcupacaoCandidato,
            descricaoOcupacao,
            dataNascimento,
            sexoCandidato,
            grauInstrucao,
            estadoCivil,
            ufNascimento,
            nomeMunicipioNascimento,
            situacaoPosPleito,
            situacaoCandidatura,
            bens=None):

    	self.__anoEleicao 				= anoEleicao
        self.__uf 						= uf
        self.__codigoCargo 				= codigoCargo
        self.__descricaoCargo			= descricaoCargo
        self.__nomeCandidato 			= nomeCandidato
        self.__idCandidato 				= idCandidato
        self.__numeroUrna 				= numeroUrna
        self.__cpf						= cpf
        self.__nomeNaUrna				= nomeNaUrna
        self.__numeroPartido 			= numeroPartido
        self.__nomePartido 				= nomePartido
        self.__siglaPartido 			= siglaPartido
        self.__codigoOcupacaoCandidato 	= codigoOcupacaoCandidato
        self.__descricaoOcupacao 		= descricaoOcupacao
        self.__dataNascimento 			= dataNascimento
        self.__sexoCandidato 			= sexoCandidato
        self.__grauInstrucao 			= grauInstrucao
        self.__estadoCivil 				= estadoCivil
        self.__ufNascimento 			= ufNascimento
        self.__nomeMunicipioNascimento  = nomeMunicipioNascimento
        self.__situacaoPosPleito 		= situacaoPosPleito
        self.__situacaoCandidatura  	= situacaoCandidatura
        self.__bens 					= bens


    @property
    def anoEleicao(self):
    	return self.__anoEleicao

    @anoEleicao.setter
    def anoEleicao(self, new):
    	self.__anoEleicao = new

    @property
    def uf(self):
    	return self.__uf

    @uf.setter
    def uf(self, new):
    	self.__uf = new

    @property
    def codigoCargo(self):
    	return self.__codigoCargo

    @codigoCargo.setter
    def codigoCargo(self, new):
    	self.__codigoCargo = new

    @property
    def descricaoCargo(self):
    	return self.__descricaoCargo

    @descricaoCargo.setter
    def descricaoCargo(self, new):
    	self.__descricaoCargo = new

    @property
    def nomeCandidato(self):
    	return self.__nomeCandidato

    @nomeCandidato.setter
    def nomeCandidato(self, new):
    	self.__nomeCandidato = new

    @property
    def idCandidato(self):
    	return self.__idCandidato

    @idCandidato.setter
    def idCandidato(self, new):
    	self.__idCandidato = new


    @property
    def numeroUrna(self):
    	return self.__numeroUrna

    @numeroUrna.setter
    def numeroUrna(self, new):
    	self.__numeroUrna = new

    @property
    def cpf(self):
    	return self.__cpf

    @cpf.setter
    def cpf(self, new):
    	self.__cpf = new

    @property
    def nomeNaUrna(self):
    	return self.__nomeNaUrna

    @nomeNaUrna.setter
    def nomeNaUrna(self, new):
    	self.__nomeNaUrna = new

    @property
    def numeroPartido(self):
    	return self.__numeroPartido

    @numeroPartido.setter
    def numeroPartido(self, new):
    	self.__numeroPartido = new

    @property
    def nomePartido(self):
    	return self.__nomePartido

    @nomePartido.setter
    def nomePartido(self, new):
    	self.__nomePartido = new

    @property
    def siglaPartido(self):
    	return self.__siglaPartido

    @siglaPartido.setter
    def siglaPartido(self, new):
    	self.__siglaPartido = new

    @property
    def codigoOcupacaoCandidato(self):
    	return self.__codigoOcupacaoCandidato

    @codigoOcupacaoCandidato.setter
    def codigoOcupacaoCandidato(self, new):
    	self.__codigoOcupacaoCandidato = new

    @property
    def descricaoOcupacao(self):
    	return self.__descricaoOcupacao

    @descricaoOcupacao.setter
    def descricaoOcupacao(self, new):
    	self.__descricaoOcupacao = new

    @property
    def dataNascimento(self):
    	return self.__dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, new):
    	self.__dataNascimento = new

    @property
    def sexoCandidato(self):
    	return self.__sexoCandidato

    @sexoCandidato.setter
    def sexoCandidato(self, new):
    	self.__sexoCandidato = new

    @property
    def grauInstrucao(self):
    	return self.__grauInstrucao

    @grauInstrucao.setter
    def grauInstrucao(self, new):
    	self.__grauInstrucao = new

    @property
    def estadoCivil(self):
    	return self.__estadoCivil

    @estadoCivil.setter
    def estadoCivil(self, new):
    	self.__estadoCivil = new

    @property
    def ufNascimento(self):
    	return self.__ufNascimento

    @ufNascimento.setter
    def ufNascimento(self, new):
    	self.__ufNascimento = new

    @property
    def nomeMunicipioNascimento(self):
    	return self.__nomeMunicipioNascimento

    @nomeMunicipioNascimento.setter
    def nomeMunicipioNascimento(self, new):
    	self.__nomeMunicipioNascimento = new

    @property
    def situacaoPosPleito(self):
    	return self.__situacaoPosPleito

    @situacaoPosPleito.setter
    def situacaoPosPleito(self, new):
    	self.__situacaoPosPleito = new

    @property
    def situacaoCandidatura(self):
    	return self.__situacaoCandidatura

    @situacaoCandidatura.setter
    def situacaoCandidatura(self, new):
    	self.__situacaoCandidatura = new

    @property
    def bens(self):
    	return self.__bens

    @bens.setter
    def bens(self, new):
    	self.__bens = new

    def __str__(self):

        valorTotal   = 0
        valorPorTipo = {}
        for bem in self.__bens:
            valorTotal += bem.valorBem
            if bem.descricaoTipoBem in valorPorTipo:
                valorPorTipo[bem.descricaoTipoBem] += bem.valorBem
            else:
                valorPorTipo[bem.descricaoTipoBem] = bem.valorBem

        # Nao eh o jeito mais bonito, mas funfa
        dictToString = ''
        for i in valorPorTipo:
            dictToString += '\t\t- %s: %.2f R$\n' % (i, valorPorTipo[i])
        dictToString = dictToString[:-1]

    	return '''\
%s -- %i -- %s
%s (%s)
%s (%s)
Resumo dos bens:
    * Total declarado: %.2f R$
    * Total por tipo de bem:
%s
    	''' % (self.__nomeNaUrna, self.__numeroUrna, self.__descricaoCargo,
    	self.__uf, self.__nomeMunicipioNascimento, self.__ufNascimento,
        valorTotal, dictToString)

    def __repr__(self):
    	return str(self)

    def incluirBem(self, novoBem):
    	self.__bens.append(novoBem)

    def __eq__(self, other):
    	return self.__cpf == other.cpf and self.__nomeCandidato == other.nomeCandidato

