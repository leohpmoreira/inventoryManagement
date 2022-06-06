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
    Data DATE,
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

CREATE TRIGGER IF NOT EXISTS Trg_entrada_estoque
AFTER INSERT ON Movimentacao WHEN NEW.Tipo = 'E'
BEGIN
    UPDATE Estoque SET Qtd = Qtd + NEW.Qtd WHERE Cod_prod = NEW.Cod_prod;
END;

CREATE TRIGGER IF NOT EXISTS Trg_saida_estoque
AFTER INSERT ON Movimentacao WHEN NEW.Tipo = 'S'
BEGIN
    UPDATE Estoque SET Qtd = Qtd - NEW.Qtd WHERE Cod_prod = NEW.Cod_prod;
END;

CREATE TRIGGER IF NOT EXISTS Trg_novo_produto
AFTER INSERT ON Produtos
FOR EACH ROW
BEGIN
    INSERT INTO Estoque VALUES (NEW.Cod, 0);
END;