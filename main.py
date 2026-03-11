import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from pathlib import Path


# olhar base de dados/importar dados
tabela = pd.read_csv('horas_extras.csv')
print(tabela)

# criar pasta de saida
pasta_saida = Path("relatorios")
pasta_saida.mkdir(exist_ok=True)

# criar 1 item para cada item da base de dados
for linha in tabela.index:
    nome = tabela.loc[linha, "Nome"]
    departamento = tabela.loc[linha, "Departamento"]
    horas_extras = tabela.loc[linha, "Horas Extras"]
    mes_ref = tabela.loc[linha, "Referência"]
    
    # nome do arquivo seguro (sem espacos e caracteres especiais)
    nome_arquivo = nome.replace(" ", "_").replace("/", "_")
    arquivo_pdf = pasta_saida / f"relatorio_horas_extras_{nome_arquivo}.pdf"
    
    documento_pdf = canvas.Canvas(str(arquivo_pdf), pagesize=A4)
    
    # titulo
    documento_pdf.setFont("Helvetica-Bold", 16)
    documento_pdf.drawString(100, 750, f"Relatório de Horas Extras")
    
    # escreve o texto
    documento_pdf.setFont("Helvetica", 12)
    documento_pdf.drawString(100, 700, f"Nome: {nome}")
    documento_pdf.drawString(100, 670, f"Departamento: {departamento}")
    documento_pdf.drawString(100, 640, f"Horas extras: {horas_extras}")
    documento_pdf.drawString(100, 610, f"Referencia: {mes_ref}")
    documento_pdf.drawString(100, 580, f"Esse texto foi gerado automaticamente com python")
    
    # salvar relatorio
    documento_pdf.save()
    print(f"PDF gerado: {arquivo_pdf.resolve()}")

print("Todos os relatórios foram gerados com sucesso!")
