# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import math

import util
from game import Directions
from typing import List


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # La pila almacena pares (estado, accion para llegar a ese estado)
    # de estados que quedan por visitar y ya visitados
    pila = util.Stack()
    estados_visitados = set()  # Almacena los estados visitados
    lista_acciones = []  # Almacena las acciones para llegar al estado objetivo

    # Añadimos el estado inicial al conjunto de estados visitados
    estados_visitados.add(problem.getStartState())
    # Obtenemos los sucesores del estado inicial
    sucesores = problem.getSuccessors(problem.getStartState())

    # Añadimos los sucesores del estado inicial a la pila
    for sucesor in sucesores:
        pila.push((sucesor[0], sucesor[1]))

    # Mientras la pila no esté vacía, seguimos buscando
    while not pila.isEmpty():
        terna_estado_actual = pila.list[-1]  # Obtenemos el último elemento de la pila

        # Si el estado actual no ha sido visitado, añadimos a la lista de acciones
        # la acción para llegar a ese estado, y comprobamos si es el estado objetivo.
        if terna_estado_actual[0] not in estados_visitados:
            lista_acciones.append(terna_estado_actual[1])
            # Si el estado actual es el objetivo, devolvemos la lista de acciones
            if problem.isGoalState(terna_estado_actual[0]):
                return lista_acciones
            else:
                # Si no lo es, lo añadimos al conjunto de estados visitados
                estados_visitados.add(terna_estado_actual[0])

            # Obtenemos los sucesores del estado actual
            sucesores = problem.getSuccessors(terna_estado_actual[0])
            for sucesor in sucesores:
                # Si el sucesor no ha sido visitado, lo añadimos a la pila
                if sucesor[0] not in estados_visitados:
                    pila.push((sucesor[0], sucesor[1]))
        else:
            # Si el estado actual ya ha sido visitado, lo eliminamos de la pila y de la lista de acciones
            pila.pop()
            lista_acciones.pop()


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def funcionheuristicaeuclidea(state, problem) -> float:
    objetivo = problem.goal
    posactual = state
    dist = math.sqrt((posactual[0] - objetivo[0]) ** 2 + (posactual[1] - objetivo[1]) ** 2)
    # print(f"Actual: {posactual[0]}, {posactual[1]} | dist: {dist}")
    return dist


def funcionheuristicamanhattan(state, problem) -> float:
    objetivo = problem.goal
    posactual = state
    dist = abs(posactual[0] - objetivo[0]) + abs(posactual[1] - objetivo[1])
    # print(f"Actual: {posactual[0]}, {posactual[1]} | dist: {dist}")
    return dist


# Función auxiliar que genera la lista de movimientos para llegar al objetivo
# a partir de los nodos.
def generarlista(estado_objetivo, nodos) -> List[Directions]:
    ruta = []
    while nodos[estado_objetivo][2] is not None:
        ruta.insert(0, nodos[estado_objetivo][0])
        estado_objetivo = nodos[estado_objetivo][2]

    return ruta


def aStarSearch(problem: SearchProblem, heuristic=funcionheuristicaeuclidea) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    colap = util.PriorityQueue()  # Cola por prioridad de tuplas (estado, valor_f)
    nodos = {}  # Diccionario de listas [movimiento, coste_acumulado, estado_anterior]

    nodos[problem.getStartState()] = [None, 0, None]
    estado_actual = problem.getStartState()
    coste_acumulado = nodos[estado_actual][1]

    # Obtenemos los sucesores del estado actual
    lista_tuplas_sucesores = problem.getSuccessors(estado_actual)

    for sucesor in lista_tuplas_sucesores:
        nuevo_coste = coste_acumulado + sucesor[2]  # Coste acumulado hasta llegar al sucesor
        valor_f = nuevo_coste + heuristic(sucesor[0],
                                          problem)  # Valor f del sucesor (coste para llegar a él + heurística)
        colap.push(sucesor, valor_f)  # Añadimos el sucesor y su valor f a la cola
        nodos[sucesor[0]] = [sucesor[1], nuevo_coste, estado_actual]  # Añadimos el sucesor al diccionario de nodos

    while not colap.isEmpty():
        estado_actual = colap.pop()[0]  # Obtenemos el estado con menor valor f
        coste_acumulado = nodos[estado_actual][1]  # Coste acumulado hasta el estado actual

        # Si se ha alcanzado el objetivo, generamos la lista de movimientos para llegar a él
        if problem.isGoalState(estado_actual):
            return generarlista(estado_actual, nodos)  # Objetivo alcanzado

        lista_tuplas_sucesores = problem.getSuccessors(estado_actual)

        for sucesor in lista_tuplas_sucesores:
            nuevo_coste = coste_acumulado + sucesor[2]  # Coste acumulado hasta llegar al sucesor
            valor_f = nuevo_coste + heuristic(sucesor[0],
                                              problem)  # Valor f del sucesor (coste para llegar a él + heurística)

            # Si el sucesor no ha sido visitado o el nuevo coste es menor que el anterior, lo añadimos a la cola
            if sucesor[0] not in nodos or nuevo_coste < nodos[sucesor[0]][1]:
                colap.update(sucesor, valor_f)
                nodos[sucesor[0]] = [sucesor[1], nuevo_coste, estado_actual]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
heuc = funcionheuristicaeuclidea
hman = funcionheuristicamanhattan
