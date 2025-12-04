# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.
from collections import OrderedDict
from typing import Iterable, Mapping, Tuple, TypeVar, Union


K = TypeVar('K')
V = TypeVar('V')


class FrozenOdict(Mapping[K, V]):
    """
    An immutable, hashable, and ordered mapping.

    `FrozenOdict` behaves similarly to an `OrderedDict` but is immutable and hashable,
    making it suitable for use as dictionary keys or set members.

    Parameters
    ----------
    key_value_mapping_or_key_value_pairs : Mapping[K, V] or Iterable[Tuple[K, V]]
        An existing mapping or an iterable of key-value pairs to initialize the mapping.
    **kwargs
        Additional key-value pairs to include.

    Example
    -------
    >>> from frozen_odict import FrozenOdict
    >>> fod = FrozenOdict({'a': 1, 'b': 2}, c=3)
    >>> fod
    FrozenOdict([('a', 1), ('b', 2), ('c', 3)])
    >>> hash(fod)
    -8237481104735627500
    """
    __slots__ = (
        'odict',
        'cached_hash_value',
    )

    def __new__(
        cls,
        key_value_mapping_or_key_value_pairs,  # type: Union[Mapping[K, V], Iterable[Tuple[K, V]]]
        **kwargs
    ):
        """
        Create a new FrozenOdict.

        Accepts a mapping object or iterable of (key, value) pairs and optional keyword arguments.

        Raises
        ------
        ValueError
            If the first argument is not a mapping or iterable of pairs.
        """
        odict = OrderedDict()

        if isinstance(key_value_mapping_or_key_value_pairs, Mapping):
            for key, value in key_value_mapping_or_key_value_pairs.items():
                odict[key] = value
        elif isinstance(key_value_mapping_or_key_value_pairs, Iterable):
            for key, value in key_value_mapping_or_key_value_pairs:
                odict[key] = value
        else:
            raise ValueError(
                'key_value_mapping_or_key_value_pairs '
                'must be Union[Mapping[K, V], Iterable[Tuple[K, V]]]'
            )

        for key, value in kwargs.items():
            odict[key] = value

        instance = super(FrozenOdict, cls).__new__(cls)
        instance.odict = odict
        instance.cached_hash_value = None
        return instance

    def __contains__(self, key):
        """
        Return True if key is in the mapping.
        """
        return key in self.odict

    def __eq__(self, other):
        """
        Return True if other is a FrozenOdict with equal ordered items.
        """
        return (
            isinstance(other, FrozenOdict)
            and self.odict == other.odict
        )

    def __getitem__(self, key):
        # type: (K) -> V
        """
        Get value corresponding to key.
        """
        return self.odict[key]

    def __hash__(self):
        """
        Compute and cache the hash of the FrozenOdict.
        """
        if self.cached_hash_value is None:
            hash_value = hash(self.__reduce__())
            self.cached_hash_value = hash_value
            return hash_value
        else:
            return self.cached_hash_value

    def __iter__(self):
        """
        Iterate over keys in order.
        """
        return iter(self.odict)

    def __len__(self):
        """
        Return the number of items.
        """
        return len(self.odict)

    def __reduce__(self):
        """
        Return value for pickling.
        """
        return self.__class__, tuple(self.odict.items())

    def __repr__(self):
        """
        Return str representation of the object.
        """
        return '%s([%s])' % (
            self.__class__.__name__,
            ', '.join(map(repr, self.odict.items()))
        )
