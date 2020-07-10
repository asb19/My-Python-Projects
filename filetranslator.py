from translate import Translator

translator=Translator(to_lang='es')
try:

    with open('test.txt','r') as reader:
        data=reader.read()
    try:
        spanish_translation=translator.translate(data)
        with open("test_spanish.txt",'w') as writer:
            writer.write(spanish_translation)
    except IOError as error:
        print("AN error occured")
        raise error
except FileNotFoundError as error:
    print("An error occured")
    raise error
