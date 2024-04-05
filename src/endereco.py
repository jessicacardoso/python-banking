from dataclasses import dataclass
from typing import Optional


@dataclass
class Endereco:
    cep: int
    bairro: str
    logradouro: str
    numero: int
    complemento: str
    cidade: str
    estado: str
    ponto_referencia: Optional[str]
