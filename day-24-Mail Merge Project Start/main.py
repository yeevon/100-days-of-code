#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
with open("./Input/Letters/starting_letter.txt") as invite:
    letter = invite.read()
    for name in names:
        new_letter = letter.replace("[name]", name.strip())

        with open(f"./Output/ReadyToSend/{name.strip('\n')} Invite", mode="w") as final_invite:
            final_invite.write(new_letter)
