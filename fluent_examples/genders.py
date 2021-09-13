from fluent_examples import DemoLocalization

l10n = DemoLocalization("""
save-and-add-another = {$gender ->
    [masculine-animate] Zapisz i dodaj kolejnego
   *[masculine-inanimate] Zapisz i dodaj kolejny
    [feminine] Zapisz i dodaj kolejną
    [neuter] Zapisz i dodaj kolejne
}
""", locale="pl")

for gender in ("masculine-animate", "masculine-inanimate", "feminine", "neuter"):
    print(l10n.format_value("save-and-add-another", {'gender': gender}))
