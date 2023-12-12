class Conta():
  def __init__(self, valor):
    self.valor = valor

  def extrato(self):
    return self.valor
  def pagamento(self, preco):
    if preco > self.valor:
      return 'Saldo insuficiente!'
    else:
      self.valor = self.valor - preco
      return f"pagmento efetuado. Saldo em conta: {self.valor}" 
  def deposito(self, quantia):
    if quantia < 0:
      return "Isto não é possível!"
    else:
      self.valor = self.valor + quantia
      return self.valor