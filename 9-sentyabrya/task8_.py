class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots
        self.mem_slots_list = []  

    def set_memory(self, *memories):
        if len(memories) > 4:
            raise ValueError("Можно передать не более 4 модулей памяти")
        self.mem_slots_list = list(memories)

    def get_config(self):
        lines = [
            f"Материнская плата: {self.name}",
            f"Процессор: {self.cpu.name} ({self.cpu.fr} ГГц)",
            f"Слоты памяти: {self.mem_slots}",
        ]

        mem_info = [f"{m.name} ({m.volume} ГБ)" for m in self.mem_slots_list]
        if mem_info:
            lines.append("Память: " + ", ".join(mem_info))
        else:
            lines.append("Память: не установлена")

        return lines


cpu = CPU("Intel Core i7", 3.6)
mb = MotherBoard("ASUS Prime", cpu, 4)

mb.set_memory(
    Memory("Kingston", 8),
    Memory("Kingston", 8),
)

for line in mb.get_config():
    print(line)