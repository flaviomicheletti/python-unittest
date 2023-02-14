from unittest.mock import Mock

m = Mock()
m.side_effect = ["foo", "bar", "baz"]
m()
# 'foo'
m()
# 'bar'
m()
# 'baz'
