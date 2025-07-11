# 📝 Comparador de Arquivos com Destaque de Diferenças

Este é um projeto simples em Flask para comparação de arquivos linha a linha, com destaque visual das diferenças.  
Atualmente, o foco está na comparação de arquivos `.txt`, com realce nas palavras diferentes entre dois documentos enviados pelo usuário.

## 🚀 Funcionalidades atuais

- Upload de dois arquivos `.txt`
- Comparação linha a linha
- Destaque das palavras diferentes no segundo arquivo
- Interface web simples usando HTML + CSS

## 🛠️ Tecnologias utilizadas

- Python 3
- Flask
- HTML5 + CSS3
- difflib (biblioteca nativa do Python para comparação de texto)

## 📦 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências (de preferência em um ambiente virtual):
```bash
pip install flask
```

3. Execute a aplicação:
```bash
bash
python app.py
```

4. Acesse no navegador:
```bash
http://localhost:5000
```

📌 Exemplo de uso
Ao enviar dois arquivos .txt, a interface exibirá as linhas correspondentes lado a lado, com as palavras diferentes destacadas em verde.

⚠️ Em desenvolvimento
Este projeto ainda está em evolução. As próximas melhorias planejadas incluem:

 Suporte à comparação de arquivos .json e .log

 Detecção de diferenças mais precisa (nível de caractere e estrutura)

 Interface gráfica mais moderna (Bootstrap ou Tailwind)

 Opção para download do resultado em HTML

 Versão responsiva para dispositivos móveis

🤝 Contribuições
Sinta-se à vontade para sugerir melhorias, abrir issues ou enviar pull requests. Toda ajuda é bem-vinda!
