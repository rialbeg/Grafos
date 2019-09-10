import bisect 
import statistics as st



class Vertice(object):

    total_vertices = 0
    identificacao = 0

    def __init__(self, nome):
        self.nome = nome
        self.id = Vertice.identificacao
        Vertice.identificacao += 1
        self.grau = 0

    def __str__(self):
        return "Vertice: %s || Grau: %s || Identificação: %s" % (self.nome, self.grau, self.id)



class Aresta(object):

    total_arestas = 0
    identificacao = 0

    def __init__(self, vertice_a, vertice_b, peso=1):
        vertice_a.grau += 1
        vertice_b.grau += 1
        self.vertice_pai = vertice_a
        self.vertice_mae = vertice_b
        self.peso = peso
        self.id = Aresta.identificacao
        Aresta.identificacao += 1


    def __str__(self):
        return "Aresta %s || Entre os vertices %s e %s" % (
            self.id, self.vertice_pai.id, self.vertice_mae.id
        )

#
class Grafo(object):
   

    def __init__(self):
        self.v_list = []
        self.a_list = []
        self.g_list = []

    def add_vertice(self, vertice_a):
        self.v_list.append(vertice_a)
        return "Vertice adicionado"

    def add_aresta(self, aresta_a):
        self.a_list.append(aresta_a) 

        if (aresta_a.vertice_pai.grau) not in self.g_list:
          bisect.insort(self.g_list,aresta_a.vertice_pai.grau) 
        if(aresta_a.vertice_mae.grau) not in self.g_list:  
          bisect.insort(self.g_list,aresta_a.vertice_mae.grau) 
        return "Aresta adicionada"

    def del_vertice(self, vertice_a):
        if vertice_a in self.v_list:
            self.v_list.remove(vertice_a)
            for aresta in self.a_list:
                if (aresta.vertice_mae.id == vertice_a.id) or (aresta.vertice_pai.id == vertice_a.id):
                    self.a_list.remove(aresta)
            return "Vertice removido"
        else:
            return "Vertice não encontrado"

    def del_aresta(self, aresta_a):
        if aresta_a in self.a_list:
            self.a_list.remove(aresta_a)
            return "Aresta removida"
        else:
            return "Aresta não encontrada"

    def vert_adj(self,vertice_a):
        res = list()
        if vertice_a in self.v_list:
            for aresta in self.a_list:
                if (aresta.vertice_mae.id == vertice_a.id):
                    res.append(aresta.vertice_pai.id) 
                if (aresta.vertice_pai.id == vertice_a.id):
                    res.append(aresta.vertice_mae.id)

            return res        
        else:
            return "Vertice nao encontrado"  

    def show_v(self):
        for vertice in self.v_list:
            print(vertice)

    def show_a(self):
        for aresta in self.a_list:
            print(aresta)        
    def min_max(self):
        res = [self.g_list[0], self.g_list[-1]]
        return res
    def avg_deg(self):
        avg = 0
        for vertice in self.v_list:
            avg += vertice.grau
        return avg/len(self.v_list)  
        
V0 = Vertice("V0")
V1 = Vertice("V1")
V2 = Vertice("V2")
V3 = Vertice("V3")
V4 = Vertice("V4")

A0 = Aresta(V0,V1)
A1 = Aresta(V0,V4)
A2 = Aresta(V1,V4)
A3 = Aresta(V1,V3)
A4 = Aresta(V3,V4)
A5 = Aresta(V1,V2)
A6 = Aresta(V2,V3)



G = Grafo()

G.add_vertice(V0)
G.add_vertice(V1)
G.add_vertice(V2)
G.add_vertice(V3)
G.add_vertice(V4)

G.add_aresta(A0)
G.add_aresta(A1)
G.add_aresta(A2)
G.add_aresta(A3)
G.add_aresta(A4)
G.add_aresta(A5)
G.add_aresta(A6)



