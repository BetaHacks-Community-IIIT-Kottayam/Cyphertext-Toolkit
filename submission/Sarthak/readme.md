# Custom OK Code Encoder/Decoder

This Python script allows users to encode and decode text using a custom code where dots ('.') are represented as 'o' and dashes ('-') are represented as 'k'.

## Usage

### Encoding

To encode a text, import the script and run the function `ok_code_encode`:

```python
import ok_code as okc

print(okc.ok_code_encode('Hello World'))
```
Enter the text you want to encode as the function parameter. The script will then output the corresponding custom code.

Output:
```bash
oooo o okoo okoo kkk / okk kkk oko okoo koo
```


### Decoding

To decode a custom code, import the script and run the function `ok_code_decode`:

```python
import ok_code as okc

print(okc.ok_code_decode('oooo o okoo okoo kkk / okk kkk oko okoo koo'))
```
Enter the custom code you want to decode as the function parameter. The script will then output the corresponding text.

Output:
```bash
Hello World
```

Note
----

*   The custom code uses 'o' for dots and 'k' for dashes.
*   Spaces are represented by a forward slash ('/').

Author
------

\[Sarthak Gupta\]
