# CPU, RAM, VGA, SSD를 구성요소로 가지고 잇는 Computer 클래스를 상의해서 인스턴스를 생성하는 프로그램.
# Computer 클래스는 각 구성요소의 값을 저장할 수 있는 set_spec() 메서드와 구성요소의 값을
# 출력할 수 있는 hardware_info() 메서드로 구성


class Computer:

    def set_spec(self, CPU, RAM, VGA, SSD):
        self.cpu = CPU
        self.ram = RAM
        self.vga = VGA
        self.ssd = SSD

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')


desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX1060', '512GB')
print('desktop 스펙입니다.')
desktop.hardware_info()

notebook = Computer()
notebook.set_spec('i5', '8GB', 'MX300', '256GB')
print()
print('notebook 스펙입니다.')
notebook.hardware_info()
