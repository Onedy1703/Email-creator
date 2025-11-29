def generate_emails():
    # Чтение файлов
    try:
        with open('firstname_1letter_ru.txt', 'r', encoding='utf-8') as f:
            first_names = [line.strip().lower() for line in f if line.strip()]
        
        with open('russian_trans_surnames.txt', 'r', encoding='utf-8') as f:
            last_names = [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
        return
    
    print("=" * 50)
    print("ГЕНЕРАТОР EMAIL АДРЕСОВ")
    print("=" * 50)
    
    # Выбор формата email
    print("\nВыберите формат email:")
    print("1 - ivanov.i@company.com")
    print("2 - i.ivanov@company.com")
    
    while True:
        format_choice = input("Введите 1 или 2: ").strip()
        if format_choice in ['1', '2']:
            break
        print("Неверный выбор! Пожалуйста, введите 1 или 2.")
    
    # Ввод домена
    domain = input("Введите домен (например: company.com): ").strip()
    
    # Предварительный просмотр
    print("\n" + "=" * 50)
    print("ПРЕДВАРИТЕЛЬНЫЙ ПРОСМОТР")
    print("=" * 50)
    
    # Генерация примера (первая комбинация)
    first_letter = first_names[0]
    last_name = last_names[0]
    
    if format_choice == '1':
        example_email = f"{last_name}.{first_letter}@{domain}"
    else:
        example_email = f"{first_letter}.{last_name}@{domain}"
    
    print(f"Пример email: {example_email}")
    print(f"Всего будет сгенерировано: {len(first_names) * len(last_names)} адресов")
    
    # Подтверждение
    print("\n" + "=" * 50)
    confirm = input("Продолжить генерацию? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("Генерация отменена.")
        return
    
    # Генерация всех email адресов
    print("\nГенерация email адресов...")
    emails = []
    
    for last_name in last_names:
        for first_letter in first_names:
            if format_choice == '1':
                email = f"{last_name}.{first_letter}@{domain}"
            else:
                email = f"{first_letter}.{last_name}@{domain}"
            
            emails.append(email)
    
    # Сохранение результатов
    output_file = 'generated_emails.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for email in emails:
            f.write(email + '\n')
    
    print(f"\n✅ Сгенерировано {len(emails)} email адресов")
    print(f"📁 Результат сохранен в файл: {output_file}")
    
    # Показать запрошенные строки
    print("\n" + "=" * 50)
    print("ЗАПРОШЕННЫЕ СТРОКИ")
    print("=" * 50)
    
    requested_lines = [1, 100, 200, len(emails)]
    for line_num in requested_lines:
        if line_num <= len(emails):
            print(f"{line_num}: {emails[line_num-1]}")
        else:
            print(f"{line_num}: (не существует)")

# Запуск программы
if __name__ == "__main__":
    generate_emails()