from icu import MessageFormat, Locale

mf = MessageFormat('Witaj świecie!', Locale('pl'))

print(mf.format([]))
