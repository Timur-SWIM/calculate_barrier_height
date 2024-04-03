import math
import pandas as pd
import matplotlib.pyplot as plt

# Исходные данные:
F_Au = 5  # эВ, работа выхода электрона для Au
F_Al = 4.1
F_Cu = 4.4
F_Pt = 5.3

Ksi_Ge = 4  # эВ, энергия сродства атома к электрону (электронное сродство)
Ksi_Si = 4.05
Ksi_GaAs = 4.07
Ksi_InSb = 4.6

Eg_Ge = 0.66  # эВ, ширина запрещенной зоны для Ge
Eg_Si = 1.12
Eg_GaAs = 1.43
Eg_InSb = 0.18

Ro_Ge = 1  # Ом*см, удельное сопротивление германия
Ro_Si = 4.5
Ro_GaAs = 2.5e-3
Ro_InSb = 5e-3

T = 300  # К, температура

ni_Ge = 2.5e13  # см^-3, собственная концентрация носителей
ni_Si = 1.6e13
ni_GaAs = 1.1e7
ni_InSb = 2e16

Mn_Ge = 3900  # см^2*В^-1*с^-1, подвижность электронов
Mn_Si = 1500
Mn_GaAs = 8500
Mn_InSb = 78000

def calculate_barrier_height(F, Ksi, Eg, Ro, T, ni, Mn):
    # Константы:
    k = 8.6173303e-5  # эВ·К^-1
    q = 1.6e-19  # Кл

    # формулы для расчета
    ND = 1 / (q * Mn * Ro)  # см^-3, концентрация легирующего вещества (донорная концентрация)
    Fi_0 = k * T * math.log(ND / ni)  # эВ, объемное положение уровня Ферми
    Delta_Fi = F - Ksi - Eg / 2 + Fi_0  # эВ, высота потенциального барьера в диоде Шоттки
    
    return Delta_Fi

# Список исходных данных
data = [
    {"Material": "Au->Ge", "F": F_Au, "Ksi": Ksi_Ge, "Eg": Eg_Ge, "Ro": Ro_Ge, "T": T, "ni": ni_Ge, "Mn": Mn_Ge},
    {"Material": "Au->Si", "F": F_Au, "Ksi": Ksi_Si, "Eg": Eg_Si, "Ro": Ro_Si, "T": T, "ni": ni_Si, "Mn": Mn_Si},
    {"Material": "Au->GaAs", "F": F_Au, "Ksi": Ksi_GaAs, "Eg": Eg_GaAs, "Ro": Ro_GaAs, "T": T, "ni": ni_GaAs, "Mn": Mn_GaAs},
    {"Material": "Au->InSb", "F": F_Au, "Ksi": Ksi_InSb, "Eg": Eg_InSb, "Ro": Ro_InSb, "T": T, "ni": ni_InSb, "Mn": Mn_InSb},
    {"Material": "Al->Ge", "F": F_Al, "Ksi": Ksi_Ge, "Eg": Eg_Ge, "Ro": Ro_Ge, "T": T, "ni": ni_Ge, "Mn": Mn_Ge},
    {"Material": "Al->Si", "F": F_Al, "Ksi": Ksi_Si, "Eg": Eg_Si, "Ro": Ro_Si, "T": T, "ni": ni_Si, "Mn": Mn_Si},
    {"Material": "Al->GaAs", "F": F_Al, "Ksi": Ksi_GaAs, "Eg": Eg_GaAs, "Ro": Ro_GaAs, "T": T, "ni": ni_GaAs, "Mn": Mn_GaAs},
    {"Material": "Al->InSb", "F": F_Al, "Ksi": Ksi_InSb, "Eg": Eg_InSb, "Ro": Ro_InSb, "T": T, "ni": ni_InSb, "Mn": Mn_InSb},
    {"Material": "Cu->Ge", "F": F_Cu, "Ksi": Ksi_Ge, "Eg": Eg_Ge, "Ro": Ro_Ge, "T": T, "ni": ni_Ge, "Mn": Mn_Ge},
    {"Material": "Cu->Si", "F": F_Cu, "Ksi": Ksi_Si, "Eg": Eg_Si, "Ro": Ro_Si, "T": T, "ni": ni_Si, "Mn": Mn_Si},
    {"Material": "Cu->GaAs", "F": F_Cu, "Ksi": Ksi_GaAs, "Eg": Eg_GaAs, "Ro": Ro_GaAs, "T": T, "ni": ni_GaAs, "Mn": Mn_GaAs},
    {"Material": "Cu->InSb", "F": F_Cu, "Ksi": Ksi_InSb, "Eg": Eg_InSb, "Ro": Ro_InSb, "T": T, "ni": ni_InSb, "Mn": Mn_InSb},
    {"Material": "Pt->Ge", "F": F_Pt, "Ksi": Ksi_Ge, "Eg": Eg_Ge, "Ro": Ro_Ge, "T": T, "ni": ni_Ge, "Mn": Mn_Ge},
    {"Material": "Pt->Si", "F": F_Pt, "Ksi": Ksi_Si, "Eg": Eg_Si, "Ro": Ro_Si, "T": T, "ni": ni_Si, "Mn": Mn_Si},
    {"Material": "Pt->GaAs", "F": F_Pt, "Ksi": Ksi_GaAs, "Eg": Eg_GaAs, "Ro": Ro_GaAs, "T": T, "ni": ni_GaAs, "Mn": Mn_GaAs},
    {"Material": "Pt->InSb", "F": F_Pt, "Ksi": Ksi_InSb, "Eg": Eg_InSb, "Ro": Ro_InSb, "T": T, "ni": ni_InSb, "Mn": Mn_InSb},
]

# Создание таблицы для хранения результатов
results = []

# Расчет высоты потенциального барьера для каждого набора данных
for material_data in data:
    # Удаляем ключ 'Material' из словаря
    material = material_data.pop("Material")
    Delta_Fi = calculate_barrier_height(**material_data)
    # Добавляем в результаты
    results.append({"Material": material, "F": material_data['F'], "Delta_Fi": Delta_Fi})

# Вывод результатов в виде таблицы
results_df = pd.DataFrame(results)
print(results_df)

# Получение данных для построения графика
x_values = results_df['F']
y_values = results_df['Delta_Fi']

# Построение точечного графика
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='blue')
plt.title('Контактная разность потенциалов vs. Работа выхода')
plt.xlabel('Работа выхода (F), эВ')
plt.ylabel('Контактная разность потенциалов (Delta_Fi), эВ')
plt.grid(True)

# Добавление пояснений к графику
for i, txt in enumerate(results_df['Material']):
    plt.text(x_values[i], y_values[i], txt, fontsize=9, ha='right')

plt.show()

