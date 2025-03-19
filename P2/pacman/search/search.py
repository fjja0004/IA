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
    # La pila almacena pares (estado, accion llegar a ese estado)
    # de estados que quedan por visitar y ya visitados
    pila = util.Stack()
    estados_visitados = set()  # Almacena los estados visitados
    lista_acciones = []  # Almacena las acciones para llegar al estado objetivo

    # Añadimos el estado inicial al conjunto de estados visitados
    estados_visitados.add(problem.getStartState())
    # Obtenemos los sucesores del estado inicial
    sucesores = problem.getSuccessors(problem.getStartState())

    # Para cada sucesor del estado inicial, comprobamos si no ha sido visitado,
    # y en ese caso, lo añadimos a la pila.
    for sucesor in sucesores:
        if sucesor[0] not in estados_visitados:
            pila.push((sucesor[0], sucesor[1]))

    # Mientras la pila no esté vacía, seguimos buscando
    while not pila.isEmpty():
        estado_actual = pila.list[-1]  # Obtenemos el último elemento de la pila

        # Si el estado actual no ha sido visitado, añadimos a la lista de acciones
        # la acción para llegar a ese estado, y comprobamos si es el estado objetivo.
        if estado_actual[0] not in estados_visitados:
            lista_acciones.append(estado_actual[1])
            if problem.isGoalState(estado_actual[0]):
                return lista_acciones
            else:
                # Si no lo es, lo añadimos al conjunto de estados visitados
                estados_visitados.add(estado_actual[0])

            # Obtenemos los sucesores del estado actual
            sucesores = problem.getSuccessors(estado_actual[0])
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
    return dist

def generarlista(estado_objetivo, predecesores) -> List[Directions]:
    ruta = []
    while predecesores[estado_objetivo][2] is not None:
        ruta.insert(0, predecesores[estado_objetivo][0])
        estado_objetivo = predecesores[estado_objetivo][2]

    return ruta

def aStarSearch(problem: SearchProblem, heuristic=funcionheuristicaeuclidea) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    colap = util.PriorityQueue() # Cola por prioridad
    estados_visitados = set()  # Almacena los estados visitados
    predecesores = {} # Diccionario de listas [movimiento, costeac, estadoant]

    estados_visitados.add(problem.getStartState())
    predecesores[problem.getStartState()] = [None, 0, None]

    estado_actual = problem.getStartState()
    listatuplas = problem.getSuccessors(estado_actual)
    costeac = predecesores[estado_actual][1]
    for tupla in listatuplas:
        if tupla[0] not in estados_visitados:
            valorf = tupla[2] + 0 + heuristic(tupla[0], problem)
            colap.push(tupla, valorf)
            predecesores[tupla[0]] = [tupla[1], costeac + tupla[2], estado_actual]

    while not colap.isEmpty():
        estado_actual, accion, coste = colap.pop()
        costeac = predecesores[estado_actual][1]

        if problem.isGoalState(estado_actual):
            return generarlista(estado_actual, predecesores)  # Objetivo alcanzado

        if estado_actual not in estados_visitados:
            estados_visitados.add(estado_actual)

        listatuplas = problem.getSuccessors(estado_actual)
        for tupla in listatuplas:
            valorf = tupla[2] + costeac + heuristic(tupla[0], problem)
            colap.push(tupla, valorf)
            predecesores[tupla[0]] = [tupla[1], costeac + tupla[2], estado_actual]

    return []





# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
