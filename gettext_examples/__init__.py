from gettext import GNUTranslations


class DemoTranslations(GNUTranslations):
    def __init__(self, catalog):
        self._catalog = catalog
        self._fallback = False

    def plural(self, n):
        if n == 1:
            return 0
        if 2 <= n % 10 <= 4 and not (10 < n % 100 < 20):
            return 1
        if n - int(n) != 0:
            return 3
        return 2