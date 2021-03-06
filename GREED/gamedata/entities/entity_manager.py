#organizes all the entities on screen and provides methods for managing them. 



class Entity_Manager:
    def __init__(self):
        self._entities = {}

    def add_entitiy(self, type, entity):
        if not type in self._entities.keys():
            self._entities[type] = []

        if not entity in self._entities[type]:
            self._entities[type].append(entity)

    def get_entities(self, type):
        if type in self._entities.keys():
            return self._entities[type].copy()
        else:
            return []
    
    def get_all(self):
        results = []
        for group in self._entities:
            results.extend(self._entities[group])
        return results

    def get_first_entity(self, type):
        if type in self._entities.keys():
            return self._entities[type][0]
        else:
            return None

    def del_entity(self, type, entity):
        if type in self._entities:
            self._entities[type].remove(entity)