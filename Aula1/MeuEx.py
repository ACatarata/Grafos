class Grafo:
    def __init__(self, motor):
        self.motor = motor
        self.grafo_dic = {}
        for comeco, fim in self.motor:
            if comeco in self.grafo_dic:
                self.grafo_dic[comeco].append(fim)
            else:
                self.grafo_dic[comeco] = [fim]
        print("Grafo Dinamico : ", self.grafo_dic)


motor = [("Ferrari", "ferrari"), ("Ferrari", "Alfa Romeo Racing"), ("Ferrari", "Hass F1 Team"),
         ("Honda", "AlphaTauri"), ("Honda", "Red Bull"),
         ("Renault", "MCLaren"), ("Renault", "Renault DP"),
         ("Mercedes-AMG", "Mercedes-Petronas"), ("Mercedes-AMG", "Williams"), ("Mercedes-AMG", "Racing Point")]

grafo_dic = {"Ferrari": ["Alfa Romeo Racing", "Hass F1 Team"],
             "Honda": ["AlphaTauri", "Red Bull"],
             "Renault": ["McLaren", "Renault DP"],
             "Mercedes-AMG": ["Mercedes-Petronas", "Williams ", "Racing Point"]}
print(grafo_dic)
print("\n")
grafo_dinamico = Grafo(motor)
