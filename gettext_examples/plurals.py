from . import DemoTranslations

t10n = DemoTranslations({
    ("{count} user", 0): "{count} artykuł",
    ("{count} user", 1): "{count} artykuły",
    ("{count} user", 2): "{count} artykułów",
    ("{count} user", 3): "{count} artykułu",
})

for number in (0, 0.5, 1, 2, 5, 12, 22):
    print(t10n.ngettext("{count} user", "{count} users", number).format(count=number))
