  
class Buffer:
    def load_buffer(self):
        arq = open('exemplo2.lcc', 'r', encoding="utf8")
        text = arq.readline()

        buffer = []
        cont = 1

        while text != "":
            buffer.append(text)
            text = arq.readline()
            cont += 1

            if cont == 10 or text == '':
                buf = ''.join(buffer)
                cont = 1
                yield buf

                buffer = []

        arq.close()