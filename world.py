from typing import Iterable

from base.component import Component


class World:
    def __init__(self) -> None:
        self._entities: dict[int, dict[type[Component], Component]] = {}
        self._components: dict[type[Component], dict[int, Component]] = {}
        self._entity_id: int = 0

    def new_entity(self) -> int:
        self._entity_id += 1
        self._entities[self._entity_id] = {}

        return self._entity_id

    def add_components(self, entity_id: int, components: Iterable[Component]) -> None:
        for component in components:
            component_type = type(component)

            if component_type not in self._components:
                self._components[component_type] = {}

            self._components[component_type][entity_id] = component
            self._entities[entity_id][component_type] = component

    def get_components(self, entity_id: int) -> dict[type[Component], Component]:
        return self._entities.get(entity_id, {})

    def query_components(
        self, components_type: list[type[Component]]
    ) -> list[dict[type[Component], Component]]:
        comp_amount = len(components_type)
        query = []
        for entity_id, comp_map in self._entities.items():
            comp = {}

            for comp_type in components_type:
                if comp_type in comp_map:
                    comp[comp_type] = comp_map[comp_type]

            if len(comp) == comp_amount:
                query.append(comp)

        return query
