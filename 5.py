talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))
talents_to_gram= talents*20*32*13.3
pound_to_gram=pounds*32*13.3
lots_to_gram= lots*13.3
sum= talents_to_gram + pound_to_gram + lots_to_gram
gram= sum%1000
kg= sum//1000
gram=round(gram,2)

print("the weight in modern units: " + str(kg) +" kilograms and " + str(gram) +" grams")