import pysat.solvers
import pysat.formula 

solvers = ['cadical',
           'glucose30',
           'glucose41',
           'lingeling',
           'maplechrono',
           'maplecm',
           'maplesat',
           'minicard',
           'minisat22',
           'minisat-gh']

clauses = ([1, 2, 3], [-1, 2], [-2])

def test_solvers():
    cnf = pysat.formula.CNF()

    for clause in clauses:
        cnf.append(clause)


    for solverName in solvers:
        with pysat.solvers.Solver(name=solverName) as solver:
            solver.append_formula(cnf)
            assert(solver.solve())
            assert(solver.get_model() in [[-1, -2, 3]])
        

