def encaixa(a, b):
  """
  Retorna True se o segundo valor encaixa no primeiro valor, e False caso contrário.

  Args:
    a: O primeiro valor.
    b: O segundo valor.

  Returns:
    True se o segundo valor encaixa no primeiro valor, e False caso contrário.
  """

  if b == 0:
    return False

  while b > 0:
    if a % b != 0:
      return False

    a = a // b

  return True


def main():
  """
  Função principal.
  """

  n = int(input())

  for _ in range(n):
    a, b = input().split()

    a = int(a)
    b = int(b)

    print("SIM" if encaixa(a, b) else "NÃO")


if __name__ == "__main__":
  main()