from openpyxl import load_workbook


class ExcelReader:

    def __init__(self, file_path):

        self.workbook = load_workbook(
            file_path
        )

        self.sheet = self.workbook.active

    def get_login_data(self):

        username = self.sheet["A2"].value

        password = self.sheet["B2"].value

        return username, password