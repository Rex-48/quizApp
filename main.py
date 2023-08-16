import requests
import random
import html


url = "https://opentdb.com/api.php?amount=20&category=18"

respose = requests.get(url)

unsorted_data = respose.json()

Sorted_data = unsorted_data['results'] 


# print(result[1])
# print("the lenght of the dictionary is ",len(result))

print(" \n ")



def decode_html(encoded_text):
    decoded_text = html.unescape(encoded_text)
    return decoded_text


def add_element_randomly(input_list, element):
    random_index = random.randint(0, len(input_list))
    input_list.insert(random_index, element)
    return input_list



def interface(category ,question_type ,question ,correct_ans ,incorrect_ans ,options ,i):
    print("Question Type : ",question_type)
    if question_type == "multiple":
        print("Question ",i," : ",decode_html(question))
        print("a. "+options[0])
        print("b. "+options[1])
        print("c. "+options[2])
        print("d. "+options[3])
        print(" ")

        user = str(input("user : "))
        if user == str(correct_ans):
            print("correct")
        
        else:
            print("incorrect")
            print(str(correct_ans))


    else:
        print("Question ",i," : ",decode_html(question))
        print("a. True")
        print("b. False")

        user = str(input("user : "))
        if user in incorrect_ans:
            print("incorrect Answer")
            print(correct_ans)
        else:
            print("correct Answer")
            

    print("\n")



for i in range(len(Sorted_data)):

    matter = Sorted_data[i]

    category = matter['category']
    question_type = matter['type']
    question = matter['question']
    correct_ans = matter['correct_answer']
    incorrect_ans = matter['incorrect_answers']
    options = add_element_randomly(incorrect_ans,correct_ans)
    interface(category ,question_type ,question ,correct_ans ,incorrect_ans ,options ,i)

    





