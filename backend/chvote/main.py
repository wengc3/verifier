import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from VoteSimulation import VoteSimulation

def main():
    automatic = True
    verbose = True
    simulation = VoteSimulation(os.path.join("profiles", "default.json"))
    simulation.run(automatic, verbose)

if __name__ == '__main__':
    main()
