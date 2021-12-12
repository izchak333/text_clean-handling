import stop_word
#open file
file = open('text.txt', 'r+', encoding='utf-8')
file_str = file.read()


#create new file for filtered data
clean_file = open('text_clean.txt', 'a')
index = 0
#loop over STR for clean the text and get it reddy to counting
while index < len(file_str):
    #special charcter replace with ' ' one spece instad
    if file_str[index] == '—':
        clean_file.write(' ')

    #clean all ' - . , ? : and etc...'
    elif (file_str[index] == '-') or (file_str[index] == ',') or (file_str[index] == ';') \
            or (file_str[index] == '.') or (file_str[index] == ')') or (file_str[index] == '(') \
            or (file_str[index] == '!') or (file_str[index] == '?'):
        pass

    #if its a letter add it to new file
    else:
        clean_file.write(file_str[index])
    index += 1


file.close()
clean_file.close()
stop_word_count = 0
# takeout stop-word from text
clean_file = open('text_clean.txt', 'r')
count_word_list = []
for word in clean_file.read().split():
    if word in stop_word.list_stop_word:
        stop_word_count += 1
    else:
        count_word_list.append(word)

#tuple (word,mention,index)
list_for_sort = []
for i in count_word_list:
    if i in list_for_sort:
        print(i[1])
    else:
        list_for_sort.append([i, count_word_list.count(i), count_word_list.index(i)])

#sort by mention
sort_l_duplicate = sorted(list_for_sort, key=lambda x: x[1], reverse=True)
list_one_sort = []

#take sort list and remove duplicate
for i in sort_l_duplicate:
    if i not in list_one_sort:
        list_one_sort.append(i)


print(f'filter total of {stop_word_count} stop-word in text.\n\n')

for i in range(10):
    print(f'{i+1}. Word : {list_one_sort[i][0]}\n   number of mention is : {list_one_sort[i][1]}\n')
