data segment
    enter_msg db 'Enter a string: $'
    str1 db 20 dup('$')            ; Buffer for user input copy
    strrev db 20 dup('$')           ; Buffer for reversed string
    str_palin db 0Dh,0Ah,'String is Palindrome.$'
    str_not_palin db 0Dh,0Ah,'String is not Palindrome.$'
    input_buffer db 20, ?, 20 dup('$') ; For DOS buffered input (size = 20)
data ends

code segment
assume cs:code, ds:data

begin:
    ; Initialize data segment
    mov ax, data
    mov ds, ax
    mov es, ax

    ; Show "Enter a string:"
    mov ah, 9
    lea dx, enter_msg
    int 21h

    ; Take user input
    mov ah, 0Ah
    lea dx, input_buffer
    int 21h

    ; Find string length
    lea si, input_buffer + 2    ; SI points to first character of input
    mov cl, [input_buffer+1]    ; Number of characters entered
    mov ch, 0
    mov bx, cx                  ; Save length in BX

    ; Copy user input to str1
    lea di, str1
copy_input:
    mov al, [si]
    mov [di], al
    inc si
    inc di
    loop copy_input

    ; Add '$' at end of str1
    mov al, '$'
    mov [di], al

    ; Reverse str1 into strrev
    lea si, str1
    lea di, strrev
    mov cx, bx
    add si, cx
    dec si                      ; SI points to last character now

reverse_string:
    mov al, [si]
    mov [di], al
    dec si
    inc di
    loop reverse_string

    ; Add '$' at end of strrev
    mov al, '$'
    mov [di], al

    ; Compare str1 and strrev
    lea si, str1
    lea di, strrev
    mov cx, bx                  ; Compare only the entered characters
compare_strings:
    mov al, [si]
    mov ah, [di]
    cmp al, ah
    jne not_palin
    inc si
    inc di
    loop compare_strings

palin:
    mov ah, 9
    lea dx, str_palin
    int 21h
    jmp exit

not_palin:
    mov ah, 9
    lea dx, str_not_palin
    int 21h

exit:
    mov ah, 4Ch
    int 21h

code ends
end begin
