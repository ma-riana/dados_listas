class Elemento:

    def __init__(self, valor, ref=None):
        self.__valor = valor
        self.__ref = ref

    @property
    def valor(self):
        return self.__valor

    @property
    def ref(self):
        return self.__ref

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @ref.setter
    def ref(self, ref):
        self.__ref = ref


class Lista:

    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__contador = 0

    def inserir_como_primeiro(self, valor):
        if self.__contador == 0:
            self.__primeiro = Elemento(valor)
        else:
            self.__primeiro = Elemento(valor, self.__primeiro)
        self.__contador += 1
        self.listagem()

    def inserir_como_ultimo(self, valor):
        if self.__contador == 0:
            self.__ultimo = Elemento(valor)
        else:
            ele = self.__primeiro
            for i in range(self.__contador):
                if ele.ref is None:
                    self.__ultimo = Elemento(valor)
                    ele.ref = self.__ultimo
                else:
                    ele = ele.ref
        self.__contador += 1
        self.listagem()

    def remover_primeiro(self):
        self.__primeiro = self.__primeiro.ref
        self.__contador -= 1
        self.listagem()

    def busca(self, valor):
        ele = self.__primeiro
        for i in range(self.__contador):
            if ele.valor == valor:
                return ele
            else:
                ele = ele.ref
        return 'Não encontrado'

    def listagem(self):
        ele = self.__primeiro
        for i in range(self.__contador):
            print(ele.valor)
            ele = ele.ref
        print('\n')

    def listagem_cm_ref(self):
        ele = self.__primeiro
        for i in range(self.__contador):
            if ele.ref is None:
                print(f'Valor: {ele.valor}')
            else:
                print(f'Valor: {ele.valor}, Referente: {ele.ref.valor}')
                ele = ele.ref
        print('\n')
