from unittest.mock import Mock

m = Mock()
m.side_effect = ["foo", "bar", "baz"]

assert m() == "foo"
assert m() == "bar"
assert m() == "baz"
