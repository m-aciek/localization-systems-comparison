from fluent_examples import DemoLocalization

l10n = DemoLocalization("""
hello-world = Witaj świecie!
""", locale="pl")

print(l10n.format_value("hello-world"))