from icu import MessageFormat, Formattable, Locale


mf = MessageFormat(
    '{count, plural, one {# artykuł} few {# artykuły} many {# artykułów} other {# artykułu}}',
    Locale('pl')
)
for number in (0, 0.5, 1, 2, 5, 22):
    print(mf.format([Formattable(number)]))
