
class EntityMaster():
    """
    provides a central source for managing all the entities in use.
    """
    def __init__(self):
        self._entities = {}

    def add_entity(self, group, entity):
        if not group in self._entities.keys():
            self._entities[group] = []

        if not entity in self._entities[group]:
            self._entities[group].append(entity)

    def get_entities(self, group):
        results = []
        if group in self._entities.keys():
            results = self._entities[group].copy()
        return results

    def get_all_entities(self):
        results = []
        for group in self._entities:
            results.extend(self._entities[group])
        return results

    def get_first_entity(self, group):
        result = None
        if group in self._entities.keys():
            result = self._entities[group][0]
        return result

    def remove_entity(self, group, entity):
        if group in self._entities:
            self._entities[group].remove(entity)

    def remove_entities(self, group):
        if group in self._entities:
            for entity in self._entities[group]:
                self._entities[group].remove(entity)