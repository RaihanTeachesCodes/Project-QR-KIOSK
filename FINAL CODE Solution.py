import keyboard
import pyautogui

with open('food json.txt', 'r') as file:
    contents = file.read()

dictionary = eval(contents)

food_articles = list(dictionary.keys())

food_list = food_articles + ["000000000","*00000000", "^0000000+"]

print(food_list)

word_buffer = []
read = []
global combined
combined = ["*00000000"]

def combine_func():
    pyautogui.press('enter')
    pyautogui.press('enter') 
    print("end buffer detected")
    order_list = []
    combined.pop(0)
    combined.pop(-1)
    combined.append("^0000000+")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace') #deleting everyhting
    print("combined list: " + str(combined))
    for order_article in combined:
            if order_article != "^0000000+":
                pyautogui.typewrite(order_article) #write everything from the left 
                print(order_article)
                pyautogui.press('enter')
            elif order_article == "^0000000+":
                pyautogui.typewrite(order_article) #write everything from the left 
                print(order_article)

    pyautogui.press('backspace', presses=10)
    
    combined.clear()
    print("done writing")
    
    
        
def on_key_press(event):

    if "^0000000+" in combined:
        combined.clear()
    
    if combined == ["*00000000"]:
        print("start buffer activated")

    if len(combined) == 0:
        combined.append("*00000000")

    if event.name.lower() == 'esc':
        word_buffer.append('esc')

    elif len(event.name) == 1:


        word_buffer.append(event.name)
        check_word_buffer()
        combined_word = ''.join(str(element)[-1] for element in word_buffer[-9:])
        reversed_word = combined_word[::-1]
        reversed_output = reversed_word[::-1] #taking the actual 9 word process
        print(combined)
        print(reversed_output)

        if reversed_output in food_list:
            if "^0000000+" in combined:
                combined.clear()
            print("food in list")
            full_length = len(word_buffer)
            minus_cut = full_length - 9
            word_buffer_new = word_buffer[minus_cut:] #taking the last 9 letters
            combined_word_new = ''.join(str(element) for element in word_buffer_new) #combining the last 9 lettes and making it into a string 
            print(combined_word_new)
            word_buffer.clear()
            word_buffer.extend(combined_word_new)
            combined.append(reversed_output) #putting the word into the combined list
            print(combined)

        if combined[len(combined) - 1] == "000000000" and combined[0] == "*00000000":
            print("last buffer detected")
            combine_func()
    
        check_word_buffer()



def check_word_buffer():
    if len(word_buffer) >= 3:
        typed_word = ''.join(word_buffer[-3:])
        if typed_word.lower() == 'esc':
            stop_program()

def stop_program():
    print("Program stopped")
    keyboard.unhook_all()
    raise SystemExit


keyboard.on_press(on_key_press)
keyboard.wait('esc')
