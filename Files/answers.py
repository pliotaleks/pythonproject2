user_language = input("����� ���� �� �����? ")
user_time = input("��� �����? ")
user_institution = input("���? ")

with open('answers.txt', 'w') as file:
    file.write(f"{user_language}\n")
    file.write(f"{user_time}\n")
    file.write(f"{user_institution}\n")

print("������ ��������")

