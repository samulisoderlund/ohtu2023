from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn


class QueryBuilder():

    def __init__(self, query = All()) -> None:
        self._query = query

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))

    def build(self):
        return self._query
