words = input().split()
text_even_lenght = [word for word in words if len(word) % 2 == 0]
print("\n".join(text_even_lenght))
