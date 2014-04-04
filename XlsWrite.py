import xlsxwriter

class XlsWrite:
    def __init__(self, cake_list):
        self.cake_list = cake_list
        self.workbook = xlsxwriter.Workbook("Cakes.xlsx")
        self.worksheet = self.workbook.add_worksheet()
        self.rows = len(cake_list)
        self.cols = 5

        
    def populate_excel(self):
        row = 0

        for cake in self.cake_list:
            self.worksheet.write(row, 0, cake.name)
            self.worksheet.write(row, 1, cake.url)
            self.worksheet.write(row, 2, cake.price)
            self.worksheet.write(row, 3, cake.desc)
            self.worksheet.write(row, 4, cake.img_src)

            row += 1

        self.workbook.close()
