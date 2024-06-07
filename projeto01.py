from fpdf import FPDF

project_description = input('Digite a descrição do projeto: ')
worked_hours = input('Digite a previsão de horas trabalhadas: ')
price_hour = input('Digite o valor por hora trabalhada: ')
term = input('Digite o prazo de entrega do projeto: ')

total_price = int(worked_hours) * int(price_hour)

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial')

pdf.image('template.png', x=0, y=0)

pdf.text(115, 145, project_description)
pdf.text(115, 160, worked_hours)
pdf.text(115, 175, price_hour)
pdf.text(115, 190, term)
pdf.text(115, 205, str(total_price))

pdf.output('Orçamento.pdf')
print('Orçamento gerado com sucesso!!')