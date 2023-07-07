import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet[1,3].value == "Hello xlwings!":
        sheet[1,3].value = "Bye xlwings!"
    else:
        sheet[1,3].value = "Hello xlwings!"


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("columnasHA.xlsm").set_mock_caller()
    main()
