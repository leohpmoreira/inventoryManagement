CREATE TABLE Produtos (
    Cod INTEGER PRIMARY KEY,
    Categoria INTEGER,
    Nome TEXT NOT NULL,
    Fabricante TEXT NOT NULL,
    Custo REAL NOT NULL,
    Preco REAL NOT NULL,
    FOREIGN KEY (Categoria) REFERENCES Categoria (Cod)
);

CREATE TABLE Movimentacao (
    ID INTEGER PRIMARY KEY,
    Tipo TEXT NOT NULL,
    Cod_prod TEXT NOT NULL,
    Qtd INTEGER NOT NULL,
    FOREIGN KEY (Cod_prod) REFERENCES Produtos (Cod)
);

CREATE TABLE Estoque (
    Cod_prod INTEGER PRIMARY KEY,
    Qtd INTEGER,
    FOREIGN KEY (Cod_prod) REFERENCES Produtos (Cod)
);

CREATE TABLE Categoria (
    Cod INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL
);

CREATE TABLE Login (
    UserID TEXT NOT NULL PRIMARY KEY,
    Password TEXT NOT NULL,
    Type TEXT NOT NULL
);

CREATE TRIGGER  IF NOT EXISTS Trg_auto_estoque
AFTER INSERT ON Movimentacao
FOR EACH ROW
BEGIN
    UPDATE Estoque SET Qtd = CASE
        WHEN NEW.Tipo = 'E'
            THEN Qtd + NEW.Qtd
            ELSE Qtd - NEW.Qtd END
        WHERE Cod_prod = NEW.Cod_prod;
END;

