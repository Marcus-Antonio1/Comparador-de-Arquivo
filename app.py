from flask import Flask, render_template, request
import difflib
import html

app = Flask("Comparador")

def destacar_diferencas(linha1, linha2):
    palavras1 = linha1.split()
    palavras2 = linha2.split()
    comparador = difflib.SequenceMatcher(None, palavras1, palavras2)

    linha2_destacada = []

    for tag, i1, i2, j1, j2 in comparador.get_opcodes():
        segmento = palavras2[j1:j2]
        if tag == 'equal':
            linha2_destacada.extend(segmento)
        else:
            for word in segmento:
                linha2_destacada.append(f'<span class="diff-insert">{html.escape(word)}</span>')

    return html.escape(linha1), ' '.join(linha2_destacada)

@app.route('/', methods=['GET', 'POST'])
def index():
    comparacoes = []

    if request.method == 'POST':
        if 'file1' not in request.files or 'file2' not in request.files:
            return "Arquivos não enviados.", 400

        try:
            arquivo1 = request.files['file1'].read().decode('utf-8').splitlines()
            arquivo2 = request.files['file2'].read().decode('utf-8').splitlines()
        except UnicodeDecodeError:
            return "Erro ao decodificar os arquivos. Certifique-se de que estão em UTF-8.", 400

        total_linhas = max(len(arquivo1), len(arquivo2))
        for i in range(total_linhas):
            linha1 = arquivo1[i] if i < len(arquivo1) else ""
            linha2 = arquivo2[i] if i < len(arquivo2) else ""
            linha_base, linha_comparada = destacar_diferencas(linha1, linha2)
            comparacoes.append((i + 1, linha_base, linha_comparada))

    return render_template('index.html', diffs=comparacoes)

if __name__ == '__main__':
    print(">> Iniciando o servidor Flask...")
    app.run(debug=True)


