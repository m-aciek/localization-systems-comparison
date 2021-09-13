from gettext_examples import DemoTranslations

t10n = DemoTranslations({
    "masculine animate\x04Save and add another": "Zapisz i dodaj kolejnego",
    "masculine inanimate\x04Save and add another": "Zapisz i dodaj kolejny",
    "feminine\x04Save and add another": "Zapisz i dodaj kolejną",
    "neuter\x04Save and add another": "Zapisz i dodaj kolejne",
})

for gender in ("masculine animate", "masculine inanimate", "feminine", "neuter"):
    print(t10n.pgettext(gender, "Save and add another"))
