def hafta_kuni(raqam):
    kunlar = {
        1: "Dushanba",
        2: "Seshanba",
        3: "Chorshanba",
        4: "Payshanba",
        5: "Juma",
        6: "Shanba",
        7: "Yakshanba"
    }
    return kunlar.get(raqam, "Bunday hafta kuni yo'q")

user_input = int(input("Hafta kunining raqamini kiriting (1-7): "))
print(hafta_kuni(user_input))
oylar = {
    "iyun": "Hozir yozgi ta’til",
    "iyul": "Hozir yozgi ta’til",
    "avgust": "Hozir yozgi ta’til"
}

user_input = input("Oyni kiriting: ").lower()
if user_input in oylar:
    print(oylar[user_input])
else:
    print("Hozir o'qish vaqti")
def svetafor(rang):
    if rang.lower() == "qizil":
        return "To'xtang"
    elif rang.lower() == "sariq":
        return "Tayyorlaning"
    elif rang.lower() == "yashil":
        return "Yurishingiz mumkin"
    else:
        return "Noto'g'ri rang"

user_input = input("Svetafor rangini kiriting (Qizil, Sariq, Yashil): ")
print(svetafor(user_input))
user_input = input("Bir harf kiriting: ")

if user_input.isupper():
    print("Bosh harf")
elif user_input.islower():
    print("Kichik harf")
else:
    print("Bu harf emas")
