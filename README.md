# `frozen-odict`

An immutable, hashable, and ordered mapping.

`FrozenOdict` behaves similarly to an `OrderedDict` but is immutable and hashable, making it suitable for use as dictionary keys or set members.

## Installation

```bash
pip install frozen-odict
```

## Usage

```python
from frozen_odict import FrozenOdict

# Create from a mapping
fod1 = FrozenOdict({'a': 1, 'b': 2})

# Create from sequence of pairs
fod2 = FrozenOdict([('x', 100), ('y', 200)])

# Create with keyword arguments
fod3 = FrozenOdict({'foo': 42}, bar=43)

# Hashable and set-usable
s = {fod1, fod2}
if fod1 in s:
    print("Found!")

# Works as dictionary keys!
d = {fod1: "first", fod2: "second"}

print(fod1)  # FrozenOdict([('a', 1), ('b', 2)])
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).