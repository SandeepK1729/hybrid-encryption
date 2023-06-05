from django.shortcuts import render
from django.http import JsonResponse
from .encryption import (
    caesar_encrypt, caesar_decrypt,
    playfair_encrypt, playfair_decrypt,
    aes_encrypt, aes_decrypt,
    otp_encrypt, otp_decrypt,
    railfence_encrypt, railfence_decrypt,
)

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        operation = request.POST.get('operation')
        algorithm1 = request.POST.get('algorithm1')
        key1 = request.POST.get('key1')
        algorithm2 = request.POST.get('algorithm2')
        key2 = request.POST.get('key2')
        algorithm3 = request.POST.get('algorithm3')
        key3 = request.POST.get('key3')

        if algorithm1 == 'caesar':
            if operation == 'encrypt':
                text = caesar_encrypt(text, int(key1))
            elif operation == 'decrypt':
                text = caesar_decrypt(text, int(key1))
        elif algorithm1 == 'playfair':
            if operation == 'encrypt':
                text = playfair_encrypt(text, key1)
            elif operation == 'decrypt':
                text = playfair_decrypt(text, key1)
        elif algorithm1 == 'aes':
            if operation == 'encrypt':
                text = aes_encrypt(text, key1)
            elif operation == 'decrypt':
                text = aes_decrypt(text, key1)
        elif algorithm1 == 'otp':
            if operation == 'encrypt':
                text = otp_encrypt(text, key1)
            elif operation == 'decrypt':
                text = otp_decrypt(text, key1)
        elif algorithm1 == 'railfence':
            if operation == 'encrypt':
                text = railfence_encrypt(text, int(key1))
            elif operation == 'decrypt':
                text = railfence_decrypt(text, int(key1))

        return JsonResponse({'result': text})

    return render(request, 'encryption.html')