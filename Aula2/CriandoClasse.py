from collections import defaultdict
class Grafo(object):
  """Implementação basica de um grafo  """
  def __init__(self, arestas , direcionado = False):
    """Inicializa as estruturas base do grafo """
    self.adj = defaultdict(set)
    self.direcionado = direcionado
    self.adiciona_arestas(arestas)
  
  def get_vertices(self):
    """Retorna a kusta de vertices di grafo """
    return list(self.adj.keys())
  
  def get_arestas(self):
    """ Retorna a lista de arestas do grafo """
    return [(k,v) for k in self.adj.keys() for v in self.adj[k]]
  
  def adiciona_arestas(self,arestas):
    """Adiciona arestas ao grafo """
    for u,v in arestas:
      self.adiciona_arco(u,v)
  
  def adiciona_arco(self,u,v):
    """Adiciona uma ligaçao (arco) entre os nodos 'u' e 'v'"""
    self.adj[u].add(v)
    # Se o grafo é não direcionado , precisa adicionar arcos nos dois sentidos.
    if not self.direcionado:
      self.adj[v].add(u)
  
  def existe_arresta(self,u,v):
    """Existe uma aresta entre os vertices 'u' e 'v'"""
    return u in self.adj and v in self.adj[u]
  
  def __len__(self):
    return len(self.adj)
  
  def __str__(self):
    return '{}({})'.format(self.__class__.__name__, dict(self.adj))
  
  def __getitem__(self, v):
    return self.adj[v]