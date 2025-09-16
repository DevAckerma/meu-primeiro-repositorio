

from escola_main import Pessoa,Curso,Notas,Aluno,Morada,Local_Nascimento,Endereco

#O programa ainda não foi finalizado, este é apenas um script de avaliação

#O aluno não vai poder manipular as disciplinas que estão no curso, tudo isso estará a cabo da escola



def trimestral(trimestre,aluno):

if len(aluno.notas)!=0:

    for a in aluno.notas:

        if a.trimestre==trimestre:

            return (a.disciplinas())

    return "Este trimestre ainda não foi inserido"

return "O aluno ainda não cumpriu qualquer trimestre."

if str(input("Deseja inserir algum aluno S//N : ")).lower().strip()=="s":

print("##################### Curso ################################\n")



curso=Curso(input("Digite o nome do curso em que o Aluno se inscreve : "))



print("\n##################### Local Nasscimento ################################")



nascimento=(Endereco(municipio=input("\nDigite o Municipio : "),provincia=input("\nDigite a Provincia : "),pais=input("\nDigite o País : ")))

print("\n##################### Morada ################################")



morada=(Endereco(input("\nDigite o Municipio : "),input("\nDigite a Provincia : "),input("\nDigite o País : ")))



aluno=Aluno(nome=input(("\nDigite o nome do aluno :")), nascimento=input(("\nDigite a data de nascime)nto do aluno : ")), sexo=input("\nDigite o sexo do Aluno :"), numero_identificador=input("\nDigite o numero do Bi do Aluno : "), local_nascimento=nascimento, morada=morada,classe=input("\nDigite a classe do aluno : "),curso=curso,turma=None,email=None)



trimestre=int(input("\nQual trimestre vc quer ver : ")) 

print(trimestral(trimestre,aluno))





aluno.curso.add_disciplinas(aluno.classe,"Quimica","Historia","Fisica","Matematica")#Podes adicionar mais disciplinas ao curso para poder testar

print(aluno.curso.disciplinas(aluno.classe))

while True:

    print("######################################################\n")



    adicionar_trimestre=int(input("Qual trimestre quer trabalhar  : "))



    aluno.notas.append(Notas(adicionar_trimestre,aluno.curso,aluno.classe))

    for a in aluno.notas:

        if a.trimestre==adicionar_trimestre:

            a.adicionar_nota(input("\nDigite a disciplina que vai ser adicionada a nota : "),str(input("\nDigite a nota : ")))

            break



    trimestre=int(input("\nQual trimestre vc quer ver : ")) 

    print(trimestral(trimestre,aluno))

else:

print("Não foi dessa")

