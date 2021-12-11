# Copyright 2021 Gina Häußge & Octoprint contributors
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>

from op_hierarchical_chainmap._ext import (HierarchicalChainMapBase, get_next,
                                           hierarchy_for_key)


def _as_base(obj):
    if isinstance(obj, HierarchicalChainMap):
        return obj.base
    return obj


class HierarchicalChainMap:
    def __init__(self, *args):
        self.base = HierarchicalChainMapBase(*args)

    @property
    def parents(self):
        return self.base.parents

    @property
    def maps(self):
        return self.base.maps

    def deep_dict(self):
        return self.base.deep_dict(self.base)

    def __copy__(self):
        return self.base.__copy__()

    def copy(self):
        return self.base.copy()

    def new_child(self):
        return self.base.new_child()

    def __getstate__(self):
        return self.base.__getstate__()

    def __setstate__(self, state):
        return self.base.__setstate__(state)

    def __getitem__(self, arg0):
        return self.base.__getitem__(arg0)

    def __setitem__(self, arg0, arg1):
        return self.base.__setitem__(arg0, arg1)

    def __delitem__(self, arg0):
        return self.base.__delitem__(arg0)

    def __contains__(self, arg0):
        return self.base.__contains__(arg0)

    def __len__(self):
        return self.base.__len__()

    def __iter__(self):
        return self.base.__iter__()

    def items(self):
        return self.base.items()

    def keys(self):
        return self.base.keys()

    def values(self):
        return self.base.values()

    def __eq__(self, arg0):
        return self.base.__eq__(arg0)

    def flatten(self):
        return self.base.flatten()

    def get(self, arg0, default=None):
        return self.base.get(arg0, default)

    def has_path(self, path, only_local=False, only_defaults=False):
        if only_defaults:
            current = self.parents
        elif only_local:
            current = HierarchicalChainMap(self.maps[0])
        else:
            current = self

        try:
            for key in path[:-1]:
                value = current[key]
                if isinstance(value, dict):
                    current = get_next(
                        key, _as_base(current), only_local=only_local
                    )
                else:
                    return False
            return path[-1] in current
        except KeyError:
            return False

    def get_by_path(self, path, only_local=False, only_defaults=False, merged=False):
        if only_defaults:
            current = self.parents
        elif only_local:
            current = HierarchicalChainMap(self.maps[0])
        else:
            current = self

        for key in path[:-1]:
            value = current[key]
            if isinstance(value, dict):
                current = get_next(key, _as_base(current), only_local=only_local)
            else:
                raise KeyError(key)

        if merged:
            current = current.deep_dict()
        return current[path[-1]]

    def set_by_path(self, path, value):
        current = self

        for key in path[:-1]:
            if key not in current.maps[0]:
                current.maps[0][key] = {}
            if not isinstance(current[key], dict):
                raise KeyError(key)
            current = hierarchy_for_key(key, _as_base(current))

        current[path[-1]] = value

    def del_by_path(self, path):
        if not path:
            raise ValueError("Invalid path")

        current = self

        for key in path[:-1]:
            if not isinstance(current[key], dict):
                raise KeyError(key)
            current = hierarchy_for_key(key, _as_base(current))

        del current[path[-1]]
