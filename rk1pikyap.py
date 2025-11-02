from dataclasses import dataclass


@dataclass
class Postavshik:
    id_postavshika: int
    naimenovanie: str


@dataclass
class Detal:
    id_detali: int
    naimenovanie: str
    stoimost: float
    id_postavshika: int


@dataclass
class PostavshikDetal:
    id_postavshika: int
    id_detali: int


postavshiki = [
    Postavshik(1, "ООО Автодеталь"),
    Postavshik(2, "ИП Иванов - отдел металлов"),
    Postavshik(3, "ЗАО Механика"),
    Postavshik(4, "ООО Промышленный"),
    Postavshik(5, "Торговая фирма отдел электроники")
]

detali = [
    Detal(1, "Шкив коленвала", 1250.50, 1),
    Detal(2, "Поршень", 890.00, 1),
    Detal(3, "Тормозная колодка", 340.75, 1),
    Detal(4, "Рычаг подвески", 1560.00, 2),
    Detal(5, "Кузовная панель", 2100.25, 2),
    Detal(6, "Амортизатор", 980.00, 3),
    Detal(7, "Гайка М12", 15.50, 3),
    Detal(8, "Фильтр масляный", 250.00, 3),
    Detal(9, "Свеча зажигания", 120.00, 5),
    Detal(10, "Датчик кислорода", 1850.00, 5)
]

svyazi_postavshik_detal = [
    PostavshikDetal(1, 1), PostavshikDetal(1, 2), PostavshikDetal(1, 3),
    PostavshikDetal(2, 4), PostavshikDetal(2, 5), PostavshikDetal(3, 6),
    PostavshikDetal(3, 7), PostavshikDetal(3, 8), PostavshikDetal(5, 9),
    PostavshikDetal(5, 10), PostavshikDetal(2, 6), PostavshikDetal(3, 1),
    PostavshikDetal(4, 2)
]


def zapros1():
    print("\n" + "=" * 80)
    print("ЗАПРОС 1: Список всех связанных деталей и поставщиков (один-ко-многим)")
    print("=" * 80)
    rezultat = sorted([(d, p) for p in postavshiki for d in detali
                       if d.id_postavshika == p.id_postavshika],
                      key=lambda x: (x[1].id_postavshika, x[0].naimenovanie))
    for d, p in rezultat:
        print(f"Поставщик: {p.naimenovanie:<35} | Деталь: {d.naimenovanie:<25} | Стоимость: {d.stoimost:>10.2f}")
    return rezultat


def zapros2():
    print("\n" + "=" * 80)
    print("ЗАПРОС 2: Список поставщиков с суммарной стоимостью деталей")
    print("=" * 80)
    summa = {d.id_postavshika: sum(d2.stoimost for d2 in detali if d2.id_postavshika == d.id_postavshika)
             for d in detali}
    rezultat = sorted([(p, summa[p.id_postavshika]) for p in postavshiki
                       if p.id_postavshika in summa], key=lambda x: x[1])
    for p, s in rezultat:
        print(f"Поставщик: {p.naimenovanie:<40} | Суммарная стоимость: {s:>12.2f} руб.")
    return rezultat


def zapros3():
    print("\n" + "=" * 80)
    print("ЗАПРОС 3: Поставщики со словом 'отдел' и их детали (многие-ко-многим)")
    print("=" * 80)
    postavshiki_s_otdelom = [p for p in postavshiki if "отдел" in p.naimenovanie.lower()]
    rezultat = []
    for p in postavshiki_s_otdelom:
        detali_p = [d for d in detali
                    if d.id_detali in [sv.id_detali for sv in svyazi_postavshik_detal
                                       if sv.id_postavshika == p.id_postavshika]]
        if detali_p:
            print(f"\nПоставщик: {p.naimenovanie}")
            for d in detali_p:
                print(f"  └─ Деталь: {d.naimenovanie:<30} | Стоимость: {d.stoimost:>10.2f}")
            rezultat.append((p, detali_p))
    return rezultat


def sozdat_pdf(output_buffer, filename="rk1pykyap.py"):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER

        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()

        doc = SimpleDocTemplate("rubegnyi_kontrol.pdf", pagesize=A4,
                                rightMargin=20 * mm, leftMargin=20 * mm,
                                topMargin=20 * mm, bottomMargin=20 * mm)
        styles = getSampleStyleSheet()
        style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16,
                               textColor='#0066CC', spaceAfter=10, alignment=TA_CENTER)

        story = []
        story.append(Paragraph("РУБЕЖНЫЙ КОНТРОЛЬ", style))
        story.append(Paragraph("Предметная область: Деталь - Поставщик", styles['Heading2']))
        story.append(Spacer(1, 10))

        story.append(Paragraph("ТЕКСТ ПРОГРАММЫ", styles['Heading2']))
        story.append(Spacer(1, 5))
        story.append(Preformatted(code, styles['Code']))

        story.append(Spacer(1, 10))
        story.append(Paragraph("РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ", styles['Heading2']))
        story.append(Spacer(1, 5))
        story.append(Preformatted(output_buffer, styles['Code']))

        doc.build(story)
        print("\n✓ PDF создан: rubegnyi_kontrol.pdf")
        return True
    except ImportError:
        print("\n⚠ Библиотека reportlab не установлена. PDF не будет создан.")
        print("   Установите: pip install reportlab")
        return False


import sys
from io import StringIO

if __name__ == "__main__":
    output_buffer = StringIO()
    old_stdout = sys.stdout
    sys.stdout = output_buffer

    print("\n" + "=" * 80)
    print("РУБЕЖНЫЙ КОНТРОЛЬ")
    print("Предметная область: Деталь - Поставщик")
    print("=" * 80)

    zapros1()
    zapros2()
    zapros3()

    print("\n" + "=" * 80)
    print("Выполнение программы завершено")
    print("=" * 80)

    output_text = output_buffer.getvalue()
    sys.stdout = old_stdout
    print(output_text)
    sozdat_pdf(output_text, __file__)
