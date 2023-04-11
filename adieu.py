
import inflect

p = inflect.engine()

answer = ["Adieu", "adieu"] #statement has to start with adieu
while True:
    try:
        x = input("Enter your name: ")

    except EOFError:
        print()
        break
    answer.append()


if len(answer)== 3:
    new_answer = p.join(answer, conj='')

elif len(answer) ==4:
    new_answer = p.join(answer, final_sep='')
else:
    new_answer = p.join(answer)

print(new_answer)
