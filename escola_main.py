
from datetime import *

import string

def validar_letras(nome_atributo,nome):

nome_atributo=nome_atributo.title()



if isinstance(nome,str) and nome!="": 

    nome=nome.strip()

    for caracter in nome:

        if caracter.isdigit():

            raise Exception(f"{nome_atributo} não pode conter números.")

        elif caracter==" ":

            continue

        elif caracter.isalpha():

            continue

        else:

            raise Exception(f"{nome_atributo} não pode conter caracteres especiais.")

    return nome

else:

    raise Exception ("Valor não suportado")

class Endereco():

def __init__(self,municipio,provincia,pais):

    self.municipio=municipio

    self.provincia=provincia

    self.pais=pais



@property

def municipio(self):

    return self._municipio



@municipio.setter

def municipio(self,local):

    nome=validar_letras("municipio",local)

    self._municipio=nome



@property

def provincia(self):

    return self._provincia



@provincia.setter

def provincia(self,local):

    nome=validar_letras("provincia",local)

    self._provincia=nome



@property

def pais(self):

    return self._pais



@pais.setter

def pais(self,local):

    nome=validar_letras("pais",local)

    self._pais=nome

class Local_Nascimento(Endereco):

pass

class Morada(Endereco):

pass

class Pessoa():

def __init__(self,nome,nascimento,sexo,numero_identificador,local_nascimento,morada,email=None):

    self.nome=nome.strip()

    self.nascimento=nascimento

    self.sexo=sexo

    self._email=email

    self.numero_identificador=numero_identificador

    self.morada=morada

    self.local_nascimento=local_nascimento

    

@property

def nome(self):

    return self.__nome



@nome.setter

def nome(self,valor):

    self.__nome=validar_letras("nome",valor)



@property

def nascimento(self):

    return self.__nascimento



@nascimento.setter

def nascimento(self,data):

    formatado=datetime.strptime(data,"%d %m %Y").strftime("%d-%m-%Y")

    self.__nascimento=formatado



@property

def sexo(self):

    return self.__sexo



@sexo.setter

def sexo(self,sexo):

    if isinstance(sexo,str) and sexo.upper() in ["S","M"]:

        self.__sexo=sexo.upper()

    else:

        raise Exception("Valor invalido sexo")



@property

def numero_identificador(self):

    return self.__numero_identificador



@numero_identificador.setter

def numero_identificador(self,identificador):

    if isinstance(identificador,str) and identificador!="":

        caracteres_especiais=string.punctuation

        for caracter in identificador:

            if not caracter  in  string.punctuation:

                continue

            else:

                raise Exception ("Numero de BI não suportado")

        self.__numero_identificador=identificador

    else:

        raise Exception("Identificador não suportado")

    

def add_email(self,novo_email):

    self._email=novo_email

class Curso:

lista_cursos=list()

def __init__(self,nome_curso):

    self.nome=nome_curso

    self.dados=list()

    

    Curso.lista_cursos.append(self)

    

@property

def nome(self):

    return self._nome

@nome.setter

def nome(self,valor):

    self._nome=validar_letras("nome",valor)



def disciplinas(self,classe):

    for a in self.dados:

        if a["classe"]==classe:

            return a["disciplinas"]

    return None



def add_disciplinas(self,classe,*disciplinas):



    for a in disciplinas:

        validar=validar_letras("Disciplina",a)

        del validar

    disciplinas=list(disciplinas)

    classes=dict()



    if len(self.dados)==0:

        classes["classe"]=classe

        classes["disciplinas"]=disciplinas

        self.dados.append(classes.copy())

        del classes

    else:

        for a in self.dados:

            if a["classe"]!=classe:

                cont=True

                continue

            else:

                for b in disciplinas:

                    a["disciplinas"].append(b)

                cont=False

                break      

        if cont:     

            classes["classe"]=classe

            classes["disciplinas"]=list()

            for b in disciplinas:

                classes["disciplinas"].append(b)

            self.dados.append(classes.copy())

class Notas:

def __init__(self,trimestre,curso,classe):

    self.trimestre=trimestre

    self.__disciplinas=list()

    self.course_discipline=curso #Foi usado para poder ter acesso as disciplinas que estão no Curso. Assim, só vai ser possivel add notas ao aluno de acordo o curso...

    self.__classe=classe#...só vai ser possivel add notas ao Aluno de acordo a classe



@property

def trimestre(self):

    return self.__trimestre

@trimestre.setter

def trimestre(self,valor):

    if isinstance(valor,int):

        self.__trimestre=valor

    else:

        raise Exception("Trimestre só pode conter valores inteiros")



def disciplinas(self):

    if len(self.__disciplinas)!=0:

        return self.__disciplinas

    return None



def adicionar_nota (self,disciplina,nota) :#Adiciona notas numa disciplina de acordo o Curso e a Classe

    

    if self.course_discipline.disciplinas(self.__classe) is not None: #Acessa o Curso e verifica se o Curso  já tem disciplinas.

        for  discipline in self.course_discipline.disciplinas(self.__classe):#Acessa cada Disciplina do Curso ##2

            if discipline==disciplina:#verfica se o Curso tem uma disciplina identica ao que esta ser inserida pelo Usuario ##3

                if len(self.__disciplinas)==0:#Verifica se é a primeira vez que estão ser introduzidos dados no Trimestre

                    self.__disciplinas.append({"Disciplina":disciplina,"Notas":[nota]})#Adiciona dados ao trimestre 

                    return True

                else:#Caso não seja a primeira vez que estão ser introduzidos dados  ao Trimestre

                    for dicionario in self.__disciplinas:#Acessa cada disciplina/nota dentro do Trimestre 

                        if dicionario["Disciplina"]==disciplina:#Verifica se dentro do Trimestre já temos os dados de uma Disciplina 

                            dicionario["Notas"].append(nota)

                            return True

                    self.__disciplinas.append({"Disciplina": disciplina,"Notas":[nota]})#É adicionado a Disciplina desejada ao Trimestre,caso não esteja dentro do Trimestre

                    return True                

        return False         

    return None ##1 Caso não haja nenhuma Disciplina no Curso

class Aluno(Pessoa): #Ainda em fase de conclusão

def __init__(self, nome, nascimento, sexo, numero_identificador, local_nascimento, morada,classe,curso,turma=None,email=None):

    super().__init__(nome, nascimento, sexo, numero_identificador, local_nascimento, morada, email)

    self.classe=classe

    self.turma=turma

    self.__curso=curso

    self.notas=list()

@property

def curso(self):

    return self.__curso

    

def add_notas(self,nota):

   self.notas.append(nota)

