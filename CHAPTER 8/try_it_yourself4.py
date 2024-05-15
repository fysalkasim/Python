# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.
# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() 
# with a copy of the list of messages. After calling the function, print both of your lists to show that the original 
# list has retained its messages.

def show_messages(listname):
    for i in listname:
        print(i)
l1 = ["HI","HOW ARE YOU","HOPE YOU ARE FINE","BE THE CHAMPION"]
def send_message(listname):
    completed_list = []
    for i in listname:
        print(f"\n The {i} has been sent")
        completed_list.append(i)
    print(f"The completed list is {completed_list}")

show_messages(l1)
send_message(l1)
print(f"the {l1}" )
