from typing import Dict, List, Tuple, Set
versions: tuple = (1, 2, 3)

options: dict = {'air conditioned': True, 'aluminium wheels': True}

values: set = {3, 4, 5, 6}

print(__annotations__)

print("--------------------------------------------------")


names: List[str] = ['Ronaldo', 'Battisti']

versions: Tuple[int, int, int] = (3, 7, 4)

options: Dict[str, bool] = {'air conditioned': True, 'aluminium wheels': True}

values: set[int] = {3, 4, 5, 6}

print(__annotations__)
