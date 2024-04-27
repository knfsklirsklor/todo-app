# text = input("Enter a title: ")
#
# dlina = len(text)
# print('Dlina xujni kotoruju napisal: ', dlina)

# password = input("Enter password: ")
#
# while password != "pass123":
#     password = input("Enter password: ")
#
# print("password is correct!")


# x = 1
#
# while x <= 6:
#     print(x)
#     x = x + 1


# eda = ['pasta', "pizza", 'salat']
#
# for meal in eda:
#     print(meal.capitalize())


# country = "India"
#
# match country:
#     case 'USA':
#         print("Hello")
#     case "India":
#         print("Namaste")
#     case "Germany":
#         print("Hallo")

# for item in ["sandals", "glasses", "trousers"):
#     print(item.capitalize())

# frazi = ['ebis naxuj'
#          ' pidaras', 'sasaj xuj sasajka', 'ebatisa sasatsia naxuj']
#
# filenames = ['piska.txt', 'zopa.txt', 'bliat.txt']
#
# for fraza, filename in zip(frazi, filenames):
#     file = open(f'.venv/papka/{filename}', 'w')
#     file.write(fraza)

#
# file = open('file.txt', 'w')
# file.writelines('snail')
# file.close()

# meme = input("vvedi xujniu kakuju nibud: ")
#
# file = open('members.txt', 'r')
# musk = file.readlines()
# print(musk)
# file.close()
#
# musk.append(meme + "\n")
#
# file = open('members.txt', 'w')
# musk = file.writelines(musk)
# file.close()


# member = input("Add a new member: ")
#
# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(member)
#
# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()

#
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello naxuj")
#     file.close()

# fajli = ['a.txt', 'b.txt', 'c.txt']
# #
# for fajl in fajli:
#     file = open(fajl, 'r')
#     meme = file.read()
#     print(meme)

file = open("data.txt", 'w')

file.write("100.12\n")
file.write("111.23")

file.close()