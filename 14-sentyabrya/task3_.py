TYPE_OS = 1  # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, name, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
        obj.name = name
        return obj

TYPE_OS = 1
dlg = Dialog("Окно 1")
print(type(dlg).__name__, dlg.name, dlg.name_class)

TYPE_OS = 2
dlg = Dialog("Окно 2")
print(type(dlg).__name__, dlg.name, dlg.name_class)



