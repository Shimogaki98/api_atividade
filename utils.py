from models import Pessoas, db_session


# insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Bronzatti", idade=25)
    print(pessoa)
    pessoa.save()


# Realiza consultas na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(f'{i.nome},  {i.idade}')


# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Bronzatti').first()
    pessoa.nome = 'Simogaki'
    pessoa.save()


# exclui dados na tabela pessoa
def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Bronzatti')
    pessoa.delete()


if __name__ == '__main__':
    insere_pessoas()
    altera_pessoas()
    exclui_pessoas()
    consulta_pessoas()
