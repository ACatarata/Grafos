class Grafo:
    """__init__ é o que inicia o construtor"""
    """self é como se fosse o this do java """

    def __init__(self, rotas):
        self.rotas = rotas
        self.grafo_dic = {}
        for comeco, fim in self.rotas:
            if comeco in self.grafo_dic:
                self.grafo_dic[comeco].append(fim)
            else:
                self.grafo_dic[comeco] = [fim]
        print("Grafo dinâmico : ", self.grafo_dic)


if __name__ == '__main__':
    '''Cidades
    Ituiutaba/Monte Alegre/Uberlandia/Prata/Capinopolis/Canapolis/Campina Verde
    "Ituiutaba","Monte alegre"
    "Ituiutaba","Campina Verde"
    "Ituiutaba","Prata"
    "Ituiutaba","Capinopolis"

    "Monte alegre","Prata"
    "Monte alegre","Uberlandia"
    "Monte alegre","Canapolis"

    "Uberlandia","Prata"

    "Prata","Campina Verde"
    "Prata","Canapolis"

    "Capinopolis","Canapolis"
    '''
    rotas = [("Ituiutaba", "Monte Alegre"), ("Ituiutaba", "Campina Verde"), ("Ituiutaba", "Prata"), ("Ituiutaba", "Capinopolis"), ("Monte alegre", "Prata"), ("Monte alegre", "Uberlandia"),
             ("Monte alegre", "Canapolis"), ("Uberlandia", "Prata"), ("Prata", "Campina Verde"), ("Prata", "Canapolis"), ("Capinopolis", "Canapolis")]
    #Grafo statico 
    grafo_dic = {"Ituiutaba": ["Monte Alegre", "Campina Verde", "Prata", "Capinopolis"],
                 "Monte alegre": ["Prata", "Uberlandia", "Canapolis"],
                 "Uberlandia": ["Prata"],
                 "Prata": ["Campina Verde", "Canapolis"],
                 "Capinopolis": ["Canapolis"]}
    print(grafo_dic)
    print("\n")

    grafo_dinamico = Grafo(rotas)
