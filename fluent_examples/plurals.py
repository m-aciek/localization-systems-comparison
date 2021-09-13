from . import DemoLocalization

l10n = DemoLocalization("""
number-of-articles = {$count ->
    [one] { $count } artykuł
   *[few] { $count } artykuły
    [many] { $count } artykułów
    [other] { $count } artykułu
}
""", locale="pl")

for number in (0, 0.5, 1, 2, 5, 22):
    print(l10n.format_value("number-of-articles", {'count': number}))