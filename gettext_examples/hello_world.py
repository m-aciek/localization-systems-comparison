from gettext_examples import DemoTranslations

t10n = DemoTranslations({
    "Hello world!": "Witaj świecie!",
})

print(t10n.gettext("Hello world!"))
