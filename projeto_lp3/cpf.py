from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("147.971.499-22"))

cpfs = {
    "331.749.092-02",
    "56392678298"
    "82325423"
}

print(cpf.validate_list(cpfs))