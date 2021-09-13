from icu import MessageFormat, Formattable, Locale

# messages.getString("groups-number")

mf = MessageFormat(
    '{0, select, masculine_animate {Zapisz i dodaj kolejnego} masculine_inanimate {Zapisz i dodaj kolejny} feminine {Zapisz i dodaj kolejną} other {Zapisz i dodaj kolejne}}',
    Locale('pl')
)
for gender in ("masculine_animate", "masculine_inanimate", "feminine", "neuter"):
    print(mf.format([Formattable(gender)]))
