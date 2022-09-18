class Sequential:
    def __init__(self):
        self.model = []
        self.addlayer = True
        self.activations = ['sigmoid', 'tanh', 'relu', 'relu2', 'cutoff']

    def check_activation(self, x):
        found = False
        for a in self.activations:
            if (a == x): found = True
        return found

    def add(self, layer):
        if self.addlayer:
            if len(layer) == 2:
                if not self.check_activation(layer[1]):
                    self.model.append(layer)
                else:
                    raise ValueError("Your models activation is not found / not supported")
            else:
                raise Exception("Your input is of an incorrect shape")
        else:
            raise Exception("Model is already compiled")

    def compile(self, hard_drive=False, preload=True):
        import numpy as np

        model = self.model
        modelout = []
        if hard_drive:
            raise ValueError("Hard drive optimizations are currently not optimized")
            return 1
        else:
            final = []
            for im in range(len(model) - 1):  # Weight Creation
                m1 = []
                for i in range(model[im][0]):
                    m2 = []
                    for j in range(model[im + 1][0]):
                        m3 = []
                        for k in range(model[im][0]):
                            m3.append(np.random.uniform(0, 1))
                        m2.append(m3)
                    m1.append(m2)
                final.append(m1)
            modelout.append(final)
            final = []
            for im in range(len(model) - 1):  # Bias Creation
                if im != 0:
                    m1 = []
                    for i in range(model[im][0]):
                        m1.append(np.random.uniform(0, 1))
                    final.append([m1])
            modelout.append(final)
            if(preload):
                self.wbc = modelout # wbc = weights-biases-compute
            self.addlayer = False
            return modelout

    def preload(self, inputs, preload=True):
        print(self.model)
        modelout = []
        modelout.append(inputs)
        self.inlayer = inputs
        for im in range(len(self.model)):  # Activation Inititalization
            if im != 0:
                m1 = []
                for i in range(self.model[im][0]):
                    m1.append(0)
                modelout.append(m1)
        if preload:
            self.pm = modelout  # Preloaded Model
        return modelout

    def compute_losses(self, model_compiled, self_add=True):
        modelout = []
        for im in range(len(self.model)):  # Activation Inititalization
            if im != 0:
                m1 = []
                for i in range(self.model[im][0]):
                    activation = self.model[im][1]
                    for k in range(self.model[im - 1][0]):
                        value = self.pm[im - 1][k]
                        weight = self.wbc[0][0][im - 1][i][k]
                        print(f'value: {value}, weight: {weight}')
                modelout.append(m1)


